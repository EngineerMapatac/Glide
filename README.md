# Glide 🌬️

**An automated workflow diagnostic engine for continuous improvement.**

## What is Glide?
Glide is an open-source analytics overlay designed to automatically identify bottlenecks, rework loops, and wasted time in team workflows. 

When coordinating fast-paced teams or managing escalations, efficiency is everything. However, most ticketing systems (like Jira, Zendesk, or internal tools) only show you the *current status* of a task. They don't tell you the health of the process itself. Glide ingests raw task events and applies continuous improvement logic to pinpoint exactly where workflows are stalling and why.

## The Problem It Solves
Relying on gut feeling to find process defects costs teams time and money. Glide automatically measures the metrics that actually matter:
* **Wait Time vs. Touch Time:** Accurately track how long a task is actively being worked on versus how long it sits idle in a queue waiting for assignment.
* **Rework Rate (Defects):** Automatically flag tickets that are repeatedly reopened or sent back to a previous stage, indicating broken processes or unclear instructions.
* **Handoff Waste:** Measure the time lost every time a task changes hands between departments or agents.

## Core Features (MVP)
* **REST API Ingestion:** Push state-change events directly from your existing tools or upload historical CSV data.
* **Waste Identification Algorithm:** Automatically flags tasks that exceed historical cycle times or get caught in reassignment loops.
* **Process Health Dashboard:** A clean, minimal React frontend visualizing workflow bottlenecks in real-time.

## Tech Stack
* **Backend:** Python (FastAPI/Flask) - Optimized for fast data manipulation.
* **Frontend:** React.js - Component-driven, responsive dashboard.
* **Database:** PostgreSQL - Essential for maintaining a strict, relational audit trail of task events.
* **Deployment:** Dockerized for seamless local development (macOS/Linux) and one-click cloud deployment.

## Getting Started (Local Development)

1. **Clone the repo:**

   ```
   git clone [https://github.com/yourusername/glide.git](https://github.com/yourusername/glide.git)
   cd glide
   ```