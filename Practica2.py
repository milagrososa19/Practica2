import requests
import json

respuesta = requests.get("https://jsonplaceholder.typicode.com/users")
usuarios = respuesta.json()

print(json.dumps(usuarios, indent=2))
print("Cantidad de usuarios:", len(usuarios))
for usuario in usuarios:
    print(usuario["id"], usuario["name"], "-", usuario["email"], "-", usuario["address"]["city"])
numero = input("Ingresá el número de usuario: ")

respuesta = requests.get("https://jsonplaceholder.typicode.com/posts?userId=" + numero)
posts = respuesta.json()

for post in posts:
    print(post["title"])
respuesta = requests.get("https://jsonplaceholder.typicode.com/usuarioss")

print("Código de respuesta:", respuesta.status_code)

if respuesta.status_code == 200:
    print("La solicitud salió bien")
elif respuesta.status_code == 404:
    print("No se encontró la dirección")
respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
comentarios = respuesta.json()

# Preguntas
# 1) Devuelve los datos en un formato que Python puede utilizar. En este caso, devuelve una lista de diccionarios porque hay varios usuarios con diferentes datos.
# 2)El código 200 significa que la solicitud se realizó correctamente. El código 404 significa que no se encontró la dirección solicitada.