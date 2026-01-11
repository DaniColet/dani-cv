resource "aws_route53_zone" "main" {
  name = "${var.subdomain}.${var.domain_name}"
}

resource "aws_route53_record" "cv_cname" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "cv.${var.subdomain}.${var.domain_name}"
  type    = "CNAME"
  ttl     = 300
  records = [var.amplify_default_domain]
}
