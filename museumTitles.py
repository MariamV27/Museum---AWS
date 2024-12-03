import boto3

# Create a DynamoDB client

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cambia a tu región
table = dynamodb.Table('museumTitles')

definitions = [

    {"id": "1", "country": "France", "city": "Paris", "museum": "Louvre Museum", "description": "World's largest art museum, home to the Mona Lisa and Venus de Milo."},
    {"id": "2", "country": "United Kingdom", "city": "London", "museum": "British Museum", "description": "A world-renowned museum of human history and culture, with a vast collection of artifacts."},
    {"id": "3", "country": "United States", "city": "New York", "museum": "Metropolitan Museum of Art", "description": "One of the world's largest and most comprehensive art museums, featuring over 2 million works."},
    {"id": "4", "country": "Spain", "city": "Madrid", "museum": "Prado Museum", "description": "A national museum housing one of the finest collections of European art."},
    {"id": "5", "country": "Italy", "city": "Florence", "museum": "Uffizi Gallery", "description": "One of the most famous museums in the world, featuring Renaissance art masterpieces."},
    {"id": "6", "country": "Russia", "city": "Saint Petersburg", "museum": "Hermitage Museum", "description": "One of the largest and oldest museums in the world, founded by Catherine the Great."},
    {"id": "7", "country": "Germany", "city": "Berlin", "museum": "Pergamon Museum", "description": "Famous for its archaeological collections, including the Pergamon Altar."},
    {"id": "8", "country": "Netherlands", "city": "Amsterdam", "museum": "Rijksmuseum", "description": "National museum dedicated to Dutch arts and history, featuring works by Rembrandt."},
    {"id": "9", "country": "United States", "city": "Washington D.C.", "museum": "Smithsonian National Air and Space Museum", "description": "The world's largest collection of historic aircraft and spacecraft."},
    {"id": "10", "country": "Egypt", "city": "Cairo", "museum": "Egyptian Museum", "description": "Home to the world's largest collection of Pharaonic antiquities."},
    {"id": "11", "country": "Japan", "city": "Tokyo", "museum": "Tokyo National Museum", "description": "The oldest and largest museum in Japan, focusing on Japanese art and antiquities."},
    {"id": "12", "country": "Australia", "city": "Canberra", "museum": "National Museum of Australia", "description": "Explores the social history, culture, and stories of Australia."},
    {"id": "13", "country": "China", "city": "Beijing", "museum": "National Museum of China", "description": "The most visited museum in the world, showcasing Chinese history and culture."},
    {"id": "14", "country": "Mexico", "city": "Mexico City", "museum": "National Museum of Anthropology", "description": "The world's largest and most comprehensive pre-Columbian Mexican art collection."},
    {"id": "15", "country": "India", "city": "New Delhi", "museum": "National Museum", "description": "Houses a vast collection of artifacts representing India's rich cultural heritage."},
    {"id": "16", "country": "Brazil", "city": "Rio de Janeiro", "museum": "Museum of Tomorrow", "description": "A science museum exploring sustainability and the future of the planet."},
    {"id": "17", "country": "Canada", "city": "Ottawa", "museum": "Canadian Museum of History", "description": "Explores Canadian history and indigenous cultures."},
    {"id": "18", "country": "Greece", "city": "Athens", "museum": "Acropolis Museum", "description": "Houses artifacts from the Acropolis archaeological site."},
    {"id": "19", "country": "Turkey", "city": "Istanbul", "museum": "Istanbul Archaeological Museums", "description": "A complex of three museums with an extensive collection of archaeological artifacts."},
    {"id": "20", "country": "South Africa", "city": "Cape Town", "museum": "Iziko South African Museum", "description": "The oldest museum in South Africa, focusing on natural and cultural history."}
]

# Función para insertar definiciones
def insert_definitions():
    for definition in definitions:
        table.put_item(Item=definition)  # Uso correcto de put_item
    print("Museums inserted successfully!")

# Ejecutar la función
insert_definitions()