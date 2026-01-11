# Cost Estimation

Estimated Monthly Cost: **$1.00 - $3.00**

| Service | Tier / Usage | Estimated Cost |
|---------|--------------|----------------|
| **DynamoDB** | On-Demand, < 1000 RW/month | Free Tier (25GB storage, 25 RCU/WCU) -> **$0.00** |
| **Lambda** | < 1000 requests, 128MB, 100ms | Free Tier (400k GB-seconds) -> **$0.00** |
| **API Gateway** | HTTP API, ~1000 requests | $1.00/million requests -> **<$0.01** |
| **Route 53** | 1 Hosted Zone | **$0.50** / month |
| **S3** | Terraform State (minimal) | **<$0.01** |
| **Amplify** | Build minutes + Hosting | Free Tier (1000 mins, 5GB storage) -> **$0.00** |
| **CloudWatch** | Logs (minimal) | Free Tier (5GB data) -> **$0.00** |

**Total**: ~$0.52 (rounded up to $1 for buffer).
