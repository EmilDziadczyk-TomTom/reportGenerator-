import json

# Read JSON data from the input file
with open('input.json', 'r') as file:
    data = json.load(file)

# Extract and list unique contacts
unique_contacts = set()
for layer in data["layers"]:
    unique_contacts.update(layer.get("contact", []))

# Print the list of unique contacts
print("List of Unique Contacts:")
for contact in unique_contacts:
    print(contact)
