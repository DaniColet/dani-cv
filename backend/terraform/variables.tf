variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  default     = "cloud-resume-challenge"
}

variable "dynamodb_table_name" {
  description = "DynamoDB table name"
  default     = "cv-visitor-counter"
}

variable "domain_name" {
  description = "Base domain name"
  default     = "dcoletasix2a.cat"
}

variable "subdomain" {
  description = "Subdomain"
  default     = "aws10"
}

variable "amplify_default_domain" {
  description = "Default Amplify domain to point CNAME to (e.g., main.d12345.amplifyapp.com)"
  type        = string
}

variable "frontend_url" {
  description = "Frontend URL for CORS"
  type        = string
  default     = "https://cv.aws10.dcoletasix2a.cat"
}
