#Import Libries
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

#Initialize DefaultAzureCredential
def_credentials = DefaultAzureCredential()

#Set storage account name
STORAGE_ACCOUNT_NAME = "storageaccountazurea855"

#Set container name
CONTAINER_NAME="users-container"

#Set blob name
BLOB_NAME="users.txt"

#Initialize BlobClient
blob_client = BlobClient(
    credential=def_credentials,
    account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net.",
    container_name=CONTAINER_NAME,
    blob_name=BLOB_NAME
)

#Upload image to storage bucket
with open("storage/text.txt", "rb") as data:
    blob_client.upload_blob(data)