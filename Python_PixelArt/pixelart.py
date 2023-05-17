from json import load
from msilib import MSIDBOPEN_READONLY
import re
from subprocess import list2cmdline
import numpy as np
from PIL import Image

# Funciones #####################################################################

'''
def ancho():Busca el ancho de la matriz a partir de la primera linea, pasando por filtros de errores.

Parametros:
    lista_errores (str): lista que contiene los errores encontrados hasta el momento

Retorno:
    anch (int): numero entero con el ancho encontrado en la funcion
'''
def ancho(lista_errores):
    archivo = open("codigo.txt","r")
    linea= archivo.readline().strip()
    aux = split(linea.strip())
    aux.append(" ")
    if aux[1].isdigit() != True:
        error_write(linea,lista_errores)
        exit()
    elif aux[0] != "Ancho":
        error_write(linea,lista_errores)
    anch = int(aux[1])
    archivo.close()
    return anch

'''
def color(): Busca el color de fondo de la matriz, pasando por filtros de errores.

Parametros:
    lista_errores (str): lista que contiene los errores encontrados hasta el momento

Retorno:
    (Caso 1)linea (str): la linea encontrada está bien escrita, por ende retorna la linea en donde se encuentra el color.
    (Caso 2)linea (str): la linea encontrada está mal escrita, aun asi retorna la linea en donde se encuentra el color, pero antes se escribe el error.
'''
def color(lista_errores):
    archivo = open("codigo.txt","r")
    asegurar = 0
    for linea in archivo:
        if re.match("Color de fondo", linea) is not None:
            return linea.strip()
        elif asegurar == 1:
            error_write(linea,lista_errores)
            return linea.strip()
        asegurar = asegurar+1
    archivo.close()

'''
def color_lista(): Busca que el color sea el correcto dentro de la lista de colores, incluyendo el RGB. Si no lo encuentra, pinta de color negro (Momentaneamente).
    Esto sirve para que el programa no tenga errores y siga su fincionamiento. aun asi, existiendo un error, el programa no deberia imprimir una imagen.

Parametros:
    clr (str): Palabra con el color que se desea buscar su existencia
    linea (str): linea en la que se ubica el color que se desea buscar su existencia. Esto sirve en caso de que exista un error, para guardarlo en la lista de errores.
    lista_errores (str): lista que contiene los errores encontrados hasta el momento

Retorno:
    lista (int): lista de tipo entero, que guarda los numeros que describen cada color.
'''
def color_lista(clr,linea,lista_errores):
    if re.match("RGB", clr) is not None:
        aux = re.split(",", clr[4:-1])
        lista = [int(aux[0]),int(aux[1]),int(aux[2])]
    elif re.fullmatch("Blanco",clr) is not None:
        lista = [255,255,255]
    elif re.fullmatch("Rojo",clr) is not None:
        lista = [255,0,0]
    elif re.fullmatch("Verde",clr) is not None:
        lista = [0,255,0]
    elif re.fullmatch("Azul",clr) is not None:
        lista = [0,0,255]
    elif re.fullmatch("Negro",clr) is not None:
        lista = [0,0,0]
    else:
        error_write(linea.strip(),lista_errores)
        lista = [0,0,0]
    return lista

'''
def MatrizAImagen(): A partir de la matriz final que se obtiene, se genera una imagen de tipo ".png".

Parametros:
    matriz (int): matriz que en cada coordenada contiene los colores correctos despues de repasar las intrucciones indicadas.
    filename (str): el nombre que se le desea poner a la imagen.

Retorno:
    
'''
def MatrizAImagen(matriz, filename='pixelart.png', factor=10):
    img = Image.fromarray(matriz, 'RGB')
    N = np.shape(matriz)[0]
    img = img.resize((N*10, N*10), Image.Resampling.BOX)
    img.save(filename)  

'''
def pintar(): a partir de los parametros indicados y de la posicion actual en la que se encuentra, pinta la coordenada del color indicado.

Parametros:
    columna (int): posicion entera con la posicion actual de la columna.
    fila (int): posicion entera con la posicion actual de la fila.
    color (int): lista con los numeros que identifican a cada color.
    matriz (int): matriz que en cada coordenada contiene los colores correctos despues de repasar las intrucciones indicadas.

Retorno:
    matriz (int): matriz que en cada coordenada contiene los colores correctos despues de haber pintado la coordenada.
'''
def pintar(columna,fila,color,matriz):
    matriz[fila,columna] = color
    return matriz

'''
def derecha(): depende del modo en que esté actualmente, la dirección en la que mira cambiará.

Parametros:
    modo (int): lista con los modos de cada posicion. Si está en el eje x, cambiará uno de los parametros, así mismo con el eje y. Estos sirven para saber hacia donde avanzar posteriormente.
        Este se explica en los comentarios dejados en la misma funcion.
Retorno:
    modo (int): dependiendo de la posicion que se miraba antes de la función, cambiará uno de los parametros para saber cuál será la dirección en que se mirará ahora.
'''
def derecha(modo):
    modo[2] = modo[2]*(-1)
    if modo[2] == -1:
        #Se trabajará el en eje y
        if modo[0] == 1: #Si la posicion de x es positiva
            #se trabaja en la posicion inferior de y
            modo[1] = 1
        else:#Si la posicion de x es negativa
            #se trabaja en la posicion superior de y
            modo[1] = modo[1]*(-1)
    else:
        #se trabajará en el eje x
        if modo[1] == 1:#Si la posicion de y es inferior
            #se trabaja en la posicion derecha de x
            modo[0] = modo[0]*(-1)
        else:#Si la posicion de y es superior
            #se trabaja en la posicion izquierda de x
            modo[0] = 1
    return modo

'''
def izquierda(): depende del modo en que esté actualmente, la dirección en la que mira cambiará.

Parametros:
    modo (int): lista con los modos de cada posicion. Si está en el eje x, cambiará uno de los parametros, así mismo con el eje y. Estos sirven para saber hacia donde avanzar posteriormente.
        Este se explica en los comentarios dejados en la misma funcion.
Retorno:
    modo (int): dependiendo de la posicion que se miraba antes de la función, cambiará uno de los parametros para saber cuál será la dirección en que se mirará ahora.
'''
def izquierda(modo):
    modo[2] = modo[2]*(-1)
    if modo[2] == -1:
        #Se trabajará el en eje y
        if modo[0] == 1: #Si la posicion en x es positiva
            #se trabaja en la posicion superior de y
            modo[1] = modo[1]*(-1)
        else:#Si la posicion de x es negativa
            #se trabaja con la posicion inferior de y
            modo[1] = 1
            
    else:
        #Se trabajará en el eje x
        if modo[1] == 1: #Si la posicion de y es inferior
            #se trabaja en la posicion izquierda de x
            modo[0] = 1
        else: #Si la posicion de y es superior
            #se trabaja en la posicion derecha de x
            modo[0] = modo[0]*(-1)
    return modo

'''
def avanzar(): dependiendo del modo, la posicion de la matriz avanzará las casillas indicadas en las intrucciones, cambiando así la posición en que se ubicaba.

Parametros:
    pos (int): lista con la posicion actual dentro de la matriz.
    modo (int): lista con los modos de cada posicion. Si está en el eje x, cambiará uno de los parametros, así mismo con el eje y.
    n (int): entero con la cantidad de veces que debe avanzar en la dirección que se está mirando (depende del modo la direccion)
    linea (str): linea en la que se encuentra la instruccion, en caso de error se ocupará.
    lista_errores (str): lista con los errores hasta el momento.

Retorno:
    pos (int): lista con la posicion actual posterior de ser actualizada por la funcion.
'''
def avanzar(pos, modo, n, linea,lista_errores):
    anch = ancho(lista_errores)
    if modo[2] == 1: #se mueve en el eje x
        numero = n*modo[0]
        pos[0] = pos[0] + numero
        if pos[0] >= anch or pos[0] < 0:
            errores.write("Error, en las instrucciones se salio del borde:"+"\n"+linea)
            exit()
    else: #se mueve en el eje y
        numero = n*modo[1]
        pos[1] = pos[1] + numero
        if pos[1] >= anch or pos[1] < 0:
            errores.write("Error, en las instrucciones se salio del borde"+"\n"+linea)
            exit()
    return pos

'''
def repetir(): si en las instrucciones encuentra la palabra repetir, las instrucciones que abarcan el repetir entran a la funcion para generarlas la cantidad de veces pedida.

Parametros:
    lista (str): lista con las lineas que se desean repetir
    n (int): entero con la cantidad de veces que se desea repetir las intrucciones de la lista
    pos (int): lista con la posicion actual dentro de la matriz.
    matriz (int): matriz que en cada coordenada contiene los colores correctos despues de repasar las intrucciones indicadas.
    modo (int): lista con los modos de cada posicion. Si está en el eje x, cambiará uno de los parametros, así mismo con el eje y.
    errores (str): archivo en el que se desea escribir los errores (en caso de existir).
    lista_errores (str): lista con los errores hasta el momento.

Retorno:

'''
def repetir(lista, n, pos, matriz, modo, errores, lista_errores):
    x=0
    lrg=len(lista)
    rep = False
    while x<n:
        i=0
        while i<lrg:
            if re.match("Repetir", lista[i]) is not None or rep == True:
                lista_aux = split(lista[i].strip())
                largo = len(lista_aux)
                if lista_aux[0] == "Repetir":
                    if lista_aux[2] != "veces":
                        errores.write(lista[i]+"\n")
                        exit()
                    elif lista_aux[1].isdigit() != True:
                        errores.write(lista[i]+"\n")
                        exit()
                if lista_aux[-1] == "}" and largo>1 and rep == False:
                    str = " ".join(lista_aux[4:-1])
                    lista_aux2=[str]
                    repetir(lista_aux2,int(lista_aux[1]),pos,matriz,modo,errores,lista_errores)
                else:
                    if lista_aux[0] != "}" and rep == False:
                        m = int(lista_aux[1])
                        lista = lista_aux[4:-1]
                        rep = True
                    elif lista_aux[0] != "}" and rep == True:
                        lista.append(lista[i].strip())
                    elif lista_aux[0] == "}":
                        rep = False
                        repetir(lista,m,pos,matriz,modo,errores,lista_errores)
            else:
                aux = split(lista[i].strip())
                aux.append(" ")
                j=0
                lrg2=len(aux)
                while j<lrg2:
                    instruccion = aux[j]
                    if instruccion == "Pintar": #Si la instruccion es pintar, pintará el color de la siguiente posicion
                        pintar(pos[0],pos[1],color_lista(aux[j+1],lista[i],lista_errores),matriz)
                    elif instruccion == "Avanzar":
                        if aux[j+1].isdigit() == True:
                            av = int(aux[j+1])
                        else:
                            av = 1
                        avanzar(pos,modo,av,lista[i],lista_errores)
                    elif instruccion == "Izquierda":
                        izquierda(modo)
                    elif instruccion == "Derecha":
                        derecha(modo)
                    else:
                        error_escritura(instruccion,lista[i],lista_errores)
                    j=j+1
            i=i+1
        x=x+1

'''
def error_escritura(): a partir de filtros, busca errores de escritura existentes. en caso de que existan, se guarda la linea en la lista de errores.

Parametros:
    palabra (str): palabra la cual se desea comprobar que no exista error.
    linea (str): linea en la que se encuentra la instruccion, en caso de error se ocupará.
    lista_errores (str): lista con los errores hasta el momento.

Retorno:
    Retorna nada en caso de que la palabra no de error, esto sirve para que no se escriba en la listra de errores.
'''
def error_escritura(palabra,linea,lista_errores):
    if palabra == "Blanco":
        return
    elif palabra == "Negro":
        return
    elif palabra == "Azul":
        return
    elif palabra == "Verde":
        return
    elif palabra == "Rojo":
        return
    elif palabra[0:3] == "RGB":
        return
    elif palabra == " ":
        return
    else:
        error_write(linea,lista_errores)

'''
def error_write(): funcion en la cual se escriben los errores dentro de la lista. En caso de la linea ya se haya ingresado, no se escribirá (Esto ocurre en los anidamientos).

Parametros:
    linea (str): linea en la que se encuentra la instruccion, en caso de error se ocupará.
    lista_errores (str): lista con los errores hasta el momento.

Retorno:

'''
def error_write(linea,lista_errores):
    flag = False
    if len(lista_errores) == 0:
        lista_errores.append(linea)
    for x in lista_errores:
        if linea == x:
            flag = True
    if flag == False:
        lista_errores.append(linea)

'''
def split(): funcion que separa una linea por cada " " que exista, estas palabras serán guardadas en una lista para su posterior uso.

Parametros:
    linea (str): linea en la que se encuentran las intrucciones sin separar.

Retorno:
    lista (str): lista con cada instruccion separada, para su posterior uso.
'''
def split(linea):
    i = 0
    linea = linea + " "
    largo = len(linea)
    lista=[]
    palabra = ""
    while(i<largo):
        if(linea[i] != " "):
            palabra=palabra+linea[i]
        else:
            lista.append(palabra)
            palabra = ""
        i=i+1
    return lista

# Main #########################################################################
archivo = open("codigo.txt","r")
errores = open("errores.txt","w")
lista_errores = []
pos=[0,0]
anch = int(ancho(lista_errores))
color_fondo = color(lista_errores)
coloraux = split(color_fondo)
list_color = color_lista(coloraux[-1],color_fondo,lista_errores)
matriz = np.zeros((anch,anch,3), dtype=np.uint8) #Se crea la matriz de nxn, generada por matriz de nx3
matriz[:,:,:] = (list_color[0],list_color[1],list_color[2]) #Se le ingresan los colores a las matrices nx3

#Recorrer las instrucciones
rep = False
modo=[1,1,1] #La primera posicicon es el modo de x, la segunda es el modo de y, y la tercera si debemos trabajar en x o y
for linea in archivo:
    if (re.match("Color de fondo", linea) is None) and (re.match("Ancho", linea) is None):
        if re.match("Repetir", linea) is not None or rep == True:
            lista_inst = split(linea.strip())
            largo=len(lista_inst)
            #Comparar la syntaxis del repetir
            if lista_inst[0] == "Repetir":
                if lista_inst[2] != "veces":
                    errores.write(linea+"\n")
                    exit()
                elif lista_inst[1].isdigit() != True:
                    errores.write(linea+"\n")
                    exit()

            if lista_inst[-1] == "}" and largo>1 and rep == False:
                str = " ".join(lista_inst[4:-1])
                lista_aux2=[str]
                repetir(lista_aux2,int(lista_inst[1]),pos,matriz,modo,errores,lista_errores)
            else:
                if lista_inst[0] != "}" and rep == False:
                    m = int(lista_inst[1])
                    lista = lista_inst[4:-1]
                    rep = True
                elif lista_inst[0] != "}" and rep == True:
                    lista.append(linea.strip())
                elif lista_inst[0] == "}":
                    rep = False
                    repetir(lista,m,pos,matriz,modo,errores,lista_errores)
        elif rep == False:
            lista_inst = split(linea.strip())
            i=0
            largo=len(lista_inst)
            lista_inst.append(" ")
            while i<largo:
                instruccion = lista_inst[i]
                if instruccion == "Pintar": #Si la instruccion es pintar, pintará el color de la siguiente posicion
                    pintar(pos[0],pos[1],color_lista(lista_inst[i+1],linea,lista_errores),matriz)
                elif instruccion == "Avanzar":
                    if lista_inst[i+1].isdigit() == True:
                        n = int(lista_inst[i+1])
                    else:
                        n = 1
                    avanzar(pos,modo,n,linea,lista_errores)
                elif instruccion == "Izquierda":
                    izquierda(modo)
                elif instruccion == "Derecha":
                    derecha(modo)
                i=i+1
if len(lista_errores) == 0:
    errores.write("No hay errores!")
    MatrizAImagen(matriz) #Se crea la imagen
else:
    i=0
    while i<len(lista_errores):
        errores.write(lista_errores[i]+"\n")
        i=i+1

archivo.close()
errores.close()