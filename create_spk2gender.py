carpeta = input()
texto = ""
if carpeta=="train":
	texto="""erick m
gambito m
gio m
jake m
jewel f
luis m
oropeza m
rod m"""
else:
	texto="""jess f"""

archivo = open("data/"+carpeta+"/spk2gender","w")
archivo.write(texto)
archivo.close()