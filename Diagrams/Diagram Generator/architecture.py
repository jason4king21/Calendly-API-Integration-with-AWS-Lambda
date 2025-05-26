from diagrams import Diagram, Cluster
from diagrams.onprem.vcs import Github
from diagrams.onprem.container import Docker
from diagrams.onprem.client import Users
from diagrams.programming.language import Python
from diagrams.aws.compute import Lambda
from diagrams.aws.compute import ECR
from diagrams.aws.security import SecretsManager
from diagrams.aws.storage import S3


with Diagram("Calendly API ETL Pipeline", show=False, filename="diagrams/architecture", outformat="png"):
    github = Github("GitHub Actions")
    docker = Docker("Docker Image")
    ecr = ECR("ECR Repo")

    with Cluster("AWS"):
        secrets = SecretsManager("Secrets Manager")
        lambda_fn = Lambda("Lambda (Docker)")
        s3 = S3("S3 Bucket")

    calendly = Users("Calendly API")
    python_proc = Python("Python + Pandas")

    github >> docker >> ecr >> lambda_fn
    lambda_fn >> [secrets, calendly]
    lambda_fn >> python_proc >> s3
