# Schemas

This directory will contain JSON Schemas for the **Structural AI Tuning Layer**.

The schemas define machine-readable structures for governance records, recovery gates, constitutional alignment checks, semantic drift detection, human review boundaries, and incident lifecycle records.

---

## Purpose

The purpose of this directory is to provide formal validation structures for the concepts defined in the `docs/` directory.

The documents in `docs/` define the philosophy and governance models.

The schemas in this directory will define how those models can be represented, validated, and checked as structured data.

```text
docs/    = conceptual and governance specifications
schemas/ = machine-readable validation structures
```

---

## Planned Schemas

Future versions may include the following schemas.

```text
schemas/
├─ structural-tuning-record.schema.json
├─ recovery-gate.schema.json
├─ constitution-alignment.schema.json
├─ semantic-drift.schema.json
├─ human-review-boundary.schema.json
└─ incident-lifecycle.schema.json
```

---

## Schema Roles

### `structural-tuning-record.schema.json`

Defines the general structural tuning record.

This schema may combine:

* AI action metadata
* governance state
* constitutional alignment
* semantic drift status
* recovery gate status
* human review status
* incident lifecycle references

---

### `recovery-gate.schema.json`

Defines records for recovery gate evaluation.

Based on the principle:

```text
No recovery without verification.
```

This schema will validate whether a recovery action includes required verification, governance approval, human review, trace consistency, and constitutional alignment fields.

---

### `constitution-alignment.schema.json`

Defines records for checking AI actions against declared constitutional or institutional principles.

Based on the principle:

```text
Declared principles must be checkable.
```

This schema will validate applicable principles, satisfaction states, violations, unresolved conditions, and alignment status.

---

### `semantic-drift.schema.json`

Defines records for detecting meaning-level misalignment.

Based on the principle:

```text
Same label does not guarantee same meaning.
```

This schema will validate claimed states, expected meanings, observed structures, drift codes, severity, and drift evaluation results.

---

### `human-review-boundary.schema.json`

Defines records for explicit human review requirements.

Based on the principle:

```text
Human review must be explicit.
```

This schema will validate review requirement levels, review status, reviewer roles, review traces, and review boundary results.

---

### `incident-lifecycle.schema.json`

Defines records for incident lifecycle evaluation.

Based on the principle:

```text
An incident is a lifecycle, not a single log.
```

This schema will validate incident phases, statuses, trace links, governance state, lifecycle evaluation results, and invalid transition codes.

---

## Design Principles

The schemas in this directory should follow these principles.

### 1. Specification First

Schemas should reflect the governance models defined in `docs/`.

A schema should not introduce concepts that are not documented.

### 2. Checkable Principles

Constitutional and institutional principles should be represented in a form that can be validated.

### 3. Explicit Status Fields

Important governance states should be explicit.

Missing data should not be treated as approval, completion, or alignment.

### 4. Traceability

Records should include identifiers and references that allow related actions, reviews, incidents, and decisions to be linked.

### 5. Human Review Visibility

Human review requirements and outcomes should be visible in structured data.

### 6. Recovery Safety

Recovery-related records should prevent unverified or premature recovery.

### 7. Drift Detection

Schemas should support detecting when labels such as `approved`, `verified`, `recovered`, or `closed` no longer match their required institutional meaning.

---

## Planned Validation Flow

A future validation flow may look like this:

```text
YAML examples
↓
JSON Schema validation
↓
structural consistency checks
↓
constitutional alignment checks
↓
semantic drift checks
↓
recovery gate checks
↓
human review boundary checks
↓
incident lifecycle checks
```

---

## Planned Relationship to Examples

The `examples/` directory will contain YAML files that correspond to these schemas.

Example relationship:

```text
schemas/recovery-gate.schema.json
↓ validates
examples/recovery-gate.example.yaml
```

Planned examples:

```text
examples/
├─ structural-tuning-record.example.yaml
├─ recovery-gate.example.yaml
├─ constitution-alignment.example.yaml
├─ semantic-drift.example.yaml
├─ human-review-boundary.example.yaml
└─ incident-lifecycle.example.yaml
```

---

## Planned Relationship to Scripts

The `scripts/` directory will eventually contain validation scripts.

Possible script:

```text
scripts/validate_examples.py
```

This script may validate YAML examples against the JSON Schemas in this directory.

---

## Current Status

This directory is currently reserved for future schema definitions.

The first planned schema is:

```text
schemas/structural-tuning-record.schema.json
```

This will serve as the general record format for the Structural AI Tuning Layer.

---

## Closing Statement

Schemas turn governance concepts into checkable structures.

They do not replace judgment.

They make judgment easier to review.

```text
Documents define meaning.
Schemas define structure.
Validation checks alignment.
```
