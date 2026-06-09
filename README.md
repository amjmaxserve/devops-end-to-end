# Farm Inventory Platform

## Project Overview

Farm Inventory is a cloud-native inventory management application built to demonstrate production-grade DevOps practices using Kubernetes, Helm, ArgoCD, Argo Rollouts, Prometheus, PostgreSQL, and GitOps workflows.

The project evolved from a simple FastAPI application into a complete Kubernetes platform supporting multiple deployment strategies, autoscaling, monitoring, security controls, and GitOps-based delivery.

---

# Project Goals

The primary goals of this project were:

* Build a containerized application
* Deploy to Kubernetes
* Manage infrastructure using Helm
* Implement GitOps using ArgoCD
* Implement multiple deployment strategies
* Implement Horizontal Pod Autoscaling (HPA)
* Implement monitoring and observability
* Demonstrate progressive delivery techniques
* Simulate production-grade deployment workflows

---

# Technology Stack

## Application Layer

* FastAPI
* Python 3.12

## Database Layer

* PostgreSQL

## Containerization

* Docker

## Kubernetes Platform

* Kubernetes
* Helm

## GitOps

* ArgoCD

## Progressive Delivery

* Argo Rollouts

## Monitoring

* Prometheus
* ServiceMonitor
* PrometheusRule

## Networking

* Traefik Ingress

## Security

* Kubernetes RBAC
* Service Accounts
* Secrets

---

# Architecture

Git Repository
↓
GitHub Actions (Planned)
↓
ArgoCD
↓
Helm Charts
↓
Kubernetes
↓
Application Pods
↓
PostgreSQL

Monitoring Stack

Prometheus
↓
ServiceMonitor
↓
Application Metrics

---

# Project Milestones

---

## Milestone 1: Application Development

### Achievements

* Created FastAPI inventory application
* Added REST APIs
* Connected application to PostgreSQL
* Implemented health endpoint

### Deliverables

* FastAPI backend
* PostgreSQL integration
* Health checks

---

## Milestone 2: Dockerization

### Achievements

* Created Dockerfile
* Built container image
* Published images to Docker Hub

### Deliverables

Docker Image:

arjunmj/farm-stack

---

## Milestone 3: Kubernetes Deployment

### Achievements

* Created Kubernetes manifests
* Deployed application pods
* Deployed PostgreSQL
* Configured services

### Deliverables

* Deployment
* Service
* ConfigMap
* Secret

---

## Milestone 4: Helm Migration

### Achievements

* Converted manifests into Helm Charts
* Parameterized configurations
* Added environment-based values

### Deliverables

Helm Chart Structure

farm-stack
├── farm-app
└── postgres

---

## Milestone 5: Security Implementation

### Achievements

* Created Service Accounts
* Implemented RBAC
* Added Secrets Management

### Deliverables

* Role
* RoleBinding
* ServiceAccount
* Secret

---

## Milestone 6: Health Probes

### Achievements

Implemented:

* Startup Probe
* Readiness Probe
* Liveness Probe

### Benefits

* Faster recovery
* Better pod lifecycle management
* Improved application availability

---

## Milestone 7: Monitoring Integration

### Achievements

Integrated Prometheus monitoring

### Deliverables

* ServiceMonitor
* PrometheusRule
* PostgreSQL Alerts
* Application Alerts

### Monitoring Coverage

* Application availability
* Database status
* Resource consumption

---

## Milestone 8: Horizontal Pod Autoscaling (HPA)

### Achievements

Implemented CPU-based autoscaling.

### Features

* Dynamic scaling
* Scale up policies
* Scale down policies
* Stabilization windows

### Validation

Successfully tested scaling configurations.

---

## Milestone 9: Pod Disruption Budget

### Achievements

Configured Pod Disruption Budget.

### Benefits

* High Availability
* Safe node maintenance
* Controlled pod eviction

---

## Milestone 10: Ingress Implementation

### Achievements

Integrated Traefik Ingress.

### Deliverables

* Host-based routing
* External application access

---

# Deployment Strategy Implementations

---

## Strategy 1: Standard Deployment

### Branch

main

### Features

* Kubernetes Deployment
* HPA Integration
* Rolling Updates

### Status

Validated Successfully

---

## Strategy 2: Manual Canary Deployment

### Branch

farmapp-canary

### Architecture

Stable Deployment
+
Canary Deployment

### Features

* Stable Pods
* Canary Pods
* Independent HPA
* Traffic Distribution

### Validation

Successfully tested:

* Stable Version (34)
* Canary Version (35)

Traffic distribution verified through API responses.

### Example

Version 34 → Stable

Version 35 → Canary

---

## Strategy 3: Blue-Green Deployment

### Branch

farmapp-bluegreen

### Architecture

Blue Environment
+
Green Environment

### Features

* Zero Downtime Switching
* Parallel Environments
* Safe Rollbacks

### Validation

Successfully synchronized using ArgoCD.

---

## Strategy 4: Argo Rollouts Canary

### Branch

farmapp-rollouts

### Architecture

Argo Rollout
↓
ReplicaSet
↓
Pods

### Features

* Progressive Delivery
* Traffic Weight Control
* Automated Rollout Steps
* HPA Integration

### Rollout Steps

20%
↓
Pause

50%
↓
Pause

100%
↓
Promotion

### Validation

Successfully tested:

* Replica management
* Rollout progression
* HPA integration
* Automated ReplicaSet management

---

# GitOps Implementation

## ArgoCD Applications

### Branch Isolation

Each deployment strategy is maintained in its own branch.

main
farmapp-canary
farmapp-bluegreen
farmapp-rollouts

### Validation

Successfully verified:

* Independent synchronization
* No cross-branch interference
* Automatic reconciliation
* Drift detection

---

# Key Challenges Solved

## Helm Ownership Conflicts

Resolved Helm ownership metadata issues.

## Immutable Deployment Selectors

Resolved deployment selector conflicts during strategy migration.

## HPA Selector Conflicts

Resolved ambiguous selector issues when multiple deployments existed.

## Rollout Migration

Successfully migrated from Deployment resources to Argo Rollouts.

## Replica Management

Implemented conditional logic:

* HPA Enabled
* HPA Disabled

with proper replica handling.

---

# Current Status

Completed:

* Docker
* Kubernetes
* Helm
* PostgreSQL
* RBAC
* Secrets
* ConfigMaps
* Probes
* HPA
* PDB
* Prometheus
* ServiceMonitor
* Traefik
* ArgoCD
* Manual Canary
* Blue-Green
* Argo Rollouts Canary

Project State:

Production-Ready Demonstration Platform

---

# Future Enhancements

## CI/CD Pipeline

GitHub Actions

* Linting
* Testing
* Build
* Push Images
* Helm Validation

## Security

* Trivy Scanning
* Secret Scanning
* Image Vulnerability Scanning

## Advanced Rollouts

* Analysis Templates
* Automatic Rollbacks
* Prometheus-based Decisions

## Multi-Environment Promotion

Development
↓
QA
↓
Staging
↓
Production

---

# Author

Arjun M J

DevOps Engineer | Cloud Architect | Cyber Forensics Analyst

AWS Solution Architect Associate
AWS Security Specialty
RCCE Certified
