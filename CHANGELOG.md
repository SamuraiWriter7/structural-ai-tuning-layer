# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple versioning structure during the early specification phase.

---

## [0.2.0-candidate] - 2026-06-09

### Added Schema Layer

* Added `schemas/README.md`.

  * Defines the purpose of the `schemas/` directory.
  * Describes planned schemas for:

    * structural tuning records
    * recovery gates
    * constitution alignment
    * semantic drift detection
    * human review boundaries
    * incident lifecycle records
  * Defines schema design principles such as:

    * specification first
    * checkable principles
    * explicit status fields
    * traceability
    * human review visibility
    * recovery safety
    * drift detection

* Added `schemas/structural-tuning-record.schema.json`.

  * Defines the first machine-readable schema for Structural AI Tuning Layer.
  * Covers:

    * record type and version
    * action metadata
    * governance state
    * constitutional alignment
    * semantic drift
    * recovery gate
    * human review
    * incident lifecycle
    * traceability
    * structural tuning result
  * Adds conditional schema behavior requiring `recovery_gate` when `action_type` is `recovery`.
  * Adds a constraint preventing `human_review_status: not_required` when `human_review_required` is `true`.

### Added Example Layer

* Added `examples/README.md`.

  * Defines the purpose of the `examples/` directory.
  * Describes planned YAML examples for:

    * structural tuning records
    * recovery gates
    * constitution alignment
    * semantic drift detection
    * human review boundaries
    * incident lifecycle records
  * Defines the relationship between `docs/`, `schemas/`, and `examples/`.
  * Introduces valid and invalid example naming conventions.

* Added `examples/structural-tuning-record.example.yaml`.

  * Provides the first valid example record for Structural AI Tuning Layer.
  * Demonstrates a structurally aligned recovery action.
  * Includes:

    * action metadata
    * governance state
    * constitutional principles
    * semantic drift evaluation
    * recovery gate result
    * human review boundary result
    * incident lifecycle state
    * traceability references
    * structural tuning result

### Added Script Layer

* Added `scripts/README.md`.

  * Defines the purpose of the `scripts/` directory.
  * Describes planned validation scripts and validation layers.
  * Defines script design principles including:

    * specification first
    * clear error messages
    * fail fast for syntax errors
    * separation of schema checks and governance checks
    * explicit human review handling
    * recovery verification
    * semantic drift detection

* Added `scripts/validate_examples.py`.

  * Validates YAML examples against JSON Schemas.
  * Uses Draft 2020-12 JSON Schema validation.
  * Validates `examples/structural-tuning-record.example.yaml` against `schemas/structural-tuning-record.schema.json`.
  * Adds initial structural consistency checks beyond schema validation.
  * Checks relationships such as:

    * recovery actions must include a recovery gate,
    * passed recovery gates must allow recovery,
    * blocked or failed recovery gates must not allow recovery,
    * human review required must not be marked as `not_required`,
    * governance state human review status must match the human review section,
    * structural action allowance must not contradict human review boundary status.

### Added Dependency Definition

* Added `requirements.txt`.

  * Defines Python dependencies required for validation.
  * Includes:

    * `PyYAML>=6.0`
    * `jsonschema>=4.0`

### Added GitHub Actions Workflow

* Added `.github/workflows/validate-examples.yml`.

  * Runs validation automatically on push to `main`.
  * Runs validation automatically on pull requests to `main`.
  * Sets up Python 3.11.
  * Installs dependencies from `requirements.txt`.
  * Runs `python scripts/validate_examples.py`.

### Changed README

* Updated `README.md` to reflect the new schema, example, script, dependency, and workflow layers.
* Added or updated repository structure to include:

  * `requirements.txt`
  * `schemas/structural-tuning-record.schema.json`
  * `examples/structural-tuning-record.example.yaml`
  * `scripts/validate_examples.py`
  * `.github/workflows/validate-examples.yml`
* Added validation instructions:

  * `pip install -r requirements.txt`
  * `python scripts/validate_examples.py`
* Added GitHub Actions validation description.
* Updated project status from foundational specification toward `v0.2.0-candidate`.
* Updated roadmap to position `v0.2` as the schema, example, validation, and CI phase.

### Validated

* Confirmed that GitHub Actions validation passes.
* Confirmed that the repository now supports an initial self-checking workflow.

### Significance

This release candidate marks the transition from static documentation to executable structural validation.

In project terms:

```text
v0.1 = foundational documents and governance architecture
v0.2 = initial schema, example, validation script, dependencies, and CI workflow
```

In conceptual terms:

```text
The structure has begun to check itself.
```

---

## [0.1.0-candidate] - 2026-06-09

### Added

* Added initial `README.md` defining the basic philosophy of **Structural AI Tuning Layer**.
* Added repository description:

  * A structural tuning layer for AI governance, designed to align AI actions, recovery decisions, self-improvement loops, and human review with constitutional principles.

### Added Core Specification

* Added `docs/structural-ai-tuning-layer-v0.1.md`.

  * Defines the foundational architecture of Structural AI Tuning Layer.
  * Establishes structural tuning as distinct from model fine-tuning.
  * Defines the relationship between behavioral tuning, institutional tuning, and constitutional alignment.
  * Introduces the core components:

    * Constitution Alignment Layer
    * Semantic Drift Detection
    * Recovery Gate Verification
    * Human Review Boundary
    * Trace Consistency Model
    * Incident Lifecycle Model
    * Governance Decision Record

### Added Governance Models

* Added `docs/recovery-gate-model.md`.

  * Defines the Recovery Gate Model.
  * Establishes the principle: **No recovery without verification.**
  * Defines verification, governance approval, human review, trace consistency, incident lifecycle, and constitutional alignment conditions for recovery.
  * Provides valid and blocked recovery gate examples.

* Added `docs/constitution-alignment-model.md`.

  * Defines checkable constitutional principles.
  * Establishes the principle: **Declared principles must be checkable.**
  * Defines alignment states such as:

    * `aligned`
    * `partially_aligned`
    * `misaligned`
    * `insufficient_evidence`
    * `requires_human_review`
    * `escalated`
  * Provides examples of constitutional principle records and alignment records.

* Added `docs/semantic-drift-detection.md`.

  * Defines semantic drift as meaning-level misalignment.
  * Establishes the principle: **Same label does not guarantee same meaning.**
  * Defines drift types including:

    * State Drift
    * Recovery Drift
    * Approval Drift
    * Trace Drift
    * Scope Drift
    * Governance Drift
    * Self-Improvement Drift
    * Constitutional Drift
  * Provides semantic drift examples for recovery and self-improvement.

* Added `docs/human-review-boundary.md`.

  * Defines explicit human review requirements.
  * Establishes the principle: **Human review must be explicit.**
  * Defines review states such as:

    * `not_required`
    * `required`
    * `pending`
    * `in_review`
    * `approved`
    * `rejected`
    * `escalated`
    * `expired`
    * `invalid`
  * Defines review bypass conditions and approval authority requirements.

* Added `docs/incident-lifecycle-model.md`.

  * Defines incidents as lifecycles rather than isolated logs.
  * Establishes the principle: **An incident is a lifecycle, not a single log.**
  * Defines lifecycle phases:

    * `detected`
    * `triaged`
    * `contained`
    * `quarantined`
    * `verified`
    * `review_pending`
    * `recovery_pending`
    * `recovered`
    * `closed`
    * `escalated`
  * Provides valid, invalid, and escalated lifecycle examples.

### Added Repository Planning Sections

* Added repository structure planning.
* Added planned `schemas/`, `examples/`, and `scripts/` directories.
* Added planned schema list:

  * `structural-tuning-record.schema.json`
  * `recovery-gate.schema.json`
  * `constitution-alignment.schema.json`
  * `semantic-drift.schema.json`
  * `human-review-boundary.schema.json`
  * `incident-lifecycle.schema.json`
* Added planned example list:

  * `structural-tuning-record.example.yaml`
  * `recovery-gate.example.yaml`
  * `constitution-alignment.example.yaml`
  * `semantic-drift.example.yaml`
  * `human-review-boundary.example.yaml`
  * `incident-lifecycle.example.yaml`

### Defined

* Defined Structural AI Tuning Layer as a governance architecture for aligning:

  * AI actions
  * recovery decisions
  * human review requirements
  * trace records
  * incident lifecycles
  * self-improvement loops
  * constitutional or institutional principles

### Project Direction

* Established `v0.1` as the foundational specification phase.
* Prepared the repository for schemas, examples, validation scripts, and CI workflows.

Planned next steps at this stage were:

* Add `schemas/` for structural tuning records.
* Add `examples/` for YAML examples.
* Add validation scripts for recovery gates, constitutional alignment, semantic drift, human review boundaries, and incident lifecycles.
* Extend the architecture toward multi-protocol governance and recursive self-improvement review.

