# Incident Lifecycle Model

## Structured Incident Progression for Structural AI Tuning

---

## 0. Status

**Version:** v0.1
**Status:** Initial Specification
**Scope:** Incident phases, lifecycle states, trace relationships, recovery readiness, closure conditions, and escalation paths
**Parent Architecture:** Structural AI Tuning Layer

---

## 1. Overview

The **Incident Lifecycle Model** defines how AI governance systems should represent the progression of an incident from detection to closure.

An incident should not be treated as a single isolated record.

It should be understood as a structured lifecycle.

In AI governance, an incident may involve:

* abnormal AI behavior,
* unsafe or unauthorized action,
* failed recovery,
* semantic drift,
* governance violation,
* self-improvement failure,
* trace inconsistency,
* human review bypass,
* or constitutional misalignment.

The Incident Lifecycle Model provides a common structure for tracking how such events move through detection, triage, containment, verification, recovery, review, and closure.

---

## 2. Purpose

The purpose of the Incident Lifecycle Model is to prevent governance systems from treating complex AI events as disconnected logs.

It answers questions such as:

```text
What incident is this action part of?
What phase is the incident currently in?
Has containment occurred?
Has verification occurred?
Is recovery allowed?
Has human review been completed?
Can the incident be closed?
Were related traces properly linked?
Was escalation required?
```

This model allows AI governance systems to evaluate not only individual records, but also the institutional sequence of events.

---

## 3. Core Principle

The core principle of this model is:

```text
An incident is a lifecycle, not a single log.
```

A single trace may describe one moment.

An incident lifecycle describes the governance journey of an event.

In structural terms:

```text
detection trace
↓
triage trace
↓
containment trace
↓
verification trace
↓
human review trace
↓
recovery trace
↓
closure trace
```

The purpose of the lifecycle is to preserve institutional memory across these stages.

---

## 4. Incident Definition

In this specification, an **incident** is any event that requires structured governance attention because it may affect alignment, safety, reliability, recovery, responsibility, or institutional coherence.

An incident may be:

* technical,
* operational,
* semantic,
* constitutional,
* governance-related,
* security-related,
* or self-improvement-related.

Examples:

```text
An AI agent performs an action outside declared scope.
A recovery action is requested without verification.
A self-improving system weakens human review constraints.
A governance trace contradicts an incident status.
A system claims "recovered" while verification remains incomplete.
An autonomous defense action bypasses required human review.
```

---

## 5. Lifecycle Phases

The Incident Lifecycle Model defines the following recommended phases:

```text
detected
triaged
contained
quarantined
verified
review_pending
recovery_pending
recovered
closed
escalated
```

These phases represent institutional progression.

They are not merely technical states.

---

## 6. Phase Definitions

### 6.1 detected

An event has been identified as requiring attention.

At this phase, the system has not yet determined severity, cause, scope, or response.

Typical requirements:

* incident ID assigned,
* detection trace created,
* initial summary recorded,
* source identified if available.

---

### 6.2 triaged

The incident has been assessed for severity, scope, and governance relevance.

Typical requirements:

* risk level assigned,
* affected systems identified,
* action type classified,
* review requirement considered,
* escalation need assessed.

---

### 6.3 contained

The incident has been limited or stabilized.

Containment does not mean recovery.

It only means the immediate spread, damage, or unsafe behavior has been reduced or stopped.

Typical requirements:

* containment action recorded,
* containment trace created,
* remaining risk noted,
* verification still required.

---

### 6.4 quarantined

The affected component, workflow, agent, model output, or governance record has been isolated.

Quarantine may be required when the incident involves:

* compromised state,
* unsafe self-modification,
* suspicious agent behavior,
* unverified recovery,
* trace inconsistency,
* or possible semantic drift.

Typical requirements:

* quarantine reason recorded,
* affected scope identified,
* release conditions defined.

---

### 6.5 verified

The incident has been investigated and verification evidence exists.

Verification should confirm the actual state of the incident, not merely the disappearance of visible symptoms.

Typical requirements:

* verification trace exists,
* verification result recorded,
* related traces reviewed,
* recovery readiness evaluated.

---

### 6.6 review_pending

Human review or higher-level governance review is required before further action.

Typical requirements:

* review requirement recorded,
* reviewer role identified,
* review status pending or in progress,
* action blocked until review completes if mandatory.

---

### 6.7 recovery_pending

Recovery is being considered or requested, but has not yet been finalized.

At this phase, the Recovery Gate Model should be applied.

Typical requirements:

* verification completed,
* governance approval assessed,
* human review boundary checked,
* trace consistency checked,
* recovery gate evaluated.

---

### 6.8 recovered

The incident has passed recovery requirements and the system has been restored to an acceptable state.

Recovery must not be claimed unless required conditions are satisfied.

Typical requirements:

* recovery gate passed,
* recovery trace exists,
* verification status supports recovery,
* required review completed or explicitly not required,
* constitutional alignment satisfied.

---

### 6.9 closed

The incident has been formally closed.

Closure is an institutional state, not merely the end of visible activity.

Typical requirements:

* recovery completed or incident otherwise resolved,
* closure trace created,
* required human review completed,
* unresolved contradictions addressed,
* final governance status recorded.

---

### 6.10 escalated

The incident requires higher-level review, authority, or governance intervention.

Escalation may occur at any phase.

Typical triggers:

* critical risk,
* unresolved constitutional misalignment,
* review bypass,
* self-improvement drift,
* trace contradiction,
* failed recovery,
* repeated incident recurrence.

---

## 7. Recommended Phase Flow

A standard lifecycle may follow this path:

```text
detected
↓
triaged
↓
contained
↓
verified
↓
review_pending
↓
recovery_pending
↓
recovered
↓
closed
```

A security-sensitive path may include quarantine:

```text
detected
↓
triaged
↓
contained
↓
quarantined
↓
verified
↓
review_pending
↓
recovery_pending
↓
recovered
↓
closed
```

An unresolved or high-risk path may escalate:

```text
detected
↓
triaged
↓
contained
↓
escalated
```

or:

```text
recovery_pending
↓
escalated
```

---

## 8. Invalid or Suspicious Phase Transitions

Certain transitions should be flagged as structurally suspicious.

Examples:

```text
detected → recovered
triaged → closed
contained → recovered without verification
verified → closed without recovery or review
recovery_pending → closed while recovery gate is blocked
review_pending → recovered without human approval
```

These transitions may indicate:

* premature recovery,
* missing verification,
* bypassed human review,
* semantic drift,
* trace inconsistency,
* or governance shortcutting.

---

## 9. Lifecycle Status Values

In addition to `phase`, an incident may have a broader `status`.

Recommended values:

```text
open
active
contained
quarantined
verified
pending_review
pending_recovery
recovered
closed
blocked
escalated
failed
```

The `phase` describes where the incident is in the lifecycle.

The `status` describes the current governance condition.

Example:

```yaml
incident_lifecycle:
  incident_id: inc-2026-0001
  phase: recovery_pending
  status: pending_recovery
```

---

## 10. Incident Lifecycle Record

A minimal incident lifecycle record may include:

```yaml
incident_lifecycle:
  incident_id: inc-2026-0001
  phase: containment
  status: contained
  parent_trace_id: trace-2026-0001
  related_trace_ids:
    - trace-2026-0002
    - trace-2026-0003
```

Recommended fields:

```text
incident_id
phase
status
severity
created_at
updated_at
parent_trace_id
related_trace_ids
current_owner
review_required
recovery_allowed
closure_allowed
escalation_required
```

---

## 11. Trace Relationships

An incident lifecycle depends on trace relationships.

Trace records preserve institutional memory.

Recommended trace relationships:

```text
parent_trace_id
related_trace_ids
detection_trace_id
triage_trace_id
containment_trace_id
verification_trace_id
human_review_trace_id
recovery_trace_id
closure_trace_id
```

A lifecycle record should not simply claim that an event moved forward.

It should point to the traces that justify the transition.

Example:

```yaml
incident_lifecycle:
  incident_id: inc-2026-0002
  phase: recovered
  status: recovered
  detection_trace_id: trace-2026-0101
  containment_trace_id: trace-2026-0102
  verification_trace_id: trace-2026-0103
  human_review_trace_id: trace-2026-0104
  recovery_trace_id: trace-2026-0105
```

---

## 12. Phase Transition Checks

A structural tuning layer should evaluate whether a phase transition is allowed.

Minimal transition check:

```text
IF next_phase = recovered
    REQUIRE verification_status IN [verified, recovery_approved]
    REQUIRE recovery_gate_status = passed
    REQUIRE trace_consistency_status = consistent
    REQUIRE human review satisfied if required

IF next_phase = closed
    REQUIRE incident status IN [recovered, resolved, escalated]
    REQUIRE closure trace exists
    REQUIRE unresolved contradictions = false

IF next_phase = recovery_pending
    REQUIRE incident phase IN [verified, review_pending]
    REQUIRE recovery request exists

IF next_phase = escalated
    REQUIRE escalation reason exists
```

This logic is not final implementation.

It defines the minimum structural intent.

---

## 13. Relationship to Recovery Gate Model

The Recovery Gate Model depends on the Incident Lifecycle Model.

Recovery should not proceed unless the incident lifecycle supports recovery.

Example valid recovery condition:

```yaml
incident_lifecycle:
  phase: recovery_pending
  status: verified

recovery_gate_result:
  recovery_gate_status: passed
  recovery_allowed: true
```

Example invalid recovery condition:

```yaml
incident_lifecycle:
  phase: detected
  status: open

recovery_gate_result:
  recovery_gate_status: blocked
  recovery_allowed: false
```

The recovery gate should block premature recovery when the lifecycle has not reached a recoverable phase.

---

## 14. Relationship to Constitution Alignment Model

The Constitution Alignment Model checks whether lifecycle transitions violate declared principles.

Examples of applicable principles:

```text
No recovery without verification.
No closure without trace consistency.
No bypassing required human review.
No escalation without recorded reason.
No self-improvement recovery without review.
```

If a lifecycle transition violates these principles, the incident should be marked:

```text
misaligned
requires_human_review
escalated
blocked
```

depending on severity.

---

## 15. Relationship to Semantic Drift Detection

Incident lifecycle states are vulnerable to semantic drift.

Examples:

```text
contained does not mean resolved.
verified does not mean recovered.
recovered does not mean closed.
closed does not mean forgotten.
escalated does not mean solved.
```

Semantic Drift Detection should compare lifecycle labels with their required conditions.

Example drift:

```yaml
incident_lifecycle:
  phase: closed
  status: closed

human_review:
  human_review_required: true
  human_review_status: pending
```

This is lifecycle semantic drift.

The incident claims closure, but required review remains incomplete.

---

## 16. Relationship to Human Review Boundary

The Human Review Boundary determines when lifecycle progression must pause for human review.

Common review points:

```text
triaged → contained
verified → recovery_pending
review_pending → recovery_pending
recovery_pending → recovered
recovered → closed
```

For high-risk incidents, review may be required before recovery or closure.

Example:

```yaml
incident_lifecycle:
  phase: review_pending
  status: pending_review

human_review:
  human_review_required: true
  human_review_status: pending
```

The lifecycle should not advance to `recovered` until review is completed.

---

## 17. Relationship to Recursive Self-Improvement

Self-improvement events may also be treated as incidents when they affect governance, scope, safety, or institutional alignment.

Examples:

```text
An AI agent modifies its recovery logic.
A self-improvement loop removes a review requirement.
An AI-generated patch expands action scope.
A model update improves performance but weakens traceability.
```

Such events should be tracked through a lifecycle.

Example:

```text
detected
↓
triaged
↓
quarantined
↓
verified
↓
review_pending
↓
recovery_pending
↓
recovered
↓
closed
```

In this context, recovery may involve rollback, constraint restoration, or governance patch approval.

---

## 18. Example: Valid Incident Lifecycle Record

```yaml
record_type: incident_lifecycle_record
version: "0.1"

incident_lifecycle:
  incident_id: inc-2026-0001
  phase: recovery_pending
  status: pending_recovery
  severity: medium
  created_at: "2026-06-09T10:00:00Z"
  updated_at: "2026-06-09T11:30:00Z"

trace_links:
  detection_trace_id: trace-2026-0001
  triage_trace_id: trace-2026-0002
  containment_trace_id: trace-2026-0003
  verification_trace_id: trace-2026-0004
  human_review_trace_id: trace-2026-0005
  related_trace_ids:
    - trace-2026-0001
    - trace-2026-0002
    - trace-2026-0003
    - trace-2026-0004
    - trace-2026-0005

governance_state:
  verification_status: recovery_approved
  human_review_status: approved
  trace_consistency_status: consistent
  constitutional_alignment_status: aligned

lifecycle_evaluation:
  transition_allowed: true
  next_allowed_phases:
    - recovered
    - escalated
  reason: "The incident is verified, review is approved, and recovery may proceed through the recovery gate."
```

---

## 19. Example: Invalid Lifecycle Transition

```yaml
record_type: incident_lifecycle_record
version: "0.1"

incident_lifecycle:
  incident_id: inc-2026-0002
  phase: recovered
  status: recovered
  severity: high
  created_at: "2026-06-09T10:00:00Z"
  updated_at: "2026-06-09T10:15:00Z"

trace_links:
  detection_trace_id: trace-2026-0101
  triage_trace_id: null
  containment_trace_id: null
  verification_trace_id: null
  human_review_trace_id: null
  recovery_trace_id: trace-2026-0102
  related_trace_ids:
    - trace-2026-0101
    - trace-2026-0102

governance_state:
  verification_status: not_started
  human_review_status: pending
  trace_consistency_status: incomplete
  constitutional_alignment_status: misaligned

lifecycle_evaluation:
  transition_allowed: false
  violation_codes:
    - premature_recovery
    - recovery_without_verification
    - human_review_required_but_not_completed
    - missing_required_traces
  reason: "The incident was marked recovered before triage, containment, verification, and human review were completed."
```

---

## 20. Example: Escalated Lifecycle

```yaml
record_type: incident_lifecycle_record
version: "0.1"

incident_lifecycle:
  incident_id: inc-2026-0003
  phase: escalated
  status: escalated
  severity: critical
  created_at: "2026-06-09T10:00:00Z"
  updated_at: "2026-06-09T10:45:00Z"

trace_links:
  detection_trace_id: trace-2026-0201
  triage_trace_id: trace-2026-0202
  containment_trace_id: trace-2026-0203
  related_trace_ids:
    - trace-2026-0201
    - trace-2026-0202
    - trace-2026-0203

escalation:
  escalation_required: true
  escalation_reason: "Constitutional misalignment detected in autonomous recovery logic."
  required_reviewer_role: constitutional_reviewer

governance_state:
  verification_status: in_progress
  human_review_status: escalated
  semantic_drift_status: drift_detected
  constitutional_alignment_status: misaligned

lifecycle_evaluation:
  transition_allowed: false
  next_allowed_phases:
    - verified
    - review_pending
    - closed
  reason: "The incident requires higher-level constitutional review before recovery can be considered."
```

---

## 21. Lifecycle Evaluation Status Values

Recommended values:

```text
valid
invalid
pending
blocked
escalated
inconsistent
insufficient_evidence
```

### 21.1 valid

The current phase and related governance conditions are coherent.

### 21.2 invalid

The lifecycle contains an invalid transition or contradiction.

### 21.3 pending

The incident is waiting for required action, review, verification, or trace completion.

### 21.4 blocked

The incident cannot proceed due to failed conditions.

### 21.5 escalated

The incident requires higher-level review.

### 21.6 inconsistent

The lifecycle state contradicts related records.

### 21.7 insufficient_evidence

There is not enough information to evaluate the lifecycle.

---

## 22. Violation Codes

Recommended violation codes:

```text
premature_recovery
recovery_without_verification
closure_without_recovery
closure_without_trace_consistency
human_review_required_but_not_completed
missing_required_traces
invalid_phase_transition
phase_status_mismatch
incident_trace_contradiction
semantic_drift_detected
unauthorized_escalation
self_improvement_without_review
```

These codes may be used by future schemas and validation scripts.

---

## 23. Required Fields for Future Schema

A future `incident-lifecycle.schema.json` should likely include:

```text
record_type
version
incident_lifecycle
trace_links
governance_state
lifecycle_evaluation
```

Minimum recommended fields:

```yaml
record_type: incident_lifecycle_record
version: "0.1"

incident_lifecycle:
  incident_id: string
  phase: string
  status: string
  severity: string
  created_at: string
  updated_at: string

trace_links:
  detection_trace_id: string | null
  triage_trace_id: string | null
  containment_trace_id: string | null
  verification_trace_id: string | null
  human_review_trace_id: string | null
  recovery_trace_id: string | null
  closure_trace_id: string | null
  related_trace_ids: array

governance_state:
  verification_status: string
  human_review_status: string
  trace_consistency_status: string
  constitutional_alignment_status: string

lifecycle_evaluation:
  transition_allowed: boolean
  lifecycle_evaluation_status: string
  violation_codes: array
  reason: string
```

---

## 24. Design Principles

### 24.1 Incidents Are Lifecycles

An incident is not a single log entry.

It is a sequence of governance states.

### 24.2 Containment Is Not Recovery

A contained incident is not automatically recovered.

### 24.3 Verification Comes Before Recovery

Recovery should not proceed before verification.

### 24.4 Closure Requires Institutional Completion

An incident should not be closed while required review, recovery, trace consistency, or alignment checks remain incomplete.

### 24.5 Trace Links Preserve Memory

Lifecycle transitions should be supported by trace records.

### 24.6 Escalation Is a Valid State

Escalation is not failure.

It is a governance response to unresolved risk.

### 24.7 Lifecycle Labels Must Preserve Meaning

State labels such as `contained`, `verified`, `recovered`, and `closed` must remain structurally meaningful.

---

## 25. Minimal Definition

```text
The Incident Lifecycle Model is a structural governance model for representing
incidents as phased institutional processes rather than isolated logs, allowing
AI governance systems to evaluate detection, triage, containment, verification,
human review, recovery, escalation, and closure as coherent sequences.
```

---

## 26. Closing Statement

An incident does not end because a system says it is over.

An incident ends when its lifecycle has been structurally completed.

Detection must be remembered.

Containment must be distinguished from recovery.

Recovery must be verified.

Closure must be justified.

The Incident Lifecycle Model exists to preserve that sequence.

```text
An incident is a lifecycle, not a single log.
Trace preserves the path.
Governance completes the journey.
```
