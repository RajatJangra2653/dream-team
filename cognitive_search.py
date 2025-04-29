from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

client = SearchClient(endpoint="<Your_Search_Endpoint>", index_name="<Your_Index>", credential=AzureKeyCredential("<Your_Search_Key>"))
results = client.search("project roadmap")