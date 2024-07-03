import json
def formatter22(ok):
 with open("datos.json", "r") as file:
     te = file.read()
 te = te.replace('\\"', '"')
 te = te.replace('\\\\\\\\"', "'")
 te = te.replace('"[[', "[[")
 te = te.replace('activado"]]"', 'activado"]]]]]]]]')

 with open("datos.json", "w") as file:
     file.write(te)

 json_data = json.loads(te)