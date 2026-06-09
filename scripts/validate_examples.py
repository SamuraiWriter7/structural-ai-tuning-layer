#!/usr/bin/env python3
"""
Validate Structural AI Tuning Layer example YAML files against JSON Schemas.

Required packages:
pip install pyyaml jsonschema

Usage:
python scripts/validate_examples.py
"""

import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    print("Missing dependency: PyYAML")
    print("Install with: pip install pyyaml")
    raise SystemExit(1) from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError as exc:
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    raise SystemExit(1) from exc

REPO_ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Structural Tuning Record",
        "schema": "schemas/structural-tuning-record.schema.json",
        "example": "examples/structural-tuning-record.example.yaml",
    }
]


def load_json(path: Path) -> Any:
    """Load a JSON file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise RuntimeError(f"JSON file not found: {path}")
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc


def load_yaml(path: Path) -> Any:
    """Load a YAML file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise RuntimeError(f"YAML file not found: {path}")
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc


def format_error_path(error: Any) -> str:
    """Format a jsonschema validation error path."""
    if not error.path:
        return "<root>"

    parts = []
    for item in error.path:
        if isinstance(item, int):
            parts.append(f"[{item}]")
        else:
            if parts:
                parts.append(f".{item}")
            else:
                parts.append(str(item))

    return "".join(parts)


def validate_schema(schema: Any, schema_path: Path) -> None:
    """Validate that the schema itself is valid Draft 2020-12 JSON Schema."""
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise RuntimeError(f"Invalid JSON Schema in {schema_path}: {exc.message}") from exc


def validate_example_against_schema(
    *,
    target_name: str,
    schema_path: Path,
    example_path: Path,
) -> bool:
    """Validate one YAML example against one JSON Schema."""
    print(f"Validating target: {target_name}")
    print(f"  Schema : {schema_path.relative_to(REPO_ROOT)}")
    print(f"  Example: {example_path.relative_to(REPO_ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validate_schema(schema, schema_path)

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))

    if errors:
        print("  Result : failed\n")
        for error in errors:
            print(f"  Error at {format_error_path(error)}:")
            print(f"    {error.message}")
        print()
        return False

    print("  Result : passed\n")
    return True


def run_structural_consistency_checks(example: Any) -> list[str]:
    """
    Run minimal governance-aware consistency checks.
    These checks go beyond JSON Schema validation.
    """
    errors: list[str] = []

    action = example.get("action", {})
    governance_state = example.get("governance_state", {})
    recovery_gate = example.get("recovery_gate")
    human_review = example.get("human_review", {})
    structural_result = example.get("structural_tuning_result", {})

    action_type = action.get("action_type")

    if action_type == "recovery" and recovery_gate is None:
        errors.append("Recovery actions must include a recovery_gate section.")

    if recovery_gate is not None:
        recovery_gate_status = recovery_gate.get("recovery_gate_status")
        recovery_allowed = recovery_gate.get("recovery_allowed")

        if recovery_gate_status == "passed" and recovery_allowed is not True:
            errors.append(
                "recovery_gate_status is passed, but recovery_allowed is not true."
            )

        if recovery_gate_status in {"blocked", "failed"} and recovery_allowed is True:
            errors.append(
                "recovery_gate_status is blocked or failed, but recovery_allowed is true."
            )

    human_review_required = human_review.get("human_review_required")
    human_review_status = human_review.get("human_review_status")

    if human_review_required is True and human_review_status == "not_required":
        errors.append(
            "human_review_required is true, but human_review_status is not_required."
        )

    if human_review_required is False and human_review_status != "not_required":
        errors.append(
            "human_review_required is false, but human_review_status is not not_required."
        )

    governance_human_review_status = governance_state.get("human_review_status")
    if (
        governance_human_review_status is not None
        and human_review_status is not None
        and governance_human_review_status != human_review_status
    ):
        errors.append(
            "governance_state.human_review_status does not match "
            "human_review.human_review_status."
        )

    structural_action_allowed = structural_result.get("action_allowed")
    human_review_action_allowed = human_review.get("action_allowed")

    if (
        structural_action_allowed is not None
        and human_review_action_allowed is not None
        and structural_action_allowed is True
        and human_review_action_allowed is False
    ):
        errors.append(
            "structural_tuning_result.action_allowed is true, but "
            "human_review.action_allowed is false."
        )

    return errors


def run_additional_checks(target_name: str, example_path: Path) -> bool:
    """Run target-specific structural consistency checks."""
    example = load_yaml(example_path)

    if target_name != "Structural Tuning Record":
        return True

    print(f"Running structural consistency checks: {target_name}")

    errors = run_structural_consistency_checks(example)

    if errors:
        print("  Result : failed\n")
        for error in errors:
            print(f"  Error: {error}")
        print()
        return False

    print("  Result : passed\n")
    return True


def main() -> int:
    all_passed = True

    for target in VALIDATION_TARGETS:
        target_name = target["name"]
        schema_path = REPO_ROOT / target["schema"]
        example_path = REPO_ROOT / target["example"]

        try:
            schema_passed = validate_example_against_schema(
                target_name=target_name,
                schema_path=schema_path,
                example_path=example_path,
            )

            structural_passed = run_additional_checks(target_name, example_path)

            if not schema_passed or not structural_passed:
                all_passed = False

        except RuntimeError as exc:
            all_passed = False
            print(f"Validation failed for target: {target_name}")
            print(f"Error: {exc}\n")

    if all_passed:
        print("All validations passed.")
        return 0

    print("One or more validations failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

