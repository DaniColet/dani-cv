# Guía de Despliegue y Verificación (AWS Cloud Resume Challenge)

Esta guía te llevará paso a paso para desplegar la infraestructura en AWS (usando Terraform) y configurar el Frontend (Hugo + Amplify).

## 1. Prerrequisitos
Asegúrate de tener instalado en tu máquina (o en AWS CloudShell):
- **AWS CLI**: Configurado con tus credenciales (`aws configure`).
- **Terraform**: [Instalar Terraform](https://developer.hashicorp.com/terraform/downloads).
- **Hugo**: [Instalar Hugo](https://gohugo.io/installation/) (versión "extended").
- **Git**: Configurado.

## 2. Despliegue del Backend (Infraestructura)

1. **Navega al directorio de Terraform**:
   ```powershell
   cd backend/terraform
   ```

2. **Inicializa Terraform**:
   Descarga los proveedores necesarios (AWS).
   ```powershell
   terraform init
   ```

3. **Planifica el despliegue**:
   Verifica qué recursos se crearán.
   ```powershell
   terraform plan -out=tfplan
   ```
   *Nota: Se te pedirá confirmar `amplify_default_domain`. Puedes usar cualquier valor temporal (ej. `midominio.com`) si aún no tienes el de Amplify, pero lo necesitaremos para el DNS.*

4. **Aplica los cambios**:
   ```powershell
   terraform apply tfplan
   ```
   
5. **Guarda los Outputs**:
   Al finalizar, verás algo como:
   ```
   api_endpoint   = "https://xyz.execute-api.us-east-1.amazonaws.com/prod/counter"
   nameservers    = [...]
   dynamodb_table = "cv-visitor-counter"
   ```
   **Copia el `api_endpoint`**, lo necesitarás para el Frontend.

## 3. Configuración del Frontend

1. **Actualiza el JavaScript**:
   Edita el archivo `frontend/static/js/counter.js`.
   Reemplaza `REPLACE_WITH_YOUR_API_GATEWAY_URL` con tu `api_endpoint` copiado anteriormente.

2. **Sube el Código a GitHub**:
   ```powershell
   # Backend
   cd ../.. # raíz del proyecto
   git add .
   git commit -m "feat: initial implementation"
   # Asegúrate de tener el remote configurado
   git push origin main
   ```

## 4. Despliegue del Frontend (AWS Amplify)

1. Ve a la **Consola de AWS Amplify**.
2. Haz clic en **"Create new app"** -> **"GitHub"**.
3. Selecciona tu repositorio `curriculum-frontend` (o el que estés usando).
4. Amplify detectará automáticamente que es un sitio Hugo.
5. En la configuración de build, asegúrate de usar la imagen de build por defecto o una que tenga Hugo Extended.
6. Haz clic en **"Save and Deploy"**.

**Configuración de Dominio (DNS)**:
1. Una vez desplegado, Amplify te dará un dominio por defecto (ej. `d123.amplifyapp.com`).
2. Ve a `Device management` -> `Domain management`.
3. Añade tu dominio `cv.aws10.dcoletasix2a.cat`.
4. Amplify te pedirá verificar la propiedad (CNAME).
5. **IMPORTANTE**: Como usamos Terraform para Route 53, toma el valor CNAME que te da Amplify y actualiza tu archivo `backend/terraform/terraform.tfvars` (o pásalo como variable) y vuelve a hacer `terraform apply`.

## 5. Verificación Final

1. **Entra a tu web**: https://cv.aws10.dcoletasix2a.cat
2. **Revisa el Contador**: Debería mostrar un número y aumentar si recargas la página.
3. **Consola AWS**:
   - **DynamoDB**: Revisa la tabla `cv-visitor-counter`, debería tener un item con `id: visitors`.
   - **CloudWatch**: Revisa los logs en `/aws/lambda/cloud-resume-challenge-counter`.

## Solución de Problemas
- **El contador no carga**: Abre la consola del navegador (F12) -> Network. Si ves errores CORS, verifica que `frontend_url` en tus variables de Terraform coincida exactamente con tu dominio.
- **Error 500**: Revisa los logs de CloudWatch de la Lambda.
