import pyodbc
from datetime import date
#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    Revisar_cancion(): Revisa que las canciones no tengan mas de un artista. En caso de tener mas de un artista, pregunta cual deseas y lo guarda.
Paramatros: 
    lista: lista que contiene cada uno de los artista que realizo una cancion con el mismo nombre.
Retorno: lista2: lista que contiene el artista elegido.
"""
def Revisar_cancion(lista):
    largo = len(lista)
    lista2 = []
    if(largo > 1):
        flag = True
        while(flag == True):
            j=0
            print("\nEstos son los artistas que han creado la cancion " + lista[0][1] + ":\n")
            while(j<largo):
                print(lista[j][2])
                j += 1
            entrada = input("\nIngrese uno de los anteriores artistas: ")
            i=0
            while(i<largo and flag == True):
                if(entrada == (lista[i][2])[:-1]):
                    lista2.append([lista[i][0],lista[i][1],(lista[i][2])[:-1]])
                    flag = False
                i += 1
            if(len(lista2) == 0): print('Opcion indicada no valida. Vuelva a intentarlo.')
    else: lista2.append(lista[0])
    return lista2

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    Recorrer_Nombres(): en caso de que algun nombre contenga comillas (esto afecta al enviar informacion a sql), arregla el texto.
Paramatros: 
    palabra: palabra que contienen una o mas comillas.
Retorno: 
    aux: palabra que se le inserta una comilla junto a la existente para no ocacionar error.
"""
def Recorrer_Nombres(palabra):
    aux = ''
    for i in palabra:
        if(i == "\'"):
            aux = aux + "\'\'"
        else: aux = aux + i
    return aux

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    Menu_Principal(): Menu de interacciones el cual se repetirá hasta cerrar el programa desde la terminal. Dentro de esta funcion te lleva a cada uno de los menus de interacciones.
Paramatros: 
    -
Retorno:
    -
"""
def Menu_principal():
    flag = True
    while(flag == True):
        print("\nElige una de las siguientes opciones: \n\n (1) Mostrar reproduccion\n (2) Mostrar caciones favoritas\n (3) Reproducir una canción\n (4) Peak Position de un artista\n (5) Canciones escuchadas ultimamente\n (6) Buscar por artista\n (7) Ver TOP15 Artistas\n (8) Cerrar Usm-Spot")
        elecc = str(input(" \nOpcion a elegir: "))
        print('\n')
        if(elecc == '1'):#Listo
            ViewSongs()
        elif(elecc == '2'):#Listo
            FavSongs()
        elif(elecc == '3'):#Listo
            PlaySong()
        elif(elecc == '4'):
            PeakPosition()
        elif(elecc == '5'):
            Escuchadas_Ultimamente()
        elif(elecc == '6'):
            Search_Artist()
        elif(elecc == '7'):
            Top_15()
        elif(elecc == '8'):
            flag = False
        else:
            print('Opcion indicada no valida. Vuelva a intentarlo.')

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    FavSongs(): Menu de canciones favoritas, en el podrás ordenar la lista de distintas formas.
Paramatros: 
    -
Retorno:
    -
"""
def FavSongs():
    server = "DESKTOP-PH73MFC\SQLEXPRESS"
    database = "BD_Usm_Spot"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    
    archivo = open('BuscarFavorito.sql','r')
    data = archivo.read()
    cursor.execute(data)
    arreglo = cursor.fetchall()

    if(arreglo == []):
        print("No se han agregado canciones a tu lista de favoritos.")
    else:
        flag = True
        while(flag == True):
            print("Elige como deseas ordenar tus canciones: \n\n (1) Ordenar por fecha\n (2) Ordenar por nombre de cancion (A-Z)\n (3) Ordenar por nombre de cancion (Z-A)")
            elecc = str(input(' \nOpcion a elegir:'))
            print('\n')
            if(elecc == '1'):
                flag = False
                cursor.execute(  '''SELECT
                                        id, song_name, artist_name, fecha_agregada
                                    FROM
                                        lista_favoritos
                                    ORDER BY
                                        fecha_agregada ASC;''')
                arreglo = cursor.fetchall()
                for elemento in arreglo:
                    print('Cancion : ', elemento[1], ' |  Artista : ', elemento[2], ' |  Fecha guardado: ', elemento[3])
            elif(elecc == '2'):
                flag = False
                cursor.execute(  '''SELECT
                                        id, song_name, artist_name, fecha_agregada
                                    FROM
                                        lista_favoritos
                                    ORDER BY
                                        song_name ASC;''')
                arreglo = cursor.fetchall()
                for elemento in arreglo:
                    print('Cancion : ', elemento[1], ' |  Artista : ', elemento[2], ' |  Fecha guardado: ', elemento[3])
            elif(elecc == '3'):
                flag = False
                cursor.execute(  '''SELECT
                                        id, song_name, artist_name, fecha_agregada
                                    FROM
                                        lista_favoritos
                                    ORDER BY
                                        song_name DESC;''')
                arreglo = cursor.fetchall()
                for elemento in arreglo:
                    print('Cancion : ', elemento[1], ' |  Artista : ', elemento[2], ' |  Fecha guardado: ', elemento[3])
            else: print(' Opcion indicada no valida. Vuelva a intentarlo.')

    archivo.close()
    cnxn.commit()  
    cnxn.close()

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    ViewSongs(): Muestra las canciones reproducidas, mostrando fechas de la primera vez escuchadas y mas.
Paramatros: 
    -
Retorno:
    -
"""
def ViewSongs():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    archivo = open('Buscar.sql', 'r')
    data = archivo.read()
    cursor.execute(data)
    arreglo = cursor.fetchall()
    
    if(arreglo == []):
        print("No se han agregado canciones a tu lista de reproducción.")
    else:
        f = True
        while(f == True):
            desicion = str(input("Elige una de las siguientes opciones:\n(1) Mostrar lista de reproduccion\n(2) Buscar una cancion en la lista de reproduccion\nOpcion a elegir:"))
            if(desicion == '1'):
                f=False
                flag = True
                while(flag == True):
                    print("Elige como deseas ordenar tus canciones: \n\n (1) Ordenar por fecha\n (2) Ordenar por cantidad de veces reproducida")
                    elecc = str(input(" Opcion a elegir: "))
                    if(elecc == '1'):
                        flag = False
                        cursor.execute(  '''SELECT
                                                id, song_name, artist_name, fecha_reproduccion, cant_reproducciones, favorito
                                            FROM
                                                reproduccion
                                            ORDER BY
                                                fecha_reproduccion ASC;''')
                        arreglo = cursor.fetchall()
                        print('\nEstas son tus canciones:\n\n')
                        for elemento in arreglo:
                            if(elemento[5] == True):
                                print('Cancion : ', elemento[1], ' |  Artista : ', elemento[2], ' |  Fecha de reproduccion: ', elemento[3], ' | Veces reproducidas: ', elemento[4], '| Guardada en Favoritos')
                            else: print('Cancion : ', elemento[1], ' |  Artista : ', elemento[2], ' |  Fecha de reproduccion: ', elemento[3], ' | Veces reproducidas: ', elemento[4], '| No se encuentra en Favoritos')
                    elif(elecc == '2'):
                        flag = False
                        cursor.execute(  '''SELECT
                                                id, song_name, artist_name, fecha_reproduccion, cant_reproducciones, favorito
                                            FROM
                                                reproduccion
                                            ORDER BY
                                                cant_reproducciones  DESC;''')
                        arreglo = cursor.fetchall()
                        print('\nEstas son tus canciones:\n\n')
                        for elemento in arreglo:
                            if(elemento[5] == True):
                                print('Cancion : ', elemento[1], ' |  Artista : ', elemento[2], ' |  Fecha de reproduccion: ', elemento[3], ' | Veces reproducidas: ', elemento[4], '| Guardada en Favoritos')
                            else: print('Cancion : ', elemento[1], ' |  Artista : ', elemento[2], ' |  Fecha de reproduccion: ', elemento[3], ' | Veces reproducidas: ', elemento[4], '| No se encuentra en Favoritos')
                    else: 
                        print(' Opcion indicada no valida. Vuelva a intentarlo.')
            elif(desicion == '2'):
                f = False
                f2 = True
                while (f2 == True):
                    entrada1 = input("\nIngrese el nombre de la canción: ")
                    entrada = Recorrer_Nombres(entrada1)
                    cursor.execute('''SELECT
                                        song_name, artist_name, fecha_reproduccion, cant_reproducciones, favorito
                                    FROM
                                        reproduccion
                                    WHERE
                                        song_name = \''''+ entrada +'''\';''')
                    cancion = cursor.fetchall()
                    if(cancion != []):
                        f2 = False
                        for elemento in cancion:
                            if(elemento[4] == True):
                                print('Cancion : ', elemento[0], ' |  Artista : ', elemento[1], ' |  Fecha de reproduccion: ', elemento[2], ' | Veces reproducidas: ', elemento[3], '| Guardada en Favoritos')
                            else: print('Cancion : ', elemento[0], ' |  Artista : ', elemento[1], ' |  Fecha de reproduccion: ', elemento[2], ' | Veces reproducidas: ', elemento[3], '| No se encuentra en Favoritos') 
                    else: #Pedir si quiere volver a buscar o ir al menu principal
                        pedir = str(input("Cancion no encontrada. Elija una de las siguientes opciones:\n(1) Volver a buscar una cancion\n(2) Volver al menu principal\nOpcion a elegir: "))
                        f3 = True
                        while(f3 == True):
                            if(pedir == '1'):
                                f3=False
                            elif(pedir == '2'):
                                f3=False
                                f2=False
                                print('Dirigiendo al menu principal...')
                            else: print(' Opcion indicada no valida. Vuelva a intentarlo.')    
            else: print(' Opcion indicada no valida. Vuelva a intentarlo.')

    archivo.close()
    cnxn.commit()  
    cnxn.close()

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    PlaySong(): Reproduce una cancion, dando opcion de agregarla a favoritos o eliminarla de esta lista.
Paramatros: 
    -
Retorno:
    -
"""
def PlaySong():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    fecha = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day)
    flag1 = True
    while(flag1 == True):
        nombre_cancion1 = str(input("Escriba el nombre de la canción: "))
        nombre_cancion = Recorrer_Nombres(nombre_cancion1) 
        cursor.execute('''
                          SELECT
                            id, song_name, artist_name
                          FROM
                            repositorio_musica
                          WHERE
                            song_name = \''''+ nombre_cancion +'''\';''')
        data = cursor.fetchall()
        #Verifica si el nombre de la cancion a buscar existe en el repositorio, si no es así volver a ingresar el nombre
        if(data != []):
            data = Revisar_cancion(data)
            id = str(data[0][0])
            flag1 = False
            flag2 = True
            while(flag2 == True):
                decision = str(input(('\nSe ha encontrado la canción. ¿Desea reproducir? SI/NO ')))
                #Este te verifica si la eleccion de reproducir es la correcta. si no es así volver a ingresar la opcion
                if(decision == "SI"):
                    flag2=False
                    cursor.execute(''' SELECT
                                            song_name
                                        FROM
                                            reproduccion
                                        WHERE
                                            id = \'''' + id + '''\';''')
                    vr = cursor.fetchall()
                    #Verifica si la cancion a reproducir está en la lista de reproduccion o es primera vez que se reproduce
                    if(vr == []):
                        insert_query = '''INSERT INTO reproduccion (id, song_name, artist_name, fecha_reproduccion,
                                        cant_reproducciones)
                                        VALUES (?, ?, ?, ?, ?);'''
                        values = (id, data[0][1],data[0][2],fecha,1)
                        cursor.execute(insert_query, values)
                        #Mini menu para dirigir al principio o agregar a favorito
                        flag3=True
                        while(flag3==True):
                            elecc = str(input(('\nReproduciendo cancion '+ nombre_cancion +'\n\nElige una de las siguientes opciones\n (1) Agregar a Favorito.\n (2) Volver al menu principal.\n ')))
                            if(elecc == '1'):
                                flag3=False
                                cursor.execute('''UPDATE
                                                    reproduccion
                                                SET
                                                    favorito = 1
                                                WHERE
                                                    id = \'''' + id + '''\';''') 
                                insertf_query=  '''INSERT INTO lista_favoritos (id, song_name, artist_name, fecha_agregada)                
                                                   VALUES (?, ?, ?, ?);'''
                                values = (id, data[0][1], data[0][2], fecha) #VER LO DE LA FECHA
                                print("\nSe ha agregado la cancion " + nombre_cancion + " a tu lista de favoritos.")
                                cursor.execute(insertf_query, values)
                            elif(elecc == '2'):
                                flag3=False
                                print('Dirigiendo al menu principal...')

                            else:print('Opcion indicada no valida. Vuelva a intentarlo.')
                    else:
                        cursor.execute(''' SELECT
                                            cant_reproducciones
                                        FROM
                                            reproduccion
                                        WHERE
                                            id = \'''' + id + '''\';''')
                        cantidad = cursor.fetchall()[0][0]
                        cantidad  += 1     
                        cursor.execute('''UPDATE
                                            reproduccion
                                        SET
                                            cant_reproducciones = ''' + str(cantidad) + '''
                                        WHERE
                                            id = \'''' + id + '''\';''')
                        #Verificar si está en fav o no
                        cursor.execute('''SELECT
                                        song_name
                                    FROM
                                        lista_favoritos
                                    WHERE
                                        id = \'''' + id + '''\';''')
                        nom_fav = cursor.fetchall()
                        if(nom_fav == []):#No está en favoritos
                            f1 = True
                            while(f1 == True):
                                elecc1 = str(input(('\nReproduciendo cancion '+ nombre_cancion +'\n\nElige una de las siguientes opciones\n (1) Agregar a Favorito.\n (2) Volver al menu principal.\n ')))
                                if(elecc1 == '1'):
                                    f1=False
                                    cursor.execute('''UPDATE
                                                        reproduccion
                                                    SET
                                                        favorito = 1
                                                    WHERE
                                                        id = \'''' + id + '''\';''')
                                    insertf_query=  '''INSERT INTO lista_favoritos (id, song_name, artist_name, fecha_agregada)                
                                                    VALUES (?, ?, ?, ?);'''
                                    values = (id, data[0][1], data[0][2], fecha) #VER LO DE LA FECHA
                                    print("\nSe ha agregado la cancion " + nombre_cancion + "a tu lista de favoritos.")
                                    cursor.execute(insertf_query, values)
                                elif(elecc1 == '2'):
                                    flag3=False
                                    print('Dirigiendo al menu principal...')
                                else: print('Opcion indicada no valida. Vuelva a intentarlo.') 
                        else:
                            f2 = True
                            while(f2 == True):
                                elecc2 = str(input(('\nReproduciendo cancion '+ nombre_cancion +'\n\nElige una de las siguientes opciones\n (1) Eliminar de Favorito.\n (2) Volver al menu principal.\n ')))
                                if(elecc2 == '1'):
                                    f2 = False
                                    cursor.execute('''
                                                DELETE FROM 
                                                    lista_favoritos
                                                WHERE
                                                    id = \'''' + id + '''\';''')
                                elif(elecc2 == '2'):
                                    f2 = False
                                    print('Dirigiendo al menu principal...')
                                else:print('Opcion indicada no valida. Vuelva a intentarlo.')
                elif(decision == 'NO'):
                    flag2=False
                    print('Dirigiendo al menu principal...')

                else:print('Opcion indicada no valida. Vuelva a intentarlo.')
        else: print("No se ha encontrado la cancion.")
    cnxn.commit()
    cnxn.close()

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    PeakPosition(): Busca la cancion mas popular dentro del repertorio de musica.
Paramatros: 
    -
Retorno:
    -
"""
def PeakPosition():
    server = "DESKTOP-PH73MFC\SQLEXPRESS"
    database = "BD_Usm_Spot"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    flag = True
    while(flag == True):
        entrada1 = input("Ingrese el nombre del artista el cual desea saber su Peak Position\nNombre del artista: ")
        entrada = Recorrer_Nombres(entrada1)
        cursor.execute('''
                        SELECT
                            *
                        FROM
                            repositorio_musica
                        WHERE
                            artist_name = \'''' + entrada + '''\'
                        ORDER BY
                            peak_position ASC;
                    ''')
        salida = cursor.fetchall()
        if(salida != []):
            flag = False
            print("\nLa cancion " + salida[0][3] + ' de ' + salida[0][2] + 'fue la mas escuchada dentro de su repertorio, alcanzando el TOP '+ str(salida[0][6]))
        else: print("No se ha encontrado al artista.")

    archivo.close()
    cnxn.commit()  
    cnxn.close()

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    Escuchadas_Ultimamente(): Busca las canciones escuchadas entre x dias y hoy. 
Paramatros: 
    -
Retorno:
    -
"""
def Escuchadas_Ultimamente():
    server = "DESKTOP-PH73MFC\SQLEXPRESS"
    database = "BD_Usm_Spot"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    
    print('Ingrese la fecha desde donde desea mostrar las canciones escuchadas ultimamente')
    anio = input('Anio (numero): ')
    mes = input('Mes (numero): ')
    dia = input('Dia (numero): ')
    fecha = anio + '-' + mes + '-' + dia
    cursor.execute('''
                    SELECT
                        song_name, artist_name, fecha_reproduccion
                    FROM
                        reproduccion
                    WHERE
                        fecha_reproduccion >= \''''+ fecha + '''\';''')
    canciones = cursor.fetchall()

    largo = len(canciones)
    if(largo == 0):
        print('\nNo se ha encontrado ninguna cancion escuchada desde la fecha ingresada.\n\nVolviendo al menu principal...')
    else:
        print('Estas son las canciones escuchadas desde ' + fecha + ' hasta hoy: \n')
        for elemento in canciones:
            print('Cancion : ', elemento[0], ' |  Artista : ', elemento[1], ' |  Fecha de reproduccion: ', elemento[2])
    cnxn.commit
    cnxn.close()

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    Seach_Artist(): Menu de busqueda por artista, en el podrás buscar las canciones del artista y sus stream promedio
Paramatros: 
    -
Retorno:
    -
"""
def Search_Artist():
    server = "DESKTOP-PH73MFC\SQLEXPRESS"
    database = "BD_Usm_Spot"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    flag = True
    while(flag == True):
        entrada = input("Elija una de las siguientes opciones: \n (1) Buscar un artista y sus canciones\n (2) Buscar un artista y su promedio de streams\n\nOpcion a elegir: ")
        if(entrada == '1'):
            flag = False
            f = True
            while(f == True):
                artist = input("Ingrese el nombre del artista: ")
                artista = Recorrer_Nombres(artist)
                cursor.execute('''
                                SELECT
                                    song_name
                                FROM
                                    repositorio_musica
                                WHERE
                                    artist_name = \''''+ artista +'''\';''')
                lista = cursor.fetchall()
                if(lista != []):
                    f = False
                    print("Estas son las canciones del artista " + artista + ":\n")
                    for elemento in lista:
                        print(elemento[0])
                else: print('Opcion indicada no valida. Vuelva a intentarlo.')
        elif(entrada == '2'):
            flag = False
            f = True
            while(f == True):
                artista = input("\nIngrese el nombre del artista: ")
                cursor.execute('''
                                SELECT
                                    total_streams
                                FROM
                                    repositorio_musica
                                WHERE
                                    artist_name = \''''+ artista +''' \';''')
                
                lista = cursor.fetchall()
                if(lista != []):
                    f = False
                    i = 0
                    suma = 0
                    while(i < len(lista)):
                        suma = suma + int(lista[i][0])
                        i = i + 1
                    suma = round(suma/len(lista))
                    print('\nLa cantidad de streams promedio de ' + artista + ' es de '+ str(suma))
                else:print('Opcion indicada no valida. Vuelva a intentarlo.')
                    
                

        else: print('Opcion indicada no valida. Vuelva a intentarlo.') 

#-----------------------------------------------------------------------------------------------------
"""
Funcion:
    Top_15(): Muestra el listado de los 15 mejores artista respecto a su peak position en el top 3.
Paramatros: 
    -
Retorno:
    -
"""
def Top_15():
    server = "DESKTOP-PH73MFC\SQLEXPRESS"
    database = "BD_Usm_Spot"
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    cursor.execute('''SELECT
	                    artist_name
                    FROM
	                    repositorio_musica
                    GROUP BY
	                    artist_name
                    ORDER BY
                        artist_name ASC''')
    artistas = cursor.fetchall()
    lista = []
    for i in artistas:
        artist = i[0]
        artista = Recorrer_Nombres(artist)
        cursor.execute('''SELECT
                            peak_position_time
                        FROM
                            repositorio_musica
                        WHERE
                            artist_name = \''''+ artista +''' \';''')
        peak = cursor.fetchall()
        
        suma = 0
        for j in peak:
            if( j[0] == '0'):
                suma = suma + 0
            else:
                suma = suma + int(j[0][2:-1])
        aux = (artista,suma)
        lista.append(aux)

    lista.sort(key=lambda x: x[1], reverse=True)
    i = 0
    print('Estos son los artistas mas reconocidos hasta el momento: \n')
    while(i < 15):
        print('El artista ' + lista[i][0] + 'ha estado en el Top-10 ' + str(lista[i][1]) + ' veces')
        i += 1
    
#-----------------------------------------------------------------------------------------------------
#Conexión BD
server = "DESKTOP-PH73MFC\SQLEXPRESS"
database = "BD_Usm_Spot"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
cursor = cnxn.cursor()

#Creacion de Tablas
archivo = open('Table_Creation.sql','r')
data = archivo.read()
cursor.execute(data)
archivo.close()
cursor.execute('''SELECT COUNT(id) FROM repositorio_musica''')
contable = int(cursor.fetchall()[0][0])
if(contable == 0):
    #Subir los datos a las tablas
    archivo2 = open("song.csv",  encoding="utf8")
    insert_query = '''INSERT INTO repositorio_musica (position, artist_name, song_name, days, top_10, 
                    peak_position, peak_position_time, peak_streams, total_streams)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);'''
    i = 0
    for linea in archivo2:
        i += 1
        if(i >= 2):
            lista = linea.rstrip().split(";")
            #Variables de cada columna
            position = int(lista[0])
            artist_name = str(lista[1])
            song_name = str(lista[2])
            days = int(lista[3])
            top_10 = int(lista[4])
            peak_position = int(lista[5])
            peak_position_time = str(lista[6])
            peak_streams = int(lista[7])
            total_streams = int(lista[8])
            values = (position, artist_name, song_name, days, top_10, peak_position, peak_position_time, peak_streams, total_streams)
            cursor.execute(insert_query, values)
    archivo2.close()

cnxn.commit()
cnxn.close()

#-----------------------------------------------------------------------------------------------------
#Main
print("\nBienvenido(a) a Spot-Usm, la plataforma mas prestigiosa de streaming musical, en la cual podras encontrar tus canciones preferidas, reproducirlas, guardarlas y mucho mas.\n")
Menu_principal()

#-----------------------------------------------------------------------------------------------------