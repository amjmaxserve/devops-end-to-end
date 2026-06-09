# Argo Rollouts Progressive Delivery

## Objective

Replace native Kubernetes Deployment with Argo Rollout for advanced deployment strategies.

---

## Installation

Namespace:

argo-rollouts

Controller:

argo-rollouts-controller

Verification:

kubectl get pods -n argo-rollouts

---

## Rollout Resource

Replaced:

kind: Deployment

With:

kind: Rollout

---

## Canary Rollout Strategy

Example Flow

20% Traffic
↓

Pause

↓

50% Traffic
↓

Pause

↓

100% Traffic

---

## Challenges Encountered

### Deployment Ownership Conflict

Issue:

Deployment and Rollout managed same application.

Resolution:

Removed Deployment resource from Helm.

---

### Invalid Rollout Strategy

Issue:

Used Deployment-style strategy fields.

Resolution:

Converted to Argo Rollouts Canary syntax.

---

### HPA Integration

Issue:

HPA initially targeted Deployment.

Resolution:

Updated scaleTargetRef to:

kind: Rollout

---

## Validation

Verified:

* ReplicaSet creation
* Canary progression
* Stable ReplicaSet promotion
* Rollback capability
* ArgoCD synchronization

---

## Commands Used

kubectl argo rollouts get rollout farm-inventory -n farm-stack

kubectl argo rollouts promote farm-inventory -n farm-stack

kubectl argo rollouts undo farm-inventory -n farm-stack

---

## Outcome

Successfully migrated from Deployment to Argo Rollout while maintaining GitOps workflow through ArgoCD.
