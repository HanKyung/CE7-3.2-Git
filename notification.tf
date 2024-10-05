# Create SNS pub-sub message bus with topic creation
resource "aws_sns_topic" "tf-sns-topic" {
  name = var.sns_topic_name
}

# Create SNS-SQS subscription
resource "aws_sns_topic_subscription" "tf-sns-email-subscription" {
  topic_arn = aws_sns_topic.tf-sns-topic.arn
  protocol  = "email"
  endpoint  = var.sns_endpoint
}
