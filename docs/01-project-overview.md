# Project Overview

## Introduction

Farm Inventory is a cloud-native inventory management platform built to demonstrate modern DevOps practices and GitOps-based Kubernetes deployments.

The project evolved from a simple FastAPI application into a complete deployment platform supporting:

* Standard Kubernetes Deployments
* Manual Canary Deployments
* Blue-Green Deployments
* Argo Rollouts Progressive Delivery

The objective is to simulate real-world production deployment patterns while maintaining full automation through Helm and ArgoCD.

---

## Business Problem

Organizations require:

* Zero downtime deployments
* Safe application upgrades
* Automatic scaling
* Monitoring and alerting
* Controlled rollbacks

Farm Inventory demonstrates solutions for these challenges.

---

## Key Features

### Application

* Inventory Management APIs
* PostgreSQL Integration
* Health Endpoints

### Infrastructure

* Kubernetes
* Helm
* ArgoCD

### Deployment Strategies

* Rolling Update
* Canary
* Blue-Green
* Progressive Delivery

### Monitoring

* Prometheus
* ServiceMonitor
* Alert Rules

### Scaling

* Horizontal Pod Autoscaler

---

## Repository Structure

small-project

├── docker/
├── app/
├── k8s/
│ └── helm/
│ └── farm-stack/
├── docs/
├── .github/
└── README.md

---

## Architecture Overview

GitHub
↓
ArgoCD
↓
Helm
↓
Kubernetes
↓
Application Pods
↓
PostgreSQL

Prometheus monitors all platform components.
