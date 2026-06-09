# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple versioning structure during the early specification phase.

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
  * Defines alignment states such as `aligned`, `partially_aligned`, `misaligned`, `insufficient_evidence`, `requires_human_review`, and `escalated`.
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
  * Defines review states such as `not_required`, `required`, `pending`, `in_review`, `approved`, `rejected`, `escalated`, `expired`, and `invalid`.
  * Defines review bypass conditions and approval authority requirements.

* Added `docs/incident-lifecycle-model.md`.

  * Defines incidents as lifecycles rather than isolated logs.
  * Establishes the principle: **An incident is a lifecycle, not a single log.**
  * Defines lifecycle phases:

    * detected
    * triaged
    * contained
    * quarantined
    * verified
    * review_pending
    * recovery_pending
    * recovered
    * closed
    * escalated
  * Provides valid, invalid, and escalated lifecycle examples.

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
* Prepared the repository for future schemas, examples, and validation scripts.

Planned next steps:

* Add `schemas/` for structural tuning records.
* Add `examples/` for YAML examples.
* Add validation scripts for recovery gates, constitutional alignment, semantic drift, human review boundaries, and incident lifecycles.
* Extend the architecture toward multi-protocol governance and recursive self-improvement review.
