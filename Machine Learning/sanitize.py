import json
import os

path_to_hide1 = 'C:\\\\Users\\\\Admin\\\\Desktop\\\\Krish\\\\Projects\\\\Flyrank ML'
path_to_hide2 = 'C:\\Users\\Admin\\Desktop\\Krish\\Projects\\Flyrank ML'
path_to_hide3 = 'C:/Users/Admin/Desktop/Krish/Projects/Flyrank ML'
replacement = '/content/flyrank-ml-internship-starter'

def sanitize(obj):
    if isinstance(obj, str):
        return obj.replace(path_to_hide1, replacement).replace(path_to_hide2, replacement).replace(path_to_hide3, replacement)
    elif isinstance(obj, list):
        return [sanitize(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: sanitize(v) for k, v in obj.items()}
    else:
        return obj

for nb in ['notebooks/01_first_look_and_discovery.ipynb', 'notebooks/02_your_first_readable_model.ipynb']:
    with open(nb, 'r', encoding='utf-8') as f:
        d = json.load(f)
    
    d = sanitize(d)
    
    with open(nb, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=1)
