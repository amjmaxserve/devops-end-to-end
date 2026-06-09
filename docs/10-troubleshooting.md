# Troubleshooting Guide

## Helm Rendering Errors

### Nil Pointer Errors

Example:

nil pointer evaluating interface

Cause:

Incorrect values.yaml hierarchy.

Resolution:

Verify template path matches values structure.

---

## ArgoCD Sync Failure

### Immutable Selector Error

Example:

spec.selector field is immutable

Cause:

Deployment selector changed after creation.

Resolution:

Delete resource and recreate.

---

## HPA Ambiguous Selector

Example:

AmbiguousSelector

Cause:

Multiple workloads controlled same labels.

Resolution:

Use unique selectors.

---

## Rollout Not Progressing

Example:

updated replicas are still becoming available

Cause:

Application pods failing startup.

Resolution:

Check:

kubectl logs

kubectl describe pod

---

## CrashLoopBackOff

Common Causes:

* Missing environment variables
* Database unavailable
* Invalid image
* Probe failures

---

## Rollout Validation Commands

kubectl get rollout -n farm-stack

kubectl argo rollouts get rollout farm-inventory -n farm-stack

kubectl get rs -n farm-stack

kubectl get pods -n farm-stack

---

## Lessons Learned

Always validate:

1. helm template
2. kubectl apply
3. pod health
4. rollout status
5. ArgoCD sync status

before moving to production.
