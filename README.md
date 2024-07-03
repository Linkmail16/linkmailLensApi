# linkmailLensApi
Api no oficial de `Google lens` creada por mi.
# ES
### Características
Por ahora su funcionalidad es buscar la fuente de la imagen y no resultados similares.
# Uso
### Clonar el repositorio:
```sh
https://github.com/Linkmail16/linkmailLensApi
```
### Uso:
```python
from linkmailLensApi import lenSearchUrl
url = input("URL: ")
len = lenSearchUrl(url) # llamar a la funcion para buscar fuente de la imagen
print(len.reply) # para mostrar resultados en json
print(len.statusCode) # para mostrar el estado de la request
print(len.token) # para mostrar el token de la imagen
print(len) # por defecto
```
* Siempre se guardara un archivo llamado `data.json`, ya que las respuestas suelen ser muy grandes y no cabria en la consola, es mejor guardarlo en un archivo para evitar inconvenientes (segun mi opinion).
