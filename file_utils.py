import json

def save(filename, list):
    try:
        with open(filename, 'w') as f:
            json.dump(list, f, indent=4)
    except:
        print("\nErro: não foi possível guardar o ficheiro!\n")

def load(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except:
        return []
    else:
        return data