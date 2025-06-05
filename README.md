# 🖥️ Grafana Alerting & Reporting for System Monitoring

> Final-Year DevOps Project – M.Sc. Software Systems  
> Kongu Engineering College, April 2025  
> **By:** Makanesha V (22ISR023)

## 🔍 Overview

This project presents a **Docker-based infrastructure monitoring and alerting system** that integrates Grafana, Prometheus, Node Exporter, and Alertmanager. It enables real-time metric collection, alert configuration, and email notifications — all containerized for scalability and ease of deployment.

---

## 🧠 Objective

To develop a monitoring solution using Grafana alerting and Prometheus metric collection, with automated email alerts and real-time dashboards — minimizing manual configuration.

---

## 🏗️ Architecture

### 🔧 Modules
- **Metrics Collection**: Node Exporter + Prometheus
- **Alert Management**: Prometheus alert rules
- **Notification Dispatch**: Alertmanager with email config
- **Visualization**: Grafana dashboards
- **Container Orchestration**: Docker Compose

---

## 🛠️ Tech Stack

| Tool         | Purpose                      |
|--------------|-------------------------------|
| Docker       | Container orchestration        |
| Grafana      | Dashboard & alert visualization |
| Prometheus   | Metrics scraping & storage     |
| Node Exporter| Host-level metric collection   |
| Alertmanager | Routing alert notifications    |

---

## 📊 Features

- 📈 Real-time system metric monitoring (CPU, memory, disk I/O, etc.)
- 🔔 Email alerts triggered by threshold-based rules
- 📬 Custom SMTP configuration for Alertmanager
- 📊 Grafana dashboards for interactive visualization
- 🧱 Modular, scalable Docker Compose architecture

---

## 📂 Folder Structure

```bash
├── docker-compose.yml
├── prometheus.yml
├── alertmanager.yml
├── screenshots/
│   ├── container_running.png
│   ├── alert_triggered.png
│   └── email_notification.png
└── README.md
