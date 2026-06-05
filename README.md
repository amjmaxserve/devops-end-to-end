# Farm Inventory System

## Overview

Farm Inventory System is a production-style FastAPI application deployed on Kubernetes (K3s) with PostgreSQL, CI/CD automation, autoscaling, RBAC, and security best practices.

This project was built to demonstrate real-world DevOps, Cloud, and Kubernetes concepts including Infrastructure as Code, Continuous Integration, Continuous Deployment, Containerization, Monitoring Readiness, Scalability, and Security.

---

## Technology Stack

### Application

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn

### Containerization

* Docker
* Docker Hub

### CI/CD

* GitHub Actions
* Self Hosted Runner
* Trivy Security Scanner

### Kubernetes

* K3s
* Traefik Ingress Controller
* Metrics Server
* Horizontal Pod Autoscaler
* Pod Disruption Budget
* RBAC

---

## Features

### Inventory Management

* Create Inventory Item
* List Inventory Items
* Get Inventory By ID
* Update Inventory Item
* Delete Inventory Item

### Health Monitoring

* Application Health Check
* Database Connectivity Validation

### Security

* Kubernetes Secrets
* Dedicated Service Account
* Role Based Access Control

### Scalability

* Horizontal Pod Autoscaler
* CPU Based Scaling
* Automatic Scale Up and Scale Down

### Reliability

* Rolling Updates
* Rollbacks
* Startup Probe
* Readiness Probe
* Liveness Probe

---

## Kubernetes Architecture

Client
↓
Traefik Ingress
↓
Farm Inventory Service
↓
Farm Inventory Pods
↓
PostgreSQL Service
↓
PostgreSQL Database

Namespaces:

* farm
* database

---

## CI/CD Pipeline

Git Push
↓
GitHub Actions
↓
Build Docker Image
↓
Trivy Security Scan
↓
Push Docker Image
↓
Cleanup Old Docker Tags
↓
Deploy to Kubernetes
↓
Verify Rollout

---

## Kubernetes Features Implemented

- Namespace Isolation
- ConfigMaps
- Secrets
- Deployments
- Services
- Ingress (Traefik)
- Persistent Volumes
- Health Checks
- Startup Probes
- Readiness Probes
- Liveness Probes
- Horizontal Pod Autoscaler (HPA)
- Pod Disruption Budget (PDB)
- RBAC (ServiceAccount, Role, RoleBinding)
- Rolling Updates
- Rollbacks

## DevOps Features Implemented

- GitHub Actions CI/CD
- Self Hosted Runner
- Docker Build Automation
- Docker Hub Integration
- Trivy Security Scanning
- Automated Kubernetes Deployment
- Docker Image Retention Policy

---

## Current Project Status

Version: v1.0.0

Completed:

* FastAPI CRUD APIs
* PostgreSQL Integration
* Kubernetes Deployment
* CI/CD Pipeline
* Ingress Access
* HPA Validation
* PDB Configuration
* RBAC Implementation

Upcoming:

* Helm Charts
* Prometheus Monitoring
* Grafana Dashboards
* Loki Logging
* ArgoCD GitOps

---

## Author

Arjun M J

DevOps Engineer | Cloud Architect | Cyber Forensics Analyst
