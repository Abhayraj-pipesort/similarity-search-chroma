# Similarity-search with ChromaDB

In this project, we'll go through the process of setting up ChromaDB, loading data from a JSON file, and performing simple queries to get similar products. You can expand upon this foundation to build more advanced data management systems for your own applications.

## Overview

ChromaDB is a vector database that can be used to store and query vector data, such as text embeddings and product data. It is a good choice for applications that need to perform fast and efficient search and retrieval of vector data.

## Getting Started

### Installation

To get started, you need to install ChromaDB using pip:

```bash
pip install chromadb
```

### Project Files

This project consists of the following files:

- `app.py`: The main Python script that demonstrates how to use ChromaDB to store and query data.
- `data.json`: A sample JSON file containing data for the project. You can replace it with your own data.
- `README.md`: This README file providing instructions and information about the project.

## Usage

### Step 1: Import the necessary libraries

```python
import chromadb
import json
```
We need to import the chromadb library to interact with ChromaDB and the json library to read and write JSON data.

### Step 2: Create a ChromaDB client

Next, we need to create a ChromaDB client:

```python
client = chromadb.PersistentClient(path="./chroma")
```

The PersistentClient class creates a persistent ChromaDB database that is stored on disk. We specify the path to the database directory as the path argument.

### Step 3: Create a collection to store the product data

Now, we need to create a collection to store the product data:

```python
collection = client.create_collection(name="product_data")
```

A collection is a object in ChromaDB. It is similar to a table in a relational database.

### Step 4: Load the product data from the JSON file

Next, we need to load the product data from the JSON file:

```python
with open("data.json", "r") as f:
    json_data = json.load(f)
```

The open() function opens the JSON file for reading. The json.load() function reads the JSON data from the file and loads it into a Python object.

### Step 5: Extract the unique product IDs and JSON strings

Next, we need to extract the unique product IDs and JSON strings from the product data:

```python
unique_ids = []
json_string_objects = []

for json_object in json_data:
    product_id = json_object["id"]
    unique_ids.append(product_id)

    json_string_object = json.dumps(json_object)
    json_string_objects.append(json_string_object)
```
We use a for loop to iterate over the product data and extract the product ID and JSON string for each product. We then add the product ID and JSON string to their respective lists.

### Step 6: Save the product data to the ChromaDB collection

Now, we need to save the product data to the ChromaDB collection:

```python
saved_collection = client.get_collection(name="product_data")

saved_collection.add(documents=json_string_objects, ids=unique_ids)
```
First we will get our created collection from disc, The get_collection() method returns a reference to the specified collection. The add() method adds the product data to the collection. We specify the JSON strings and product IDs as the documents and ids arguments, respectively.

### Step 7: Query the product data

Now, we can query the product data:

```python
results = saved_collection.query(query_texts=["smartphone case"], n_results=2)
```
The query() method performs a text search on the collection. We specify the query text as the query_texts argument. We also specify the number of results to return as the n_results argument.

### Step 8: Print the results

Finally, we can print the results:

```python
print(results)
```

### Output

Here is our output

```python
{
  "ids": [["12", "11"]],
  "distances": [[0.8864764754956473, 1.2108526876760022]],
  "metadatas": [[null, null]],
  "embeddings": null,
  "documents": [
    {
      "id": "12",
      "name": "Phone Case",
      "description": "A protective phone case designed to safeguard your smartphone from drops and impacts.",
      "price": "19.99"
    },
    {
      "id": "11",
      "name": "Screen Protector",
      "description": "A high-quality screen protector to keep your smartphone's display safe.",
      "price": "9.99"
    }
  ]
}
```
