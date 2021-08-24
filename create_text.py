import os

carpeta = input()
texto = ""
numbers = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

for name in os.listdir("digits_audio/"+carpeta):
	for record in os.listdir("digits_audio/"+carpeta+"/"+name):
		texto+= name+"_"+record[:-4]+" "+" ".join([numbers[x] for x in record[:-4].split("_")])+"\n"

archivo = open("data/"+carpeta+"/text","w")
archivo.write(texto)
archivo.close()