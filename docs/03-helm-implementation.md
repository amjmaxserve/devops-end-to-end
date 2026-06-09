# Helm Implementation

## Why Helm

Helm was introduced to:

* Standardize deployments
* Reduce YAML duplication
* Support multiple environments

---

## Chart Structure

farm-stack

├── Chart.yaml
├── values.yaml
├── charts/
│ ├── farm-app/
│ └── postgres/

---

## Parameterization

Examples:

### Image

image:
repository: arjunmj/farm-stack
tag: "34"

### Resources

resources:
requests:
cpu: 100m
memory: 128Mi

---

## Conditional Rendering

### HPA

if enabled:

Create HPA

else:

Use replicaCount

---

### Monitoring

if monitoring.enabled:

Create:

* ServiceMonitor
* PrometheusRule

---

## Rendering Validation

helm template farm-stack ./k8s/helm/farm-stack

Used before every deployment.

---

## Benefits Achieved

* Environment flexibility
* Reusable templates
* Simplified maintenance
* GitOps compatibility
