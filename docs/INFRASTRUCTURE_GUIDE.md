# Infrastructure Documentation: GPU-Accelerated Rendering Pipeline

## Overview
This Terraform configuration sets up a production-ready AWS environment specifically tuned for AI video processing (Whisper, Computer Vision, FFmpeg).

## Key Components
1. **GPU Cluster:** Uses `g4dn.xlarge` instances which feature NVIDIA T4 GPUs. This is the industry standard for cost-effective inference.
2. **Auto-Scaling:** The ECS Capacity Provider automatically scales the EC2 fleet based on SQS queue depth or CPU/GPU utilization.
3. **IAM Scoping:** Minimalist roles granting the worker access only to the necessary S3 bucket and SQS queues.
4. **Networking:** Private subnets for GPU workers to ensure high security, with outbound access via NAT Gateway for downloading model weights (e.g., HuggingFace).

## How to Deploy
1. Ensure AWS CLI is configured with appropriate permissions.
2. `cd terraform`
3. `terraform init`
4. `terraform plan`
5. `terraform apply`

## Cost Optimization Notes
- **Spot Instances:** For production scaling, consider changing the `aws_launch_template` to use Spot instances for the GPU workers to reduce costs by up to 70%.
- **S3 Lifecycle:** Use lifecycle rules to move raw long-form videos to `INTELLIGENT_TIERING` after 30 days.

## GPU Driver Compatibility
The configuration uses the **ECS-optimized GPU AMI**. This AMI comes pre-installed with:
- NVIDIA Drivers
- NVIDIA Container Runtime
- Amazon ECS Agent
No manual driver installation is required in the Dockerfile.