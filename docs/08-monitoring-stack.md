# Monitoring and Alerting Stack

## Objective

Provide observability for application and database components.

---

## Components

### Prometheus

Metrics collection.

### ServiceMonitor

Prometheus Operator integration.

### PrometheusRule

Alert definitions.

### PostgreSQL Exporter

Database metrics collection.

---

## Application Monitoring

Farm Inventory exposes:

/metrics

Prometheus scrapes metrics periodically.

---

## Database Monitoring

Metrics collected:

* PostgreSQL availability
* Connections
* Deadlocks
* Query statistics

---

## Alerts Implemented

### Application Down

Triggered when application becomes unavailable.

---

### PostgreSQL Down

Triggered when database exporter reports failure.

---

### High Connections

Triggered when active database connections exceed threshold.

---

### Deadlock Detection

Triggered when PostgreSQL deadlocks occur.

---

## Validation

Verified:

* Metrics collection
* ServiceMonitor discovery
* Alert rule loading
* PostgreSQL exporter communication

---

## Benefits

* Faster troubleshooting
* Production visibility
* Capacity planning
* Proactive alerting
