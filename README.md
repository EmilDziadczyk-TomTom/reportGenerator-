# reportGenerator-
Test repository to check the possibility of automating reporting tools
Added one script listLayers.py to easily check a number of layers with specific parent or subscriptin. 


1. listLayers.py - script finds and lists all layers that have layer with layer_ID as parent or subscription
How to use it: puthon3 listLayers.py layer_ID 

2. showLayerContact.py - list layer IDs and contacts from registry.json, and list layer descriptions and licences. A parameter licence is optional
   How to use it:
   - showLayerContact.py --layer_ids 666 667
   - showLayerContact.py --layer_ids 666 667 --licence ODbL



Next steps:
- add configuration to list contacts in proper format
- add integration with github so there is no need for copying registry.json
