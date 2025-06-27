from linkmailLensApiv2 import lenSearchUrl, lenSearchImg

# Ejemplo de uso con URL
image_url = "https://www.geometryamerica.xyz/uploads/26129447-4db6-4e61-86ca-0e88aa8ed3a4.webp"
matches_url = lenSearchUrl(image_url)
print(matches_url)
print(matches_url.pages)

# Ejemplo de uso con imagen local
image_path = "imagen.jpg"
matches_img = lenSearchImg(image_path)
print(matches_img)
print(matches_img.pages)