# DevOps Monitoring Platform

A complete DevOps monitoring project built with Kubernetes, Helm, Jenkins, Grafana, Prometheus, and PostgreSQL.

## 📌 Project Overview
This project demonstrates a production-like monitoring and deployment pipeline.  
It includes:
- **Jenkins Pipeline** for building, pushing, and deploying the application.
- **Docker** for containerization.
- **Kubernetes + Helm** for orchestration and deployment.
- **Prometheus** for metrics collection.
- **Grafana** for visualization and dashboards.
- **PostgreSQL** as the application database.

## 🚀 Features
- CI/CD pipeline with Jenkins.
- Automated build & push to DockerHub.
- Kubernetes deployment with Helm.
- Real-time monitoring using Prometheus & Grafana.
- Node Exporter integrated with Prometheus for cluster metrics.
- Persistent storage for PostgreSQL.

## 🛠️ Tech Stack
- **CI/CD**: Jenkins
- **Containerization**: Docker
- **Orchestration**: Kubernetes, Helm
- **Monitoring**: Prometheus, Grafana, Node Exporter
- **Database**: PostgreSQL

## 📊 Monitoring Setup
- **Prometheus** scrapes metrics from Node Exporter and application endpoints.
- **Grafana** visualizes Prometheus data with pre-configured dashboards.


