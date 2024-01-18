import argparse
import json
import requests

# setup command-line arguments
parser = argparse.ArgumentParser(description='Process a list of layer_ids.')
parser.add_argument('--layer_ids', nargs='+', type=int, help='A list of layer_ids to match')
args = parser.parse_args()

# read json file
# url = "https://raw.githubusercontent.com/tomtom-internal/orbis-layer-registry/main/registry/registry.json"
# response = requests.get(url)
# data = json.loads(response.text)

# read json file localy
with open('registry.json', 'r') as f:
    data = json.load(f)

# filter layers
filtered_layers = [layer for layer in data['layers'] if layer['layer_id'] in args.layer_ids]

# print filtered layers and their contact
print(f"===================================================")

for layer in filtered_layers:
     print(f"Layer ID: {layer['layer_id']}, Description: {layer['description']}")
#      print(f"Layer ID: {layer['layer_id']}, Contact: {layer['contact']}")

print(f"===================================================")
