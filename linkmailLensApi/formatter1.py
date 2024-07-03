import json
import re
import subprocess
def formatter11(ok):

 def safe_to_json(data):
     try:
        return json.dumps(data, ensure_ascii=False)
     except (TypeError, OverflowError) as e:
        # print(f"Error al convertir a JSON: {e}")
         return None

 def save_json_to_file(data, filename):
     json_data = safe_to_json(data)
     if json_data is not None:
         try:
             with open(filename, 'w', encoding='utf-8') as file:
                 file.write(json_data)
            # print(f"Datos guardados en el archivo {filename}")
         except IOError as e:
             print(f"Error al guardar en el archivo {filename}")
     else:
         print("No se pudo convertir los datos a JSON. No se guardó ningún archivo.")


 #data = """[["wrb.fr","B7fdke","[[\"665229652\",1,1],[[null,[null,null,null,null,null,null,null,null,[null,null,[[\"No se encontraron páginas web ni imágenes duplicadas. Prueba con otra.\",[[\"https://www.gstatic.com/lens/cards/assets/image_provenance_failure.png\"],\"image_provenance_failure\"],null,null,null,[173181,null,0,\"173181.0\",-1,[173181],true],[null,null,null,null,false],null,7],true]]]]],null,null,null,null,[[null,true]],true,null,null,[],[\"CA0SCggBEgAY/cgKIABKBBACEANaEAOkmPVY+kN+gyTNrEHcrz5gAGgBeACCAUQKQAgDECQaFEFydHMgJiBFbnRlcnRhaW5tZW50Ih9BcnRzICYgRW50ZXJ0YWlubWVudC9UViAmIFZpZGVvLVIAwT0SAJoBBAgAEAA\\u003d\",null,\"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IvrTtCLV2bQi9Nq0IsHdtCKi3rQi5OC0IoDptCLr6bQi7Om0IrTqtCK49bQiufa0Is32tCLy9rQitve0Isb3tCLL+LQigf+0Ipv/tCLqgrUi/Ye1Iu+ItSKmirUi6ZS1IqCctSLpnbUisp+1IriftSKepbUizKa1IoOotSLetLUi2ri1Ir27tSKqvLUio721Iue9tSLSvrUioMC1IqXAtSLfwbUigcW1IszFtSLkxrUigMu1ItvPtSL14rUi1Oq1Ir/utSLl7rUig/S1Itj0tSKV9rUim/a1Itj2tSLY+LUi1P61Iv3+tSLZ/7Ui3oS2IqyFtiKdjL0ilY2+Is200CLN49os4+PaLIjw2iy38dos0vLaLP3y2izq9tosovjaLNi8/izCyoktobSLLaO0iy33r5Et+6+RLdP2mC2/2J0twdidLYbuqi36oa0t1/CxLfPwsS3v47Qt/961LZm4ty383p8vstagL6LYoC+X2aAvsdmgL4/aoC+K3aAv7+CgL47loC/f7qAv+e6gL8TvoC/X8KAvs/GgL4/0oC+49KAvivWgL5L1oC+n9aAvzfqgL9X7oC/H/KAvz/ygL+//oC/WgqEv4oKhL/eDoS+FhKEvu4WhL/eFoS+sh6Ev2omhL9SLoS/HjKEvho2hL5ONoS/jjqEvjpGhL6iSoS/VkqEvtpOhL56WoS+RtaIvtbWiL6C2oi/StqIvp7eiL/i4oi/+uKIvubmiL7u5oi/SuaIv37uiL5G8oi/bvKIvjr2iL6S/oi+uv6IvisCiL5XAoi+IwaIv3cGiL+/Coi/HxKIvycaiL8XIoi/myKIv68qiL/jLoi/qzKIvks2iL5vNoi+EzqIvwM6iL4XPoi+Iz6IvoNCiL8/Qoi+V0aIvn9GiL43Uoi+T1KIvltSiL5rUoi/q1KIvxNWiL8fVoi/X2KIv/NiiL77Zoi/f2qIvxNuiL+veoi+p36Ivq9+iL7bfoi/14KIvz+GiL8fkoi/H5aIv9+WiL9nmoi/t5qIvpueiL/Xnoi/77aIvjO6iL4nvoi+B8aIvovOiL87/oi+rgKMvoIGjL7ODoy+bhKMvq4WjL7uFoy/Ri6Mv1YujL5yMoy/qjaMvvo6jL7qPoy/1j6Mvx5KjL56Toy+ElKMvpJajL7aWoy/NlqMvn5ijL46aoy+snKMv5pyjL5egoy+7oqMvvKOjL/2toy+Rr6MvvbWjL5rHoy+dzaMviM6jL6jOoy+rzqMvo8+jL6rPoy+40aMv7dGjL5TSoy+u0qMvt9KjL+TUoy/01KMvwtWjL9jVoy/q16MvytmjL4zdoy/K6qMvzuyjL+Tsoy/r8aMvy9BoyciTEs3IkxKkgJ8ipu+CLZi2lS3XlJ4t+amtLcnCrS3XkLAtodu1LeOWuS0qgwPL0Gjjs8YH5/LIB/z0yAe198gH943JB4u5yQfdo5kTgaWZE/GlmRONppkTzqaZE4SnmRPZp5kT56eZE5OomRPpqJkT0KmZE+ypmROtqpkTyaqZE6qrmRO6q5kTkqyZE/np0xbc8NMWwJ3UFoDt1BbS99UWgunWFqL31xau6KsXtMToF9zq7SHMrvkh67aPIrTnsCLC67Ein/axIozxsiKy9bIiuZyzIqrxsyLH9bMiw4O0IsWjtCKtpbQilam0IqGvtCL4ubQit8a0ItbWtCLd3LQisd20IsHdtCK49bQiy/i0IsymtSLK4LUilei1Itj0tSKV9rUiuf21Iub9tSLZ/7UinYy9IpWNviLNtNAimbi3LY7loC/igqEv1IuhL+2YoS/MtaIvp7eiL9K5oi+uv6IvycaiL4TOoi/P0KIvk9SiL77Zoi/E26Ivz+GiL4zuoi+i86Ivm4SjL9GLoy+OmqMvo8+jL7jRoy+U0qMvt9KjL+TUoy/C16MvytmjL+vxoy8\\u003d\"],null,null,[],null,null,[[1,[[7,\"916443126824626\"],[55,\"916443145372437\"],[56,\"916443502922994\"],[47,\"916443126865166\"],[48,\"916443135343324\"],[57,\"916443502965388\"],[58,\"916443503286299\"],[2,\"916443503343536\",[\"665229652\",1,1]],[19,\"916443503343536\",[\"665229652\",1,1]],[8,\"916443503343536\"]]]],null,null,null,null,null,null,null,null,null,null,null,\"MAE\\u003d\",null,null,true,null,null,[2]]",null,null,null,"generic"]]"""
 with open('re.txt', 'r', encoding='utf-8') as file:
     data = file.read()
 def mostrar_despues_de_generic(texto):

     patron = r'El desenfoque de SafeSearch está activado(.*)'

     match = re.search(patron, texto, re.DOTALL)
     if match:

        texto_final = match.group(1)
        return texto_final
     else:

        return ""


 texto_original = data
 texto_modificado = mostrar_despues_de_generic(texto_original)
 #print(texto_modificado)
 texto_original = data.replace(texto_modificado, "")
 texto_original += '"]]'

 def mostrar_antes_del_patron(texto):
     patron = r'\[\[\\"[0-9]'

     match = re.search(patron, texto)
     if match:
         texto_final = texto[:match.start()]
         return texto_final
     else:

         return texto


 texto_modificado = mostrar_antes_del_patron(texto_original)
 #print(texto_modificado)
 texto_original = texto_original.replace(texto_modificado, "")
 texto_original = texto_original.replace('\\"', '"').encode('unicode_escape').decode('ascii').replace('\"', '"')
 save_json_to_file(texto_original, 'datos.json')

#
