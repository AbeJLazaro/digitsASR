import os

carpeta = input()
texto = ""
path = "/home/abelazaro/kaldi/egs/digits/digits_audio/"+carpeta+"/"

for name in os.listdir("digits_audio/"+carpeta):
	for record in os.listdir("digits_audio/"+carpeta+"/"+name):
		texto+= name+"_"+record[:-4]+" "+path+name+"/"+record+"\n"

archivo = open("data/"+carpeta+"/wav.scp","w")
archivo.write(texto)
archivo.close()