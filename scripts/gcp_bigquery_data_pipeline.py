"""
Google Cloud BigQuery Data Pipeline Automation Script
Target: GCP Data & AI Engineering / Backend Integration
"""

import os
from google.cloud import bigquery
import pandas as pd

def fetch_and_process_bigquery_data(project_id: str):
    print(f"Initializing BigQuery client for project: {project_id}")
    client = bigquery.Client(project=project_id)
    
    query = """
        SELECT 
            transaction_date,
            customer_id,
            product_category,
            SUM(sales_amount) as total_sales
        FROM `datamart.sales_transactions`
        GROUP BY transaction_date, customer_id, product_category
        LIMIT 1000
    """
    
    try:
        df = client.query(query).to_dataframe()
        print(f"Successfully retrieved {len(df)} rows from BigQuery.")
        
        # Data processing logic with pandas
        summary_df = df.groupby('product_category')['total_sales'].sum().reset_index()
        print("Processed Sales Summary:")
        print(summary_df.head())
        
        return summary_df
    except Exception as e:
        print(f"Error executing BigQuery pipeline: {str(e)}")
        return None

if __name__ == "__main__":
    PROJECT_ID = os.getenv("GCP_PROJECT_ID", "my-gcp-production-project")
    fetch_and_process_bigquery_data(PROJECT_ID)
