import json
import random
import boto3

# Inicializa el recurso DynamoDB
dynamodb = boto3.resource('dynamodb')

# Nombre de la tabla DynamoDB
table_name = 'museumTitles'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Escanea la tabla para obtener todos los registros
        response = table.scan()
        items = response.get('Items', [])
        
        if not items:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'No museum data found.'}),
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
        
        # Selecciona un museo al azar
        random_museum = random.choice(items)
        
        # Devuelve toda la información del museo
        return {
            'statusCode': 200,
            'body': json.dumps(random_museum),  # Envía todo el objeto del museo
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    except Exception as e:
        # Maneja cualquier error
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
