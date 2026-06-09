# Examples

This directory will contain YAML examples for the **Structural AI Tuning Layer**.

The examples demonstrate how governance concepts such as recovery gates, constitutional alignment, semantic drift detection, human review boundaries, and incident lifecycles can be represented as structured records.

---

## Purpose

The purpose of this directory is to provide concrete examples that correspond to the specifications in `docs/` and the schemas in `schemas/`.

```text
docs/     = conceptual and governance specifications
schemas/  = machine-readable validation structures
examples/ = concrete YAML records
```

Examples help show how abstract governance concepts can be expressed as practical, reviewable, and eventually validateable data.

---

## Planned Examples

Future versions may include the following examples.

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

## Example Roles

### `structural-tuning-record.example.yaml`

Demonstrates a general structural tuning record.

This example may combine:

* AI action metadata
* governance status
* constitutional alignment status
* semantic drift evaluation
* recovery gate result
* human review boundary result
* incident lifecycle reference

---

### `recovery-gate.example.yaml`

Demonstrates a recovery gate record.

This example should show how a recovery action is evaluated against the principle:

```text
No recovery without verification.
```

It may include:

* recovery action metadata
* verification status
* governance approval
* human review status
* trace consistency
* constitutional alignment
* recovery gate result

---

### `constitution-alignment.example.yaml`

Demonstrates a constitution alignment record.

This example should show how AI actions or governance decisions are checked against declared principles.

Core principle:

```text
Declared principles must be checkable.
```

It may include:

* applicable principles
* satisfaction status
* violations
* unresolved conditions
* semantic drift status
* alignment evaluation result

---

### `semantic-drift.example.yaml`

Demonstrates a semantic drift detection record.

This example should show how a claimed state is compared against its required institutional meaning.

Core principle:

```text
Same label does not guarantee same meaning.
```

It may include:

* claimed state
* expected meaning
* observed structure
* drift codes
* drift severity
* drift evaluation result

---

### `human-review-boundary.example.yaml`

Demonstrates a human review boundary record.

This example should show whether human review is required, completed, rejected, escalated, or explicitly not required.

Core principle:

```text
Human review must be explicit.
```

It may include:

* review requirement level
* human review status
* reviewer role
* review trace ID
* review boundary result
* action allowed status

---

### `incident-lifecycle.example.yaml`

Demonstrates an incident lifecycle record.

This example should show how an incident progresses through structured phases.

Core principle:

```text
An incident is a lifecycle, not a single log.
```

It may include:

* incident ID
* lifecycle phase
* lifecycle status
* trace links
* governance state
* transition evaluation
* violation codes if applicable

---

## Valid and Invalid Examples

Future versions may include both valid and invalid examples.

Example naming convention:

```text
recovery-gate.valid.example.yaml
recovery-gate.blocked.example.yaml
constitution-alignment.aligned.example.yaml
constitution-alignment.misaligned.example.yaml
semantic-drift.detected.example.yaml
human-review-boundary.pending.example.yaml
incident-lifecycle.invalid-transition.example.yaml
```

Valid examples show how governance records should pass structural checks.

Invalid examples show how the system should detect misalignment, missing review, premature recovery, semantic drift, or lifecycle inconsistency.

Both are useful.

A governance system must understand not only what good records look like, but also what failure looks like.

---

## Planned Relationship to Schemas

Each example should eventually correspond to a JSON Schema in `schemas/`.

Example relationship:

```text
schemas/recovery-gate.schema.json
↓ validates
examples/recovery-gate.example.yaml
```

Planned schema-example pairs:

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

## Planned Relationship to Validation Scripts

Future validation scripts may check examples against schemas.

Possible command:

```bash
python scripts/validate_examples.py
```

A future validation flow may look like this:

```text
YAML example
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
```

---

## Example Design Principles

Examples in this directory should follow these principles.

### 1. Be Concrete

Examples should use realistic field names, IDs, statuses, and governance states.

### 2. Be Minimal but Meaningful

Examples should be simple enough to understand, but complete enough to show the intended structure.

### 3. Preserve Governance Meaning

A valid example should not merely be syntactically correct.

It should also preserve the governance meaning defined in `docs/`.

### 4. Include Trace References

Where relevant, examples should include trace IDs or related record references.

### 5. Make Human Review Explicit

Human review should never be implied.

If it is not required, that should be recorded explicitly.

### 6. Show Failure Cases

Invalid examples are important.

They help define what the system should reject or escalate.

### 7. Align With Schemas

Examples should remain consistent with the JSON Schemas once schemas are introduced.

---

## Current Status

This directory is currently reserved for future YAML examples.

The first planned example is:

```text
examples/structural-tuning-record.example.yaml
```

This will serve as the general example format for the Structural AI Tuning Layer.

---

## Closing Statement

Examples turn governance structures into visible records.

They show how principles become data.

They show how alignment can be checked.

```text
Documents define meaning.
Schemas define structure.
Examples show the structure in motion.
```
