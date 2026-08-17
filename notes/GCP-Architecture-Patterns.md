# GCP Enterprise Architecture Patterns & Cloud Adoption Framework Notes

Building scalable, enterprise-grade architectures on Google Cloud Platform requires establishing strong landing zone fundamentals, implementing robust IAM governance, and selecting appropriate compute/data paradigms.

> **Key Takeaway:** Principle of Least Privilege combined with Workload Identity Federation eliminates long-lived service account keys, drastically reducing identity security risks.

## 1. Enterprise Landing Zone Architecture

* **Resource Hierarchy:** Organization -> Folders (Business Units / Environments) -> Projects -> Resources. Policy inheritance flows downward.
* **Shared VPC:** Centralized networking hub managed by host projects while granting service projects isolated subnets.
* **Hybrid Connectivity:** Dedicated Interconnect (10G/100G direct links) vs. Partner Interconnect vs. Cloud VPN (HA VPN with dynamic BGP routing).

## 2. Compute Selection Matrix

* **Compute Engine (IaaS):** Full OS control, custom machine types, GPUs, and persistent disk attachments.
* **Google Kubernetes Engine (GKE):** Container orchestration for microservices with Autopilot for fully managed node lifecycle.
* **Cloud Run (Serverless):** Containerized stateless workloads scaling automatically down to zero based on HTTP requests.

## 3. Vertex AI Architecture & Generative AI Design

* **Foundation Models & Garden:** Leveraging PaLM/Gemini models via Vertex AI APIs for summarization, code generation, and embeddings.
* **Retrieval-Augmented Generation (RAG):** Combining Vector Search (Annoy/ScaNN) with BigQuery / Cloud Storage grounding data for accurate enterprise responses.
