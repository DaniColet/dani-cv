output "api_endpoint" {
  description = "API Gateway Endpoint"
  value       = "${aws_apigatewayv2_api.http_api.api_endpoint}/prod/counter"
}

output "dynamodb_table" {
  description = "DynamoDB Table Name"
  value       = aws_dynamodb_table.visitor_counter.name
}

output "nameservers" {
  description = "Route 53 Name Servers"
  value       = aws_route53_zone.main.name_servers
}
