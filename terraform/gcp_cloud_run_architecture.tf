# Terraform Configuration for Google Cloud Run Deployment
# Target: Google Cloud Professional Cloud Architect

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {
  type    = string
  default = "my-gcp-production-project"
}

variable "region" {
  type    = string
  default = "us-central1"
}

resource "google_cloud_run_v2_service" "default" {
  name     = "enterprise-api-service"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "gcr.io/cloudrun/hello"
      resources {
        limits = {
          memory = "1Gi"
          cpu    = "1"
        }
      }
    }
  }
}

resource "google_cloud_run_service_iam_member" "noauth" {
  location = google_cloud_run_v2_service.default.location
  name     = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
