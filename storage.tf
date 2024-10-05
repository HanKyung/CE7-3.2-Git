
resource "aws_s3_bucket" "group1bucket" {
  bucket = "my-group-1-bucket"

  tags = {
    Name        = "group1bucket"
    Environment = "Dev"
  }
}
