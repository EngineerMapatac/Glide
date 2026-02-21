# Glide 🌬️

**An automated workflow diagnostic engine for continuous improvement.**

---

## What is Glide?

Glide is an open-source analytics overlay designed to automatically identify bottlenecks, rework loops, and wasted time in team workflows. 

When coordinating fast-paced teams or managing escalations, efficiency is everything. However, most ticketing systems (like Jira, Zendesk, or internal tools) only show you the *current status* of a task. They don't tell you the health of the process itself. Glide ingests raw task events and applies continuous improvement logic to pinpoint exactly where workflows are stalling and why.

---

## The Problem It Solves

Relying on gut feeling to find process defects costs teams time and money. Glide automatically measures the metrics that actually matter:
* **Wait Time vs. Touch Time:** Accurately track how long a task is actively being worked on versus how long it sits idle in a queue waiting for assignment.
* **Rework Rate (Defects):** Automatically flag tickets that are repeatedly reopened or sent back to a previous stage, indicating broken processes or unclear instructions.
* **Handoff Waste:** Measure the time lost every time a task changes hands between departments or agents.

---

## Core Features (MVP)

* **REST API Ingestion:** Push state-change events directly from your existing tools or upload historical CSV data.
* **Waste Identification Algorithm:** Automatically flags tasks that exceed historical cycle times or get caught in reassignment loops.
* **Process Health Dashboard:** A clean, minimal React frontend visualizing workflow bottlenecks in real-time.

---

## Getting Started (Using the Pre-built Image) 🚀

You do not need to build the backend from scratch. You can pull the latest pre-built Docker image directly from the GitHub Container Registry (GHCR).

1. **Pull the backend image:**

```
docker pull ghcr.io/YOUR_USERNAME/glide-backend:latest

```

2. **Run the container locally:**

```
docker run -d -p 8000:8000 ghcr.io/YOUR_USERNAME/glide-backend:latest

```

---
---

## Getting Started (Local Development from Source)

---

1. **Clone the repo:**

```
git clone [https://github.com/YOUR_USERNAME/glide.git](https://github.com/YOUR_USERNAME/glide.git)
cd glide

```

---

2. **Start the environment using Docker Compose:**

```
docker-compose up --build

```

---

3. **Access the app:**
* Frontend: `http://localhost:3000`
* Backend API Docs: `http://localhost:8000/docs`



## Deployment

Glide is designed to be easily deployed to PaaS providers like **Render** or Railway. The included `docker-compose.yml` and `Dockerfile` setups ensure that what you test locally on your machine runs identically in the cloud.

## The Glide Cloud (Roadmap)

The core diagnostic engine is fully open-source and free to self-host. A fully managed, cloud-hosted version of Glide featuring enterprise SSO, real-time Slack alerting, and automated reporting will be available for teams requiring a zero-maintenance SaaS solution.

## Contributing

Pull requests are welcome. If you are planning a major change, please open an issue first to discuss the proposed updates.