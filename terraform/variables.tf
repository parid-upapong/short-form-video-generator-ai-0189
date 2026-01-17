variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for resource tagging"
  default     = "viral-flow"
}

variable "gpu_instance_type" {
  description = "Instance type with GPU support (G4dn is best for cost/perf for inference)"
  default     = "g4dn.xlarge" # 1 NVIDIA T4 GPU
}

variable "min_gpu_instances" {
  default = 1
}

variable "max_gpu_instances" {
  default = 10
}