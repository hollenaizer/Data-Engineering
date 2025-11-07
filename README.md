# Data-Engineering
A collection of AWS and Cloud Data Engineering projects built by Casswell Maswanganye

# 👋 Hi, I'm Casswell Maswanganye
🚀 **Aspiring Data Engineer | AWS Cloud | ETL | Data Pipelines | Banking Systems**

Welcome to my Data Engineering portfolio — a collection of hands-on projects I’ve built using AWS services and Python to simulate real-world financial data workflows.

---

## 🏦 Featured Projects

### 🔹 [1. AWS ETL Pipeline for Banking Transactions](./aws-etl-banking/)
**Tech Stack:** AWS Glue, S3, Athena, IAM, PySpark  
- Built an automated ETL pipeline that processes daily bank transaction data from S3.
- Used AWS Glue to clean, transform, and store data in Parquet format.
- Queried processed data using Athena to produce daily deposit/withdrawal summaries.

📘 **Dataset:** `transactions.csv` (50 sample records)  
📊 **Goal:** Simulate a daily transaction processing pipeline used by banks.

---

### 🔹 [2. Real-Time Fraud Detection System](./fraud-detection-stream/)
**Tech Stack:** AWS Kinesis, Lambda, DynamoDB, CloudWatch  
- Streamed live credit card transactions via Kinesis.
- Used a Lambda function to detect suspicious activity (transactions > R1000).
- Stored flagged transactions in DynamoDB for audit and investigation.

📘 **Goal:** Build a serverless data streaming pipeline to detect fraud in real time.

---

## ☁️ AWS Services Used
- **S3** – Data Lake
- **AWS Glue** – ETL and Data Catalog
- **Athena** – Serverless SQL queries
- **Lambda** – Event-driven compute
- **Kinesis** – Data streaming
- **DynamoDB** – NoSQL storage
- **IAM** – Role-based access control

---

## 🐍 Languages & Tools
Python | SQL | PySpark | AWS CLI | Git | Linux | Power BI

---

## 📂 Repository Structure

