# LinkmailLensApi

An unofficial API for `Google Lens` created by me.

# ES
### Características
Por ahora su funcionalidad es buscar la fuente de la imagen y no resultados similares.

# EN
### Features
Currently, its functionality is limited to searching for the source of an image, not similar results.

---

# Uso / Usage

### ES: Clonar el repositorio:
```sh
https://github.com/Linkmail16/linkmailLensApi
```

### EN: Clone the repository:
```sh
https://github.com/Linkmail16/linkmailLensApi
```

---

### Uso / Usage:

#### ES: Ejemplo en Python:
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

#### EN: Python Example:
```python
from linkmailLensApi import lenSearchUrl
url = input("URL: ")
len = lenSearchUrl(url) # call the function to search for the image source
print(len.reply) # to display results in json
print(len.statusCode) # to display the request status
print(len.token) # to display the image token
print(len) # default
```

* A file named `data.json` will always be saved, as the responses are often very large and may not fit in the console. Saving it in a file helps avoid issues (in my opinion).
