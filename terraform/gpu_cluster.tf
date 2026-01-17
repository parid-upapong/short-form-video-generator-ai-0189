# Create ECS Cluster
resource "aws_ecs_cluster" "gpu_cluster" {
  name = "${var.project_name}-gpu-cluster"
}

# Fetch the latest ECS optimized AMI for GPU
data "aws_ssm_parameter" "ecs_gpu_ami" {
  name = "/aws/service/ecs/optimized-ami/amazon-linux-2/gpu/recommended/image_id"
}

# Launch Template for GPU Instances
resource "aws_launch_template" "gpu_nodes" {
  name_prefix   = "${var.project_name}-gpu-launch-template"
  image_id      = data.aws_ssm_parameter.ecs_gpu_ami.value
  instance_type = var.gpu_instance_type

  iam_instance_profile {
    name = aws_iam_instance_profile.gpu_node_profile.name
  }

  network_interfaces {
    associate_public_ip_address = false
    security_groups             = [aws_security_group.gpu_node_sg.id]
  }

  user_data = base64encode(<<-EOF
              #!/bin/bash
              echo ECS_CLUSTER=${aws_ecs_cluster.gpu_cluster.name} >> /etc/ecs/ecs.config
              EOF
  )
}

# Auto Scaling Group for GPU Workers
resource "aws_autoscaling_group" "gpu_asg" {
  name                = "${var.project_name}-gpu-asg"
  vpc_zone_identifier = module.vpc.private_subnets
  min_size            = var.min_gpu_instances
  max_size            = var.max_gpu_instances
  desired_capacity    = var.min_gpu_instances

  launch_template {
    id      = aws_launch_template.gpu_nodes.id
    version = "$Latest"
  }

  tag {
    key                 = "AmazonECSManaged"
    value               = true
    propagate_at_launch = true
  }
}

# Security Group for EC2 GPU Instances
resource "aws_security_group" "gpu_node_sg" {
  name   = "${var.project_name}-gpu-node-sg"
  vpc_id = module.vpc.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Capacity Provider to link ASG and ECS
resource "aws_ecs_capacity_provider" "gpu_cp" {
  name = "${var.project_name}-gpu-capacity-provider"

  auto_scaling_group_provider {
    auto_scaling_group_arn = aws_autoscaling_group.gpu_asg.arn
    managed_scaling {
      status          = "ENABLED"
      target_capacity = 80
    }
  }
}

resource "aws_ecs_cluster_capacity_providers" "gpu_cluster_cp" {
  cluster_name = aws_ecs_cluster.gpu_cluster.name
  capacity_providers = [aws_ecs_capacity_provider.gpu_cp.name]
}