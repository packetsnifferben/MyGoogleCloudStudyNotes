import os
from google.cloud import storage
from google.cloud import compute_v1

# Python Google Cloud Client Library Script: GCP Resource Audit

def list_storage_buckets(project_id):
    print(f"[*] Auditing Cloud Storage Buckets in Project: {project_id}")
    try:
        storage_client = storage.Client(project=project_id)
        buckets = storage_client.list_buckets()
        for bucket in buckets:
            print(f"  └── Bucket: {bucket.name} | Location: {bucket.location} | Storage Class: {bucket.storage_class}")
    except Exception as e:
        print(f"  └── Error retrieving buckets: {e}")

def list_compute_instances(project_id, zone="us-central1-a"):
    print(f"\n[*] Auditing Compute Engine Instances in Zone: {zone}")
    try:
        instance_client = compute_v1.InstancesClient()
        instances = instance_client.list(project=project_id, zone=zone)
        for instance in instances:
            print(f"  └── Instance: {instance.name} | Status: {instance.status} | Machine Type: {instance.machine_type.split('/')[-1]}")
    except Exception as e:
        print(f"  └── Error retrieving instances: {e}")

if __name__ == "__main__":
    gcp_project = os.getenv("GCP_PROJECT_ID", "your-gcp-project-id")
    print("=== GCP Enterprise Baseline Infrastructure Audit ===")
    list_storage_buckets(gcp_project)
    list_compute_instances(gcp_project)
