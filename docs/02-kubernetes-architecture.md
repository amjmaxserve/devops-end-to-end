# Kubernetes Architecture

## Namespace Design

Namespace:

farm-stack

Contains:

* Application Pods
* PostgreSQL
* Services
* Ingress
* Monitoring Resources

---

## Core Resources

### Deployment / Rollout

Responsible for:

* Pod creation
* Updates
* Replica management

---

### Services

#### farm-inventory-service

Exposes application traffic.

#### postgres-service

Internal database communication.

---

### ConfigMap

Stores:

* Application Name
* Environment
* Database Host

---

### Secret

Stores:

* Database Username
* Database Password

---

### Persistent Volume Claim

Used by PostgreSQL for persistent storage.

---

## Networking Flow

Client
↓
Traefik Ingress
↓
farm-inventory-service
↓
Pods

---

## Pod Lifecycle

Container Startup

↓

Startup Probe

↓

Readiness Probe

↓

Receive Traffic

↓

Liveness Probe

↓

Restart if Unhealthy
