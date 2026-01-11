# 5-Minute Presentation Script

**Project**: Cloud Resume Challenge AWS
**User**: Dani Colet

## Minute 1: Introduction & Goals
- **Goal**: Build a cloud-native resume visited by the world.
- **Access**: `cv.aws10.dcoletasix2a.cat` (HTTPS).
- **Core components**: Hugo frontend, Python/Lambda backend, Terraform Infrastructure.

## Minute 2: Architecture
- *Show Architecture Diagram*
- **Frontend**: Hosted on AWS Amplify (Global CDN).
- **Backend Service**: API Gateway + Lambda + DynamoDB.
- **DNS**: Cloudflare delegating to Route 53 (Hybrid DNS).

## Minute 3: Live Demo
1. Open the website: `https://cv.aws10.dcoletasix2a.cat`
2. Scroll to footer: "Visitor Count: X".
3. Refresh page: Counter increases to "X+1" (Atomic update).
4. Inspect Network tab: Show JSON response from API.
5. *Optional*: Show GitHub Action run (Green checkmark).

## Minute 4: Infrastructure as Code (Terraform)
- Walk through `main.tf`:
  - **DynamoDB**: On-demand billing.
  - **Lambda**: Python 3.11 with automatic zipping.
  - **Security**: IAM roles with least privilege (only `dynamodb:UpdateItem` etc).

## Minute 5: Challenges & Learnings
- **Challenge**: CORS configuration between two domains.
- **Solution**: Explicit `Access-Control-Allow-Origin` in Lambda response.
- **Learner Lab Constraints**: Handling temporary credentials in CI/CD.
- **Q&A**

## Backup Plan
- If site down: Show recorded video or local build.
- If counter fails: Show `test_lambda_function.py` passing in local terminal.
