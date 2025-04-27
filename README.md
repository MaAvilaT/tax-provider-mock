# tax-provider-mock
A mock microservice that simulates a third-party tax calculation service.

## Overview

This API allows you to retrieve tax information for different countries using a country code and an API key for authentication. The service returns the country's currency, VAT percentage, and a list of additional tax obligations.

important, this project is extremely easily deployable in GCP Cloud Run, recommended for small tests/experiments or
for academic purposes.

## Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional)

### Installation

#### Local Setup

1. Clone the repository:
```shell script
git clone https://github.com/MaAvilaT/tax-provider-api.git
   cd tax-provider-api
```

2. Install dependencies:
```shell script
pip install -r requirements.txt
```

3. Run the service:
```shell script
python app.py
```

#### Docker Setup

1. Build the Docker image:
```shell script
docker build -t tax-provider-api:latest .
```

2. Run the container:
```shell script
docker run -p 5000:5000 tax-provider-api:latest
```

## API Documentation

### Authentication

All API requests require an API key to be provided in the headers:

```
X-API-Key: tax_api_key_123456
```

Valid API keys:
- `tax_api_key_123456`
- `tax_api_key_654321`
- `test_api_key`

### Endpoints

#### Get Tax Data

Retrieves tax information for a specific country.

```
GET /api/v1/tax?country_code={country_code}
```

**Parameters:**
- `country_code` (required): The two-letter country code (e.g., US, ES, MX)

**Response Example:**
```json
{
  "success": true,
  "data": {
    "country_code": "ES",
    "currency": "EUR",
    "vat_percentage": 21.0,
    "additional_obligations": [
      "Declaración trimestral",
      "Impuesto de sociedades"
    ]
  }
}
```

**Error Responses:**

1. Invalid API Key (401):
```json
{
  "error": "Unauthorized",
  "message": "Invalid or missing API key"
}
```

2. Missing Country Code (400):
```json
{
  "error": "Bad Request",
  "message": "Missing country_code parameter"
}
```

3. Country Not Found (404):
```json
{
  "error": "Not Found",
  "message": "No tax data found for country code: XX"
}
```

#### Health Check

Verifies if the service is running correctly.

```
GET /api/v1/health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "tax-provider-api"
}
```

## Supported Countries

The API currently supports the following countries:

| Country Code | Country Name      | Currency | VAT %  |
|--------------|-------------------|----------|--------|
| ES           | Spain             | EUR      | 21.0   |
| US           | United States     | USD      | 7.25   |
| MX           | Mexico            | MXN      | 16.0   |
| AR           | Argentina         | ARS      | 21.0   |
| BR           | Brazil            | BRL      | 17.0   |
| CO           | Colombia          | COP      | 19.0   |
| CL           | Chile             | CLP      | 19.0   |
| DE           | Germany           | EUR      | 19.0   |
| FR           | France            | EUR      | 20.0   |
| UK           | United Kingdom    | GBP      | 20.0   |
| JP           | Japan             | JPY      | 10.0   |
| CN           | China             | CNY      | 13.0   |
| AU           | Australia         | AUD      | 10.0   |

## Deployment to GCP Artifact Registry

1. Update the variables in the deployment script:
```shell script
vi deploy_to_gcp.sh
```

2. Make the script executable:
```shell script
chmod +x deploy_to_gcp.sh
```

3. Run the deployment script:
```shell script
./deploy_to_gcp.sh
```

## Development

### Project Structure

Single file implementation (`app.py`):
- Flask application setup
- API key validation
- Tax data mock database
- API endpoints for tax data and health check

### Adding New Countries

To add new tax information for a country, update the `TAX_DATABASE` dictionary in `app.py`:

```python
'NEW_COUNTRY_CODE': {
    'country_code': 'NEW_COUNTRY_CODE',
    'currency': 'CURRENCY_CODE',
    'vat_percentage': VAT_PERCENTAGE,
    'additional_obligations': ['Obligation 1', 'Obligation 2']
},
```
