import os

carpeta = input()
texto = ""

for name in os.listdir("digits_audio/"+carpeta):
	for record in os.listdir("digits_audio/"+carpeta+"/"+name):
		texto+= name+"_"+record[:-4]+" "+name+"\n"

archivo = open("data/"+carpeta+"/utt2spk","w")
archivo.write(texto)
archivo.close()