# This task definition specifies the GPU resource requirement
resource "aws_ecs_task_definition" "video_worker" {
  family                   = "${var.project_name}-video-worker"
  requires_compatibilities = ["EC2"]
  network_mode             = "awsvpc"
  cpu                      = 2048
  memory                   = 8192

  container_definitions = jsonencode([
    {
      name      = "viral-flow-worker"
      image     = "your-registry/viral-flow-worker:latest"
      essential = true
      
      # GPU Allocation
      resourceRequirements = [
        {
          type  = "GPU"
          value = "1"
        }
      ]

      environment = [
        { name = "SQS_QUEUE_URL", value = aws_sqs_queue.render_tasks.url },
        { name = "S3_BUCKET", value = aws_s3_bucket.video_assets.id },
        { name = "AWS_REGION", value = var.aws_region }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/${var.project_name}-worker"
          "awslogs-region"        = var.aws_region
          "awslogs-stream-prefix" = "worker"
        }
      }
    }
  ])
}

resource "aws_cloudwatch_log_group" "worker_logs" {
  name              = "/ecs/${var.project_name}-worker"
  retention_in_days = 7
}