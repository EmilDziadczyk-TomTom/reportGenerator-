import argparse
import json

# Setup command-line arguments
parser = argparse.ArgumentParser(description='Process specific value.')
parser.add_argument('specific_value_parents', type=int, help='The specific value for parents')
args = parser.parse_args()

specific_value_subscriptions = [6]
nbr_of_layers = 0
nbr_of_printed_layers=0

# read json file
with open('registry.json', 'r') as f:
    data = json.load(f)

for layer in data['layers']:
    nbr_of_layers=nbr_of_layers+1
    if args.specific_value_parents in layer['parents'] or args.specific_value_parents in layer['subscriptions']:
        nbr_of_printed_layers=nbr_of_printed_layers+1
        print(f"Layer ID: {layer['layer_id']}, Description: {layer['description']}")

print(f"===================================================")
print(f"Number of all layers: {nbr_of_layers}")
print(f"Number of printed layers: {nbr_of_printed_layers}")
print(f"===================================================")

