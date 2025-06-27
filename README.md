# linkmailLensApi (MEJORADA)

## EN: Overview

A simple API to search images using Google Lens. This library allows you to find similar images or the original source of an image by providing a URL or a local file.

## ES: Descripción

Una API simple para buscar imágenes usando Google Lens. Esta biblioteca te permite encontrar imágenes similares o la fuente original de una imagen proporcionando una URL o un archivo local.

## EN: Installation

```bash
pip install linkmailLensApi
```

## ES: Instalación

```bash
pip install linkmailLensApi
```

## EN: Features

- Search by image URL
- Search by local image file
- Simplified and complete results
- Automatic extraction of URLs, titles, dates, and resolutions
- Get results as Python objects without saving files

## ES: Características

- Búsqueda por URL de imagen
- Búsqueda por archivo local de imagen
- Resultados simplificados y completos
- Extracción automática de URLs, títulos, fechas y resoluciones
- Obtener resultados como objetos Python sin guardar archivos

## EN: Usage

### Search by image URL

```python
from linkmailLensApi import lenSearchUrl

# Search by URL
image_url = "https://example.com/image.jpg"
matches = lenSearchUrl(image_url)

# See a summary of the results
print(matches)  # Shows basic information like number of results

# Get the list of found URLs
urls = matches.pages
for url in urls:
    print(url)

# Get results without saving to file
results = matches.response

# If you want to save results to a custom file:
import json
with open('my_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
```

### Search by local image

```python
from linkmailLensApi import lenSearchImg

# Search by local file
image_path = "path/to/your/image.jpg"
matches = lenSearchImg(image_path)

# Get detailed results as Python objects
results = matches.response

# Access specific information
for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Resolution: {result['resolution']}")
    print(f"Date: {result['date']}")
    print("---")
```

## ES: Uso

### Buscar por URL de imagen

```python
from linkmailLensApi import lenSearchUrl

# Buscar por URL
image_url = "https://ejemplo.com/imagen.jpg"
matches = lenSearchUrl(image_url)

# Ver un resumen de los resultados
print(matches)  # Muestra información básica como número de resultados

# Obtener la lista de URLs encontradas
urls = matches.pages
for url in urls:
    print(url)

# Obtener resultados sin guardar en archivo
resultados = matches.response

# Si quieres guardar los resultados en un archivo personalizado:
import json
with open('mis_resultados.json', 'w', encoding='utf-8') as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)
```

### Buscar por imagen local

```python
from linkmailLensApi import lenSearchImg

# Buscar por archivo local
image_path = "ruta/a/tu/imagen.jpg"
matches = lenSearchImg(image_path)

# Obtener resultados detallados como objetos Python
resultados = matches.response

# Acceder a información específica
for result in resultados:
    print(f"Título: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Resolución: {result['resolution']}")
    print(f"Fecha: {result['date']}")
    print("---")
```

## EN: Available Properties

Each results object provides the following properties:

- `matches.response` - Returns the simplified results as Python objects (doesn't save any files)
- `matches.realResponse` - Returns the complete results as Python objects (doesn't save any files)
- `matches.pages` - Returns only the URLs of all found results

## ES: Propiedades disponibles

Cada objeto de resultados proporciona las siguientes propiedades:

- `matches.response` - Devuelve los resultados simplificados como objetos Python (no guarda archivos)
- `matches.realResponse` - Devuelve los resultados completos como objetos Python (no guarda archivos)
- `matches.pages` - Devuelve solo las URLs de todos los resultados encontrados

## EN: Results Format

### Simplified results (response)

```json
[
  {
    "title": "Page title",
    "url": "https://example.com/original-image",
    "ping": "/url?sa=t&source=web&rct=j&...",
    "resolution": "1024 x 768",
    "date": "2 years ago",
    "source_icon": "data:image/png;base64,..."
  },
  {
    "title": "Another page with similar image",
    "url": "https://another-site.com/image",
    "ping": "/url?sa=t&source=web&rct=j&...",
    "resolution": "800 x 600",
    "date": null,
    "source_icon": "data:image/png;base64,..."
  }
]
```

## ES: Formato de los resultados

### Resultados simplificados (response)

```json
[
  {
    "title": "Título de la página",
    "url": "https://ejemplo.com/imagen-original",
    "ping": "/url?sa=t&source=web&rct=j&...",
    "resolution": "1024 x 768",
    "date": "hace 2 años",
    "source_icon": "data:image/png;base64,..."
  },
  {
    "title": "Otra página con imagen similar",
    "url": "https://otro-sitio.com/imagen",
    "ping": "/url?sa=t&source=web&rct=j&...",
    "resolution": "800 x 600",
    "date": null,
    "source_icon": "data:image/png;base64,..."
  }
]
```

## EN: Usage Examples

### Search and comparison of image sources

```python
from linkmailLensApi import lenSearchUrl

# Verify the original source of an image
image_url = "https://example.com/suspicious-image.jpg"
matches = lenSearchUrl(image_url)

# Get only URLs to verify sources
sources = matches.pages
if sources:
    print(f"Possible original sources found: {len(sources)}")
    for i, source in enumerate(sources, 1):
        print(f"{i}. {source}")
else:
    print("No matches found for this image")
```

### Saving results to a file

```python
from linkmailLensApi import lenSearchImg
import json

# Search for matches for a local image
image_path = "C:/Users/user/downloads/image.jpg"
matches = lenSearchImg(image_path)

# Get results as Python objects
results = matches.response

# Save complete results to a file
with open('search_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Filter results by date (only those with a date)
dated_results = [r for r in results if r["date"]]
print(f"Results with date: {len(dated_results)}")

# Save only dated results to a separate file
with open('dated_results.json', 'w', encoding='utf-8') as f:
    json.dump(dated_results, f, ensure_ascii=False, indent=2)
```

## ES: Ejemplos de uso

### Búsqueda y comparación de fuentes de imágenes

```python
from linkmailLensApi import lenSearchUrl

# Verificar la fuente original de una imagen
image_url = "https://ejemplo.com/imagen-sospechosa.jpg"
matches = lenSearchUrl(image_url)

# Obtener solo las URLs para verificar fuentes
sources = matches.pages
if sources:
    print(f"Posibles fuentes originales encontradas: {len(sources)}")
    for i, source in enumerate(sources, 1):
        print(f"{i}. {source}")
else:
    print("No se encontraron coincidencias para esta imagen")
```

### Guardar resultados en un archivo

```python
from linkmailLensApi import lenSearchImg
import json

# Buscar coincidencias para una imagen local
image_path = "C:/Users/usuario/descargas/imagen.jpg"
matches = lenSearchImg(image_path)

# Obtener resultados como objetos Python
resultados = matches.response

# Guardar resultados completos en un archivo
with open('resultados_busqueda.json', 'w', encoding='utf-8') as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

# Filtrar resultados por fecha (solo los que tienen fecha)
resultados_con_fecha = [r for r in resultados if r["date"]]
print(f"Resultados con fecha: {len(resultados_con_fecha)}")

# Guardar solo los resultados con fecha en un archivo separado
with open('resultados_con_fecha.json', 'w', encoding='utf-8') as f:
    json.dump(resultados_con_fecha, f, ensure_ascii=False, indent=2)
```

## EN: Notes

- This API is not official and may stop working if Google changes its interface
- For optimal results, use clear images with good resolution
- The response time may vary depending on the complexity of the image
- The API returns Python objects directly; it doesn't save files automatically. You need to use `json.dump()` if you want to save results to files.

## ES: Notas

- Esta API no es oficial y podría dejar de funcionar si Google cambia su interfaz
- Para resultados óptimos, usa imágenes claras y con buena resolución
- El tiempo de respuesta puede variar dependiendo de la complejidad de la imagen
- La API devuelve objetos Python directamente; no guarda archivos automáticamente. Necesitas usar `json.dump()` si quieres guardar los resultados en archivos.

## EN: Requirements

- Python 3.6 or higher
- Libraries: requests, beautifulsoup4, pillow

## ES: Requisitos

- Python 3.6 o superior
- Bibliotecas: requests, beautifulsoup4, pillow
