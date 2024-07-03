import os
import requests
import urllib.parse
import json
import subprocess
from .formatter1 import formatter11
from .formatter2 import formatter22
class Respuesta:
 def __init__(self, token, reply, statusCode):
        self.token = token
        self.reply = reply
        self.statusCode = statusCode
        def __str__(self):
         return f""

def lenSearchUrl(url):

 token = []
 reply = []
 statusCode = []
 url = url
 if not url:
     noDataProvide = "No data provided"
     return noDataProvide
 if not url.startswith("http"):
     noUrlProvide = "No url provided"
     return noUrlProvide
 headers = {
    'Host': 'lens.google.com',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept-Language': 'es-ES',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.google.com/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=0, i',
    # 'Cookie': 'AEC=AQTF6HxBmt_JCEihpxnEH5pi5S3ZDSJQRTPG3w6p_clUTjV484CCRjQZiw; OGPC=19037049-1:; NID=515=nfo6mGi_VLad-Fb6reFWNLJns42KwsFqv-5YDiDg4XDL347-RT4WSfvG5sVue9cHUMmp8WXVXKP4wR2hLepWtyQgd3nCNu_xEdJ2ZUMpfCHChHxIPBDeVW1v-DMu-sRxsMJmfL2kKtR3878OnVstSVSbRmr5IR39bZTeiRpFyJIQYtMfvuNHQ3AaJZQefQ; OGP=-19037049:',
}

 params = {
    'url': url,
    'hl': 'es-CO',
    're': 'df',
    'st': '1719890323700',
    'vpw': '753',
    'vph': '772',
    'ep': 'gsbubu',
}

 response = requests.get('https://lens.google.com/uploadbyurl', params=params,  headers=headers, verify=True)
 with open("re.txt", "w") as file:
  file.write(str(response.text.encode('utf-8')))
  with open('re.txt', 'r') as archivo:
     contenido = archivo.read()
     indice = contenido.find("AF_dataServiceRequests")
     if indice != -1:
         rango_busqueda = contenido[indice:indice + 600]
         contador = 0
         inicio = 0
         while contador < 3:
             inicio = rango_busqueda.find('"', inicio)
             if inicio == -1:
                 break
             fin = rango_busqueda.find('"', inicio + 1)
             if fin == -1:
                 break
             tokenImg = rango_busqueda[inicio + 1:fin]
             contador += 1
             inicio = fin + 1

         if contador == 3:
             okpe = "okpe"
         else:
              print("No se encontró el token.")
     else:
         print("No se encontró el token.")


 tokenr = tokenImg
 

 cookies = {
    'AEC': 'AQTF6HxBmt_JCEihpxnEH5pi5S3ZDSJQRTPG3w6p_clUTjV484CCRjQZiw',
    'OGPC': '19037049-1:',
    'NID': '515=nfo6mGi_VLad-Fb6reFWNLJns42KwsFqv-5YDiDg4XDL347-RT4WSfvG5sVue9cHUMmp8WXVXKP4wR2hLepWtyQgd3nCNu_xEdJ2ZUMpfCHChHxIPBDeVW1v-DMu-sRxsMJmfL2kKtR3878OnVstSVSbRmr5IR39bZTeiRpFyJIQYtMfvuNHQ3AaJZQefQ',
    'OGP': '-19037049:',
    'OTZ': '7626439_76_76__76_',
}

 headers = {
    'Host': 'lens.google.com',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
    'X-Same-Domain': '1',
    'Accept-Language': 'es-ES',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
    'Sec-Ch-Ua-Arch': '""',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Sec-Ch-Ua-Full-Version': '""',
    'Sec-Ch-Ua-Platform-Version': '""',
    'Sec-Ch-Ua-Bitness': '""',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Wow64': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://lens.google.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://lens.google.com/',
    'Priority': 'u=1, i',
}

 params = {
    'rpcids': 'B7fdke',
    'source-path': '/search',
    'f.sid': '6261054257017883305',
    'bl': 'boq_lensfrontendapiserver_20240629.08_p0',
    'hl': 'es-CO',
    'opi': '89978449',
    'soc-app': '1',
    'soc-platform': '1',
    'soc-device': '1',
    '_reqid': '181164',
    'rt': 'c',
}

 tokenU = urllib.parse.quote(str(tokenr))
 data = f'f.req=%5b%5b%5b%22B7fdke%22%2c%22%5b%5b%5c%22665229652%5c%22%2c1%2c1%5d%2c%5bnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c%5b%5c%227ae26c8b-ffb2-400d-ae76-892c033eed3a%5c%22%5d%2c%5b%5c%22{tokenU}%5c%22%2c%5bnull%2cnull%2c512%2c512%5d%5d%5d%2c%5bnull%2cnull%2cnull%2cnull%2c3%2c%5b%5c%22es-419%5c%22%2cnull%2c%5c%22419%5c%22%2c%5c%22America%2fIndianapolis%5c%22%5d%2cnull%2cnull%2c%5bnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2c1%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2c1%2cnull%2cnull%2c1%5d%2c%5b%5bnull%2c1%2c1%2c1%2c1%2c1%2c1%2cnull%2cnull%2cnull%2c1%2c1%2c1%2c1%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2c1%2c1%2cnull%2c1%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2c0%2cnull%2cnull%2cnull%2c%5b5%2c6%2c2%5d%2cnull%2cnull%2cnull%2c1%2cnull%2c1%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2c1%2cnull%2cnull%2c1%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c0%2cnull%2c1%2cnull%2cnull%2cnull%2cnull%2c1%5d%5d%2c%5b%5b%5b7%5d%5d%5d%2cnull%2cnull%2cnull%2c26%2cnull%2cnull%2cnull%2c%5b753%2c772%5d%2c%5bnull%2c6%5d%2c%5bnull%2c14%5d%2cnull%2c%5b14%5d%2c%5b%5d%5d%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c%5c%22EkcKJDYwMWY0M2MwLTQ1NjMtNGRkMC04ZDIwLTJlZTYxMzA3ZDk3ZBIfa3c0bDNDUllPWlVUUUV1eDYxXzIwWEM4QUJRWUJ4aw%3d%3d%5c%22%2cnull%2cnull%2cnull%2cnull%2cnull%2c%5b%5bnull%2c%5b%5d%5d%2c%5bnull%2cnull%2cnull%2cnull%2cnull%2cnull%2c%5b%5c%223bf15275-18f5-4469-a6a1-6c1ed269b6ea%5c%22%5d%2c%5b%5c%22%2flens-web-standalone-prod%2fe3974979-2116-46b1-9e46-41cbc28c1f37%5c%22%2c%5bnull%2cnull%2c512%2c512%5d%5d%5d%5d%2cnull%2c%5c%22MjgxNTVFQTYtM0FDMS00M0ZDLTgwQzAtRDY1RDFCQjQ1RTlF%5c%22%5d%22%2cnull%2c%22generic%22%5d%5d%5d'
 response = requests.post(
     'https://lens.google.com/_/LensWebStandaloneUi/data/batchexecute',
     params=params,
     cookies=cookies,
     headers=headers,
     data=data, 
     verify=True,
)

 #print(response)
 statusCode = response
 if len(response.text) < 10000:
        print()
        return "No se pudo buscar la imagen"
 with open("re.txt", "w", encoding='utf-8') as file:
     file.write(response.text)



 formatter11(response)
 formatter22(response)


 with open("datos.json", 'r') as f:
  f = json.load(f)
  raw_data = str(f)

 raw_data = raw_data.replace("false", '"para todos"').replace("true", "+18")

 index = raw_data.find('"El desenfoque de SafeSearch está activado')
 if index != -1:
     raw_data = raw_data[:index]
     raw_data += ']]]]]]]]'
   # print(raw_data)

 try:

     raw_data = raw_data.replace('null', 'None')


     raw_data += ''

     data = eval(raw_data)

     def filter_strings(obj):
         if isinstance(obj, str):
             return obj
         elif isinstance(obj, list):
             return [filter_strings(item) for item in obj if isinstance(item, (str, list, dict))]
         elif isinstance(obj, dict):
             return {key: filter_strings(value) for key, value in obj.items() if isinstance(value, (str, list, dict))}
         return None

     filtered_data = filter_strings(data)

     formatted_data = json.dumps(filtered_data, indent=4)

     formatted_data = formatted_data.replace('None', 'null')
   # print(formatted_data)

     def format_recursive(data, indent=0, id_counter=[1]):
         result = []
         if isinstance(data, list):
             for index, item in enumerate(data, start=1):
                 if indent == 6 and index == 1:

                     result.extend(format_recursive(item, indent + 1, id_counter))
                 elif indent == 7:

                     formatted_item = format_recursive(item, indent + 1, id_counter)
                     result.append({"id": id_counter[0], "content": formatted_item})
                     id_counter[0] += 1
                 else:
                     result.extend(format_recursive(item, indent + 1, id_counter))
         elif isinstance(data, str):
             result.append(data)
         elif isinstance(data, dict):
             for key, value in data.items():
                 result.append({key: format_recursive(value, indent + 1, id_counter)})
         else:
             result.append(data)
        
         return result


     formatted_data_recursive = format_recursive(filtered_data)


     formatted_json = json.dumps(formatted_data_recursive, indent=2)
    # okkkkkkkkkkk
     with open("data.json", "w") as file:
         file.write(formatted_json)
     with open("data.json", 'r') as f:
      data = json.load(f)
     original_data = data
     formatted_data = []
    

     timestamp = original_data[0]
     entries = original_data[1:]
 
     for entry in entries:
      formatted_entry = {
        "timestamp": timestamp,
        "id": entry["id"],
        "content": {
            "image_url": entry["content"][0] if len(entry["content"]) > 0 else None,
            "page_title": entry["content"][1] if len(entry["content"]) > 1 else None,
            "site_name": entry["content"][2] if len(entry["content"]) > 2 else None,
            "logo_url": entry["content"][3] if len(entry["content"]) > 3 else None,
            "site_url": entry["content"][4] if len(entry["content"]) > 4 else None,
            "unknown_number": entry["content"][5] if len(entry["content"]) > 5 else None,
            "shortened_title": entry["content"][6] if len(entry["content"]) > 6 else None,
            "data1": entry["content"][7] if len(entry["content"]) > 7 else None
        }
     }
    
      if len(entry["content"]) > 8:
         formatted_entry["content"]["data2"] = entry["content"][8]
      else:
         formatted_entry["content"]["data2"] = None
    
      formatted_data.append(formatted_entry)


      formatted_json = json.dumps(formatted_data, indent=4)
     #print(formatted_json)

     with open("data.json", "w") as file:
         file.write(formatted_json)
     


 except SyntaxError as e:
     print(f"Error de sintaxis en el JSON: {e}")
 except Exception as e:
     print(f"Ocurrió un error: {e}")
 token = tokenr
 reply = formatted_json

 os.remove("datos.json")
 os.remove("re.txt")
 return Respuesta(token, reply, statusCode)

