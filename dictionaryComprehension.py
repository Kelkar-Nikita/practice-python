persons = [
    {"name": "alice", "title": "Data software"},
    {"name": "nikita", "title": "other software", "number":"97784856486"},
    {"name": "teju", "title": "new software"},
    {"name": "bob", "title": "Data Hardware"},
]

dataPersons = {p["name"]:p["title"] for p in persons if "Data" in p["title"]}
print(dataPersons)
