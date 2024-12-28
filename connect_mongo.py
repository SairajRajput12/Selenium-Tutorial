from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongo db url"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the database
db = client['Sample_d'] 

# Access the collection within the database
trends = db['Sample_c']

# Document to be inserted
document = {
    'id': "1", 
    'trends': {
        '1': 'Australia vs England', 
        '2': '2025 is coming...'
    },
    'ip_address': '192.168.1.100:8080'
}

# Insert the document
insert_doc = trends.insert_one(document)

print(f"Inserted document ID: {insert_doc}")

# Close the client
client.close()
