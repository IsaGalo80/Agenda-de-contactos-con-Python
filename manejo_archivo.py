def app():
#crear el archivo
    archivo = open('archivo.txt','w') # W ES DE ESCRITURA, SI NO EXISTE LO CREARA

#generar numeros en archivos
    for i in range(0, 20):
        archivo.write('etsa es la linea' + str(i) + "\r\n")

    #cerrar archivo
    archivo.close()


app()