# Cloud Resume Challenge Architecture

```mermaid
graph TD
    User([User]) -->|Visit HTTPS| Cloudflare{Cloudflare DNS}
    Cloudflare -->|Delegation| Route53[AWS Route 53]
    Route53 -->|CNAME| Amplify[AWS Amplify]
    Amplify -->|Serve Content| Hugo[Hugo Static Site]
    
    User -->|JS Fetch| APIGateway[API Gateway HTTP API]
    APIGateway -->|Invoke| Lambda[Lambda Function]
    Lambda -->|Update/Read| DynamoDB[(DynamoDB Table)]
    
    subgraph CI/CD
    GitHub[GitHub Actions] -->|Deploy| Terraform[Terraform]
    Terraform -->|Provision| Lambda
    Terraform -->|Provision| DynamoDB
    Terraform -->|Provision| APIGateway
    end
```

## Data Flow
1. **Frontend**: The user visits `cv.aws10.dcoletasix2a.cat`.
2. **Counter**: JavaScript on the page calls API Gateway `GET /counter`.
3. **Backend**: Lambda receives the request, updates DynamoDB atomially, and returns the new count.
4. **Response**: Frontend displays the visitor count.
