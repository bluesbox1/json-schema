import json
from genson import SchemaBuilder

builder = SchemaBuilder()
with open('./source.json', 'r') as f:
    datastore = json.load(f)
    builder.add_object(datastore )

builder.to_schema()
json_schema = builder.to_json(indent=2)
print(json_schema)

f = open("./schema.json", "w")
f.write(json_schema)
f.close()