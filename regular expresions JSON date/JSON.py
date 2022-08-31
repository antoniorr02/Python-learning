producto = {"nombre":"silla", "color":"blanco", "precio":100}

import json

estructura_json = json.dumps(producto)

print(estructura_json)

producto1 = json.loads(estructura_json)
print(producto1)