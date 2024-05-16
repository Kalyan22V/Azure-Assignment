from azure.storage.blob import BlobClient, BlobServiceClient
from flask import Flask, jsonify, request

app = Flask(__name__)

# Azure Blob Storage connection string
connection_string = "AZURE_CONNECTION_STRING"
container_name = "flask-container"

# @app.route('/')
# def index():
#     return "Flask App for Azure Blob Storage"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/', methods=['GET'])
def list_files():
    folder_name = request.args.get('folder_name')
   # print(folder_name, container_name)
    if not folder_name:
        return jsonify({'error': 'Folder name is required!'}), 400

    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        blobs_list = []
        for blob in container_client.list_blobs(name_starts_with=folder_name):
            print('bname ', blob.name)
            blobs_list.append(blob.name)
        print(blobs_list)
        return jsonify({'folder_name': folder_name, 'files': blobs_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
