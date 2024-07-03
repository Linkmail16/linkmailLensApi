import json
import re
def formatter22(ok):
 def eliminar_cadena_generic(te):
    pattern = r'",null,null,null,"generic".*'
    te = re.sub(pattern, '', te)
    return te

 def eliminar_cadena_generic2(te):
    pattern2 = r',true,null,null,.*'
    te = re.sub(pattern2, ']', te)
    return te
    

 with open("datos.json", "r") as file:
    te = file.read()

 te = te.replace('\\"', '"')
 te = te.replace('\\\\\\\\"', "'")
 te = te.replace('"[[', "[[")
 te = te.replace('activado"]]"', 'activado"]]]]]]]]')

 te = eliminar_cadena_generic(te)
 te = eliminar_cadena_generic2(te)

 te = eliminar_cadena_generic2(te)

 with open("datos.json", "w") as file:
    file.write(te)
 with open("datos.json", "r") as file:
    te2 = file.read()
    te2 = eliminar_cadena_generic2(te2)
 with open("datos.json", "w") as file:
    file.write(te2)


 try:
     json_data = json.loads(te)
 except json.JSONDecodeError as e:
     print(f"Error al decodificar JSON: {e}")
