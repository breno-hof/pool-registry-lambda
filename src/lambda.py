import json

def lambda_handler(event, context):
    import json

def lambda_handler(event, context):
    # Verifica se o corpo da requisição está presente
    if 'body' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No body provided'})
        }

    # Converte o corpo da requisição de string JSON para um dicionário Python
    try:
        body = json.loads(event['body'])
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }

    # Exemplo de validação dos dados recebidos
    required_fields = ['name', 'location', 'volume', 'material', 'heating_type', 'maintenance_frequency']
    for field in required_fields:
        if field not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f'Missing required field: {field}'})
            }

    # Simula a criação de um novo Pool (aqui você pode adicionar lógica para salvar no banco de dados, etc.)
    new_pool = {
        'pool_id': '123e4567-e89b-12d3-a456-426614174000',  # Simula um ID gerado
        'name': body['name'],
        'location': body['location'],
        'volume': body['volume'],
        'material': body['material'],
        'heating_type': body['heating_type'],
        'maintenance_frequency': body['maintenance_frequency'],
        'notes': body.get('notes', '')  # Campo opcional
    }

    # Retorna uma resposta de sucesso
    return {
        'statusCode': 201,
        'body': json.dumps(new_pool)
    }
