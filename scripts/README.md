# Scripts

This directory will contain validation and checking scripts for the **Structural AI Tuning Layer**.

The scripts will support schema validation, example validation, recovery gate checks, constitution alignment checks, semantic drift detection, human review boundary checks, and incident lifecycle consistency checks.

---

## Purpose

The purpose of this directory is to provide executable tools for checking the structured records defined by this project.

```text
docs/     = conceptual and governance specifications
schemas/  = machine-readable validation structures
examples/ = concrete YAML records
scripts/  = validation and structural checking tools
```

The scripts should help determine whether examples and records are not only syntactically valid, but also structurally aligned.

---

## Planned Scripts

Future versions may include the following scripts.

```text
scripts/
└─ validate_examples.py
```

Additional scripts may be added later as the project evolves.

Possible future scripts:

```text
scripts/
├─ validate_examples.py
├─ check_recovery_gate.py
├─ check_constitution_alignment.py
├─ check_semantic_drift.py
├─ check_human_review_boundary.py
└─ check_incident_lifecycle.py
```

---

## Primary Script

### `validate_examples.py`

The first planned script is:

```text
scripts/validate_examples.py
```

This script will validate YAML examples in the `examples/` directory against JSON Schemas in the `schemas/` directory.

Planned validation targets:

```text
schemas/structural-tuning-record.schema.json
examples/structural-tuning-record.example.yaml

schemas/recovery-gate.schema.json
examples/recovery-gate.example.yaml

schemas/constitution-alignment.schema.json
examples/constitution-alignment.example.yaml

schemas/semantic-drift.schema.json
examples/semantic-drift.example.yaml

schemas/human-review-boundary.schema.json
examples/human-review-boundary.example.yaml

schemas/incident-lifecycle.schema.json
examples/incident-lifecycle.example.yaml
```

---

## Planned Validation Flow

A future validation flow may look like this:

```text
YAML example
↓
YAML parsing
↓
JSON Schema validation
↓
structural consistency check
↓
constitution alignment check
↓
semantic drift check
↓
recovery gate check
↓
human review boundary check
↓
incident lifecycle check
↓
validation result
```

The first implementation may only perform JSON Schema validation.

Later versions may add semantic and governance-aware checks.

---

## Validation Layers

The project may eventually support multiple validation layers.

### 1. Syntax Validation

Checks whether YAML files can be parsed correctly.

Example failure:

```text
Invalid YAML syntax.
```

### 2. Schema Validation

Checks whether examples match the required JSON Schema.

Example failure:

```text
Missing required field: recovery_gate_result.
```

### 3. Structural Consistency Validation

Checks whether related fields are internally consistent.

Example failure:

```text
recovery_allowed is true, but recovery_gate_status is blocked.
```

### 4. Constitution Alignment Validation

Checks whether actions satisfy declared constitutional or institutional principles.

Example failure:

```text
Recovery requested without verification.
```

### 5. Semantic Drift Validation

Checks whether labels still match their required institutional meaning.

Example failure:

```text
claimed_state is recovered, but verification_status is in_progress.
```

### 6. Human Review Boundary Validation

Checks whether required human review was completed or explicitly marked as not required.

Example failure:

```text
Human review is required, but human_review_status is pending.
```

### 7. Incident Lifecycle Validation

Checks whether incident phase transitions are structurally valid.

Example failure:

```text
Incident moved from detected directly to recovered.
```

---

## Planned Command

A future validation command may be:

```bash
python scripts/validate_examples.py
```

Expected output may look like:

```text
Validating Structural Tuning Record...
  schema: schemas/structural-tuning-record.schema.json
  example: examples/structural-tuning-record.example.yaml
  result: passed

Validating Recovery Gate...
  schema: schemas/recovery-gate.schema.json
  example: examples/recovery-gate.example.yaml
  result: passed

All validations passed.
```

A failed validation may look like:

```text
Validation failed.
Target: Recovery Gate
Example: examples/recovery-gate.example.yaml
Error: recovery_allowed is true, but recovery_gate_status is blocked.
```

---

## Script Design Principles

Scripts in this directory should follow these principles.

### 1. Specification First

Scripts should implement checks based on the specifications in `docs/`.

A script should not introduce undocumented governance rules.

### 2. Clear Error Messages

Validation errors should explain what failed and why.

A useful error message should identify:

* target name,
* schema file,
* example file,
* failing field,
* reason for failure.

### 3. Fail Fast for Syntax Errors

Invalid YAML or invalid JSON Schema should stop validation early.

### 4. Separate Schema Checks from Governance Checks

Schema validation and structural governance validation should be clearly separated.

A record may pass schema validation but fail structural checks.

### 5. Human Review Must Not Be Implied

Scripts should not treat missing human review data as approval.

### 6. Recovery Must Be Verified

Scripts should enforce the principle:

```text
No recovery without verification.
```

### 7. Labels Must Match Meaning

Scripts should support detection of semantic drift.

A label such as `recovered`, `approved`, or `verified` should be checked against required conditions.

---

## Planned Dependencies

The first validation script may use:

```text
Python 3.10+
PyYAML
jsonschema
```

Possible installation command:

```bash
pip install pyyaml jsonschema
```

Future versions may avoid external dependencies where possible, but initial validation can use standard Python ecosystem tools.

---

## Current Status

This directory is currently reserved for future validation scripts.

The first planned script is:

```text
scripts/validate_examples.py
```

This script will likely be introduced after the first schemas and examples are added.

---

## Closing Statement

Scripts turn structural principles into executable checks.

They do not replace governance judgment.

They make governance judgment easier to test, repeat, and review.

```text
Documents define meaning.
Schemas define structure.
Examples show records.
Scripts check alignment.
```
