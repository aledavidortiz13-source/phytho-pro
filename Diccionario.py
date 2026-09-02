meme_dict = {
"CRINGE": "Algo raro o embarazoso",
"LOL": "Algo gracioso",
"ROFL": "Algo muy gracioso",
"SHEESH": "Expresión de sorpresa o desaprobación",
"CREEPY": "Algo que da miedo o es inquietante",
"GG": "Buen juego"
}

print("¡Hola! Bienvenido al Meme Dictionary ")
print("Escribe una palabra en MAYÚSCULAS para conocer su significado.")

while True:
word = input("Escribe una palabra: ")

if word in meme_dict:
print("Significado:", meme_dict[word])
else:
print("Esa palabra no está en el diccionario ")
