from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_API_KEYS = [
    "tax_api_key_123456",
    "tax_api_key_654321",
    "test_api_key"
]

TAX_DATABASE = {
    'ES': {
        'country_code': 'ES',
        'currency': 'EUR',
        'vat_percentage': 21.0,
        'additional_obligations': ['Declaración trimestral', 'Impuesto de sociedades']
    },
    'US': {
        'country_code': 'US',
        'currency': 'USD',
        'vat_percentage': 7.25,
        'additional_obligations': ['State tax may apply']
    },
    'MX': {
        'country_code': 'MX',
        'currency': 'MXN',
        'vat_percentage': 16.0,
        'additional_obligations': ['IVA', 'ISR']
    },
    'AR': {
        'country_code': 'AR',
        'currency': 'ARS',
        'vat_percentage': 21.0,
        'additional_obligations': ['Ingresos Brutos', 'Impuesto PAIS']
    },
    'BR': {
        'country_code': 'BR',
        'currency': 'BRL',
        'vat_percentage': 17.0,
        'additional_obligations': ['ICMS', 'ISS']
    },
    'CO': {
        'country_code': 'CO',
        'currency': 'COP',
        'vat_percentage': 19.0,
        'additional_obligations': ['Retención en la fuente']
    },
    'CL': {
        'country_code': 'CL',
        'currency': 'CLP',
        'vat_percentage': 19.0,
        'additional_obligations': ['Impuesto a la renta']
    },
    'DE': {
        'country_code': 'DE',
        'currency': 'EUR',
        'vat_percentage': 19.0,
        'additional_obligations': ['Umsatzsteuer']
    },
    'FR': {
        'country_code': 'FR',
        'currency': 'EUR',
        'vat_percentage': 20.0,
        'additional_obligations': ['Taxe sur la valeur ajoutée']
    },
    'UK': {
        'country_code': 'UK',
        'currency': 'GBP',
        'vat_percentage': 20.0,
        'additional_obligations': ['Corporate tax']
    },
    'JP': {
        'country_code': 'JP',
        'currency': 'JPY',
        'vat_percentage': 10.0,
        'additional_obligations': ['Corporate tax', 'Resident tax']
    },
    'CN': {
        'country_code': 'CN',
        'currency': 'CNY',
        'vat_percentage': 13.0,
        'additional_obligations': ['Enterprise Income Tax']
    },
    'AU': {
        'country_code': 'AU',
        'currency': 'AUD',
        'vat_percentage': 10.0,
        'additional_obligations': ['Goods and Services Tax']
    },
}


@app.route('/api/v1/tax', methods=['GET'])
def get_tax_data():
    api_key = request.headers.get('X-API-Key')
    if not api_key or api_key not in VALID_API_KEYS:
        return jsonify({
            'error': 'Unauthorized',
            'message': 'Invalid or missing API key'
        }), 401

    country_code = request.args.get('country_code')
    if not country_code:
        return jsonify({
            'error': 'Bad Request',
            'message': 'Missing country_code parameter'
        }), 400

    country_code = country_code.upper()
    tax_data = TAX_DATABASE.get(country_code)

    if not tax_data:
        return jsonify({
            'error': 'Not Found',
            'message': f'No tax data found for country code: {country_code}'
        }), 404

    return jsonify({
        'success': True,
        'data': tax_data
    }), 200


@app.route('/api/v1/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'tax-provider-api'
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
