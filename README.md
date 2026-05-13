# AI-Powered Telecom Incident Intelligence & Operational Risk Monitoring Platform

An AI-powered telecom analytics platform that transforms raw incident data into live operational intelligence using Machine Learning, FastAPI, React, and real-time analytics dashboards.

The system helps monitor telecom incidents, predict high-risk reopen cases, analyze regional performance, track operational KPIs, and visualize network stability through dynamic dashboards and predictive analytics.

---

# Problem Statement

Telecom operations teams handle massive volumes of incidents daily, making it difficult to:

* identify high-risk incidents quickly,
* monitor operational instability,
* prevent repeated escalations,
* analyze regional outage impact,
* and track real-time network health.

This platform solves that problem by converting telecom incident data into actionable AI-driven operational intelligence through predictive monitoring and live analytics dashboards.

---

# Key Features

* ML-based Reopen Risk Prediction
* Live Telecom KPI Monitoring
* Dynamic Incident Trend Analysis
* Regional Telecom Analytics
* Network Performance Tracking
* Risk Intelligence Dashboard
* Real-Time Dashboard Refresh
* Personalized Analytics Dashboards
* FastAPI Backend APIs
* Interactive Recharts Visualizations
* Cloud Deployment with Render & Vercel

---

# Tech Stack

## Frontend

* React
* Vite
* TailwindCSS
* Recharts

## Backend

* FastAPI
* Pydantic

## Machine Learning

* Scikit-learn
* RandomForestClassifier
* SMOTE
* Pandas
* NumPy

## Deployment

* Render
* Vercel

---

# System Architecture

```text
                        ┌──────────────────────┐
                        │ Telecom Incident Data│
                        └──────────┬───────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │ Data Preprocessing Layer │
                    │ Encoding • Cleaning • ML │
                    └──────────┬───────────────┘
                               │
                               ▼
                    ┌──────────────────────────┐
                    │ Machine Learning Engine  │
                    │ RandomForest + SMOTE     │
                    └──────────┬───────────────┘
                               │
                               ▼
                    ┌──────────────────────────┐
                    │ FastAPI Prediction APIs  │
                    │ KPI • Risk • Analytics   │
                    └──────────┬───────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
     ┌──────────────────┐         ┌────────────────────┐
     │ React Dashboard  │         │ Personalized Views │
     │ Live Analytics   │         │ Region • Risk • ML │
     └──────────────────┘         └────────────────────┘
```

---

# Live Deployment

## Frontend

https://telecom-incident-intellige-git-066b07-sanskriti-duttas-projects.vercel.app

## Backend

https://telecom-ai-backend-pm1k.onrender.com

---

# Dashboards Included

* Risk & Operations Hub
* Monthly Incident Trends
* Region Analysis Dashboard
* Network Performance Dashboard
* Reopen Risk Dashboard

---

# Machine Learning Workflow

* Telecom Incident Dataset Processing
* Feature Engineering
* Categorical Encoding
* SMOTE Balancing
* RandomForest Training
* Reopen Probability Prediction
* Live ML Inference APIs

---

# Future Improvements

* GenAI Operational Copilot
* SHAP Explainability
* Kafka Streaming
* WebSocket Live Telemetry
* Alert Notification Engine
* Anomaly Detection
* Role-Based Authentication

---

# Author

Sanskriti Dutta
