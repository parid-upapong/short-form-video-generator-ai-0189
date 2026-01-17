terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  # Recommended: Configure S3 Backend for state management
  # backend "s3" { ... }
}

provider "aws" {
  region = var.aws_region
}

data "aws_availability_zones" "available" {}