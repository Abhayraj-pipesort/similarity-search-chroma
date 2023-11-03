import chromadb
import json

client = chromadb.PersistentClient(path="./chroma")

collection = client.create_collection(name="product_data")

with open("data.json", "r") as f:
    json_data = json.load(f)

unique_ids = []
json_string_objects = []

for json_object in json_data:
    product_id = json_object["id"]
    unique_ids.append(product_id)

    json_string_object = json.dumps(json_object)
    json_string_objects.append(json_string_object)

saved_collection = client.get_collection(name="product_data")

results = saved_collection.query(
    query_texts=["smartphone case"],
    n_results=2
)

print(results)
