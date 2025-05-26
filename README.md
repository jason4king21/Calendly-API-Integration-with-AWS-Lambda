# 📆 Calendly Scheduled Events ETL with AWS Lambda, Docker & GitHub Actions

This project demonstrates a secure, serverless ETL pipeline that retrieves scheduled event data from the **Calendly API**, transforms the data using Python, and stores both raw events and computed metrics into **Amazon S3**. The pipeline runs on a schedule using a **containerized AWS Lambda function**, deployed via **Docker** and **GitHub Actions**, and leverages **AWS Secrets Manager** for secure credential handling.

---

## 🧩 Architecture Overview

![Architecture](diagrams/architecture.png)

1. **AWS Lambda (Docker Image)**  
   - Authenticates to the Calendly API using a secure API key stored in **Secrets Manager**  
   - Retrieves scheduled events and computes engagement metrics  
   - Uploads `.csv` files to an **S3 bucket** (raw + summarized)

2. **Amazon ECR**  
   - Stores the Docker image for the Lambda function

3. **GitHub Actions**  
   - Automates the Docker build and deployment process to AWS Lambda using CI/CD

---

## 🔧 Tech Stack

- **AWS Lambda (Container Image)**
- **Amazon ECR**
- **Amazon S3**
- **AWS Secrets Manager**
- **GitHub Actions**
- **Calendly API**
- **Python** (pandas, boto3, requests)
- **Docker**


---

## ▶️ How It Works

1. **Secrets Management**:  
   Calendly API key is securely retrieved from AWS Secrets Manager using Boto3.

2. **Data Extraction**:  
   The Lambda function connects to the Calendly API and retrieves all scheduled event data.

3. **Data Transformation**:  
   The data is processed into a tabular format using pandas, and key metrics are calculated:
   - Total scheduled calls
   - Completed calls
   - Completion percentage

4. **Data Loading**:  
   Two CSV files (raw data + metrics summary) are uploaded to an Amazon S3 bucket.

5. **CI/CD Deployment**:  
   Docker image is built and pushed to ECR, then deployed to Lambda using GitHub Actions.

---

## ✅ Key Features

- 🔐 Secure credential management using AWS Secrets Manager
- 🐳 Containerized Lambda for portable, consistent execution
- 📊 Real-time metric tracking from Calendly data
- 🚀 Automated deployment pipeline with GitHub Actions
- 💾 Scalable storage with Amazon S3

---

## 🔒 Environment Variables

| Variable Name           | Description                          |
|------------------------|--------------------------------------|
| `S3_BUCKET_NAME`       | Target S3 bucket for storing files   |
| `S3_FOLDER_PATH`       | Path within the bucket for uploads   |
| `CALENDLY_SECRET_NAME` | Name of secret in Secrets Manager    |
| `AWS_REGION`           | AWS region to operate in             |

---

## 🏷️ Tags & Keywords
#AWS #Lambda #Docker #ECR #CalendlyAPI #SecretsManager #GitHubActions #S3 #ETL #Python #Serverless #DataEngineering #CI_CD
