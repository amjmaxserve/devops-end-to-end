# Horizontal Pod Autoscaler (HPA)

## Objective

Automatically scale workloads based on resource utilization.

---

## Configuration

Example:

minReplicas: 4

maxReplicas: 20

cpuUtilization: 70

---

## Scaling Logic

CPU > 70%

↓

Scale Up

CPU < 70%

↓

Scale Down

---

## Rollout Integration

For Argo Rollouts:

scaleTargetRef:

apiVersion: argoproj.io/v1alpha1

kind: Rollout

name: farm-inventory

---

## Testing Performed

### HPA Enabled

Verified:

* minReplicas enforcement
* automatic scaling
* Rollout integration

---

### HPA Disabled

Verified:

replicaCount controls pod count.

Examples tested:

* 2 replicas
* 4 replicas
* 7 replicas
* 9 replicas

---

## Issues Encountered

### Multiple HPA Ownership

Issue:

Stable and Canary deployments shared selectors.

Result:

AmbiguousSelector errors.

Resolution:

Separate selectors and scale targets.

---

## Outcome

Successfully validated both:

* Static replica management
* Dynamic auto-scaling
