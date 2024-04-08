import argparse
import json
import requests

# setup command-line arguments
parser = argparse.ArgumentParser(description='Process a list of layer_ids.')
parser.add_argument('--layer_ids', nargs='+', type=int, help='A list of layer_ids to match')
parser.add_argument('--licence', type=str, help='Filter by licence (optional)', nargs='?')
args = parser.parse_args()

# read json file
# url = "https://raw.githubusercontent.com/tomtom-internal/orbis-layer-registry/main/registry/registry.json"
# response = requests.get(url)
# data = json.loads(response.text)

# read json file localy
with open('registry.json', 'r') as f:
    data = json.load(f)

# filter layers
#filtered_layers = [layer for layer in data['layers'] if layer['layer_id'] in args.layer_ids]
#filtered_layers = [layer for layers in filtered_layers if (not args.licence or layer.get('licence') == args.licence)]
filtered_layers = [layer for layer in data['layers'] if (not args.layer_ids or layer['layer_id'] in args.layer_ids) and (not args.licence or layer.get('licence') == args.licence)]


# print filtered layers and their contact
print(f"===================================================")
nbrOfLayers = len(filtered_layers)
for layer in filtered_layers:
#     print(f"Layer ID: {layer['layer_id']}, Description: {layer['description']}")
#     print(f"Layer ID: {layer['layer_id']}, Contact: {layer['contact']}, Description: {layer['description']}")
#     print(f"Layer ID: {layer['layer_id']}, Contact: {layer['contact']}")
      print(f"Layer ID: {layer['layer_id']}, Description: {layer['description']}, Licence: {layer.get('licence', 'N/A')}")
print(f"Total number of layers: {nbrOfLayers}")
print(f"===================================================")
