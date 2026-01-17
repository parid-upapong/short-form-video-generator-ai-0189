# S3 Bucket for Raw and Processed Video
resource "aws_s3_bucket" "video_assets" {
  bucket = "${var.project_name}-assets-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
  byte_length = 4
}

# SQS Queue for Rendering Tasks
resource "aws_sqs_queue" "render_tasks" {
  name                        = "${var.project_name}-render-queue"
  visibility_timeout_seconds  = 3600 # 1 hour for long video processing
  message_retention_seconds   = 86400
}

# SQS Queue for Completed Notification
resource "aws_sqs_queue" "completion_queue" {
  name = "${var.project_name}-completion-queue"
}