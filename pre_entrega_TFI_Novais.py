"""
Vas a desarrollar un programa en Python que cumpla con las siguientes características:
Done 1) Ingreso de datos de productos: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría y precio (sin centavos). Estos datos deben almacenarse en una lista, donde cada cliente sea representado/a como una sublista de tres elementos (nombre, categoría, y precio).
Done 2) Visualización de productos registrados: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados. La información debe presentarse de manera ordenada y legible, con cada producto numerado.
Done 3) Búsqueda de productos: El sistema debe permitir buscar productos por su nombre. Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.
Done 4) Eliminación de productos: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

Requisitos:
1) Usar listas para almacenar y gestionar los datos.
2) Incorporar bucles while y for según corresponda.
3) Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.
4) Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.
5) Presentar un menú que permita elegir entre las funcionalidades disponibles: agregar productos, visualizar productos, buscar productos y eliminar productos.
6) El programa debe continuar funcionando hasta que se elija una opción para salir.
"""

# Variables globales
# Se crea una lista vacía para almacenar los productos (diccionarios generados)
productos = []
# Se crea una lista vacía para almacenar los productos encontrados y poder reinicar para una nueva búsqueda
productos_encontrados = []
# Se crea este dato para poder visualizar/buscar/borrar el diccionario correspondiente al producto
codigo_producto = 0


# Función del menú principal del programa. 
def menu():

    while True:
        # Se crea esta variable vacía para poder correr el menú y pasar la variable "opciones_menu" a type int
        opciones_menu_int = []
        # Input para que el usuario ingrese la opción deseada.
        opciones_menu = input('\nPor favor, indique la opción deseada: \nSi desea agregar un producto, presione 1.\nSi desea visualizar el listado completo de productos, presione 2.\nSi desea buscar un producto, presione 3.\nSi desea modificar un producto, presione 4.\nSi desea eliminar un producto, presione 5.\nSi desea salir del programa, presione 6.\n\nEscriba aquí su opción: ').strip()
        
        
        # Evitamos el error de la app si el usuario no ingresa datos.
        if opciones_menu == '' and type(opciones_menu) == str and not opciones_menu.isdigit():
            print("Error. Por favor, ingrese la opción deseada.")
        
        # Si la entrada es un número, lo pasa a type int para poder ingresar en la opción del menú deseada.
        if opciones_menu.isdigit():
            # Pasa el valor ingresado por el usuario a type int para que la app lo pueda utilizar en el match siguiente
            opciones_menu_int = int(opciones_menu)

        # Redirecciona a la función del menú deseada de acuerdo al input del usuario.
        match opciones_menu_int:
            case 1:
                # Llama a la función "agregar_productos" para que se ejecute
                agregar_productos()
            case 2:
                # Llama a la función para que se ejecute
                mostrar_listado_menu()
            case 3:
                # Llama a la función para que se ejecute
                buscador_de_productos_menu()
            case 4:
                # Llama a la función para que se ejecute
                modificar_producto()
            case 5:
                # Llama a la función para que se ejecute
                eliminar_producto()
            case 6:
                # Se despide con estilo
                print('\nHasta la vista, baby')
                exit()
            case _:
                # Por si el usuario flashea
                print("No ingresó una opción válida.")
            
        

# Función Menú de Bienvenida
def menu_de_bienvenida():
    # Damos la bienvenida al programa.
    print('\n¡Bienvenidos al progama de administración de productos de su negocio!')
    menu()
    


# Función para mostrar el listado completo de productos en la terminal | Se puede hacer otra función para mostrar el listado agregado en la sesión.
def mostrar_listado_de_productos():
    print('\nProductos registrados: ')
    for producto in productos:
        print(
            f'Código del producto: Nº{producto["codigo"]} \nProducto:  {producto["nombre"].capitalize()} \nCategoría: {producto["categoria"].capitalize()}\nPrecio:\t   ${producto["precio"]}\n')


# Función Nº 2 del menú. Llama a la función "mostrar_listado_de_productos" la cual muestra el listado completo del productos en la terminal desde el menú del inicio
def mostrar_listado_menu():
    mostrar_listado_de_productos()
    # Llama a la función "menu_de_bienvenida" para volver al menú principal y elegir qué hacer
    menu()


# Función Nº1 del Menú. Esta permite ingresar productos a la lista de productos.
def agregar_productos():

    # Creamos la variable "nombre" para ingresar en un futuro cercano el nombre de producto
    nombre = ""
    while not nombre == "fin":
        # Bucle para agregar productos y precios
        print('\nPor favor, ingrese los datos del producto o escriba "fin" para finalizar. ')
       
        # Solicita el nombre del producto
        nombre = input('Nombre del producto: ').lower().strip()
        while nombre =="":    
            # Chequea si el usuario no ingresó datos
            if nombre == '':
                print('Error. Por favor, ingrese el nombre del producto.')
                nombre = input('Nombre del producto: ')
        if nombre == 'fin':
                break   
        
        # Creamos la variable "categoria" para ingresar el tipo de producto
        categoria = ""
        while categoria == "":
            # Solicita el tipo de producto
            categoria = input('Introduzca el tipo de producto: ')
            # Chequea si el usuario dejó en blanco
            if categoria == '':
                print('Por favor, necesitamos que ingrese un dato válido.')
            
        # Creamos la variable "precio" para ingresar el precio de producto
        # Solicita el precio del producto
        precio = input("Valor del producto: $")

        # Chequea que el usuario haya ingresado contenido
        while precio == "" :
            print('Ingresó un dato no válido. Por favor, ingrese un valor.')
            precio = input("Valor del producto: $")
            
        # Si el usuario ingresó type str pide que ingrese un número
        while type(precio) == str and not precio.isdigit():
            print("Ingresó un dato no válido. Por favor, ingrese un valor.")
            precio = input("Valor del producto: $")
            
        # Si el usuario ingresó un valor lo pasa a int    
        if precio.isdigit():
            # Pasar el string ingresado a type int
            precio = int(precio)

        # Procedimeinto para generar el producto (diccionario) y agregarlo a la lista "productos" (variable global).
        # Usamos global para modificar la variable global sumándole uno.
        global codigo_producto
        codigo_producto += 1
        # Se crea el diccionario con los datos ingresados
        producto = {
            "codigo": codigo_producto,
            "nombre": nombre,
            "categoria": categoria.lower().strip(),
            "precio": precio
        }
        # Agrega el diccionario a la lista de productos. Ponemos global para cuando se modularice la app.
        global productos
        # Insertamos el producto en el índice correspondiente.
        productos.append(producto)
        #print(productos)

        # Muestra al usuario la incorporación realizada
        print(f'\n\n\nA continuación le mostramos la incorporación realizada: \n\tCódigo:\t{producto["codigo"]}\n\tNombre:\t{producto["nombre"].capitalize()}\n\tCategoría: {producto["categoria"].capitalize()}\n\tPrecio: ${producto["precio"]}\n')
        

    # Llama a la función mostrar_listado_de_productos para imprimir el listado completo de los productos | 
    print('\nEstado actual del listado de Productos:')
    mostrar_listado_de_productos()
    


# Función para buscar productos en la lista. Esta se encontrará dentro de la Función Nº2 (buscador de producto) y Función Nº 4 (eliminar producto) del Menú principal.
def buscador_de_productos():
    while True:
        # Crea la variable para iterar la lista y buscar el producto deseado
        buscar_producto = input(
            'Por favor, ingrese algún dato del producto a buscar o presione "Enter" para finalizar: ').strip()
        # Elimina cualquier entrada de la lista de productos encontrados para hacer una nueva búsqueda
        productos_encontrados.clear()
        # Si el usuario no ingresa un dato, se sale del bucle
        if buscar_producto == '':
            break

        # Buscar el producto en la lista
        # Si el valor ingresado es type string ejecuta el siguiente código para buscar en las keys nombre y categoría
        if type(buscar_producto) == str:
            buscar_producto = buscar_producto.lower()
            print(f'\nLa búsqueda "{buscar_producto}" fue encontrada en el/los siguiente/s producto/s:')
            for producto in productos:
                if producto.get('nombre') == buscar_producto or producto.get('categoria') == buscar_producto:
                    # Imprime los productos encontrados
                    print(
                        f'\n\tCódigo:\t{producto["codigo"]}\n\tNombre:\t{producto["nombre"].capitalize()}\n\tCategoría: {producto["categoria"].capitalize()}\n\tPrecio: ${producto["precio"]}.\n')
                    # Suma un elemento a productos_encontrados para que no ejecute el mensaje de error si no encuentra alguno.
                    productos_encontrados.append(buscar_producto) 
                    

        # Si el valor ingresado es type int ejecuta el siguiente código para buscar en las keys código y precio
        if buscar_producto.isdigit():
            # Pasa el input a type int para buscar cógio o valor del producto
            buscar_producto_int = int(buscar_producto)
            print(f'\nLa búsqueda "{buscar_producto}" fue encontrada en el/los siguiente/s producto/s:')
            for producto in productos:
                if producto.get('codigo') == buscar_producto_int or producto.get('precio') == buscar_producto_int:
                    # Imprime los productos encontrados
                    print(
                        f'\n\n\tCódigo:\t{producto["codigo"]}\n\tNombre:\t{producto["nombre"].capitalize()}\n\tCategoría: {producto["categoria"].capitalize()}\n\tPrecio: ${producto["precio"]}.\n')
                    # Suma un elemento a productos_encontrados para que no ejecute el mensaje de error si no encuentra alguno.
                    productos_encontrados.append(buscar_producto_int)
            

        # Si no hay productos encontrados, lo informa al usuario
        if productos_encontrados == []:
            print('No se encontró ningún producto.\n')


# Función Nº 3 del Menú principal, llama a la función "buscador_de_productos" para buscar productos en el listado general
def buscador_de_productos_menu():
    print('\nBienvenido al buscador de productos.\n')
    buscador_de_productos()
    


# Función Nº4 del menú principal para editar productos
def modificar_producto():
    print('\nBienvenido a la función para editar productos. \nA continuación le solicitamos que busque el producto a editar del listado.')
    buscador_de_productos()

    # Con el dato del producto, le pedimos que ingrese el código del mismo para poder acceder y modificarlo
    while True:
        # Creamos la variable para ingresar el código del producto a eliminar
        cod_producto_a_modificar = input(
            '\nPor favor, ingrese el código del producto a modificar o presione "Enter" para salir: ').strip()

        # Si el usuario no ingresa el código, se sale del bucle
        if cod_producto_a_modificar == "":
            break 

        # Si el usario ingresa un string, le solicita que ingrese un número y evita el error en el código
        while not cod_producto_a_modificar.isdigit():
            print('Ingresó un texto.')
            cod_producto_a_modificar = input('\nPor favor, ingrese el código del producto a eleminar o presione "Enter" para salir: ').strip()
            continue
            
        
        
        # Pasa el input a type int para poder modificar.
        if cod_producto_a_modificar.isdigit():
            cod_producto_a_modificar_int = int(cod_producto_a_modificar)
            # Creamos esta variable vacía para ver si encuentra el código dentro del listado(me imprimía una linea por cada elemento en la lista)
            no_existe_codigo = []
            # Chequea que el código ingresado esté en la lista de productos
            for producto in productos:
                if producto.get('codigo') == cod_producto_a_modificar_int:
                    # Si encuentra un producto con ese código lo suma a la lista "no_existe_codigo"
                    no_existe_codigo.append(producto)
        
            # Imprime mensaje de código inexistente cuando la lista "no_existe_codigo" sigue vacía ya que no se encontró ningún producto con ese código
            if no_existe_codigo == 0:
                print('Ingresó un código inexistente.')
                # Nos saca de este menú y regresa al menú principal
                break    
            

            
            # Solicita el key a modificar:
            key_a_modificar = input('Por favor, ingrese qué valor desea modificar. \nPresione 1 si desea modificar el nombre. \nPresione 2 si desea modificar el tipo de producto. \nPresione 3 si desea modificar el precio.\nPresione 4 si desea regresar al menú de inicio.\n\nPor favor, ingrese su opción aquí: ').strip()
            # Evitamos el error de la app si el usuario ingresa un string.
            while type(key_a_modificar) == str and not key_a_modificar.isdigit():
                print("Error. Por favor, ingrese el número indicado.")
                key_a_modificar = input('\nPor favor, ingrese qué valor desea modificar. \nPresione 1 si desea modificar el nombre. \nPresione 2 si desea modificar el tipo de producto. \nPresione 3 si desea modificar el precio.\nPresione 4 si desea regresar al menú de inicio.\n\nPor favor, ingrese su opción aquí: ').strip()
            
            # Evitamos el error de la app si el usuario no ingresa datos.
            while key_a_modificar == '' and not key_a_modificar.isdigit():
                print("Error. Por favor, ingrese el número indicado.")
                key_a_modificar = input('\nPor favor, ingrese qué valor desea modificar. \nPresione 1 si desea modificar el nombre. \nPresione 2 si desea modificar el tipo de producto. \nPresione 3 si desea modificar el precio.\nPrecione 4 si desea volver al menú de inicio. \n\nPor favor, ingrese su opción aquí: ').strip()
            
            # Si la entrada es un número, lo pasa a type int para poder ingresar en la opción del menú deseada.
            if key_a_modificar.isdigit():
            # Pasa el valor ingresado por el usuario a type int para que la app lo pueda utilizar en el match siguiente
                key_a_modificar_int = int(key_a_modificar)

                # Asociamos el valor ingresado a las keys de nuestros productos
                match key_a_modificar_int:
                    case 1:
                        llave = 'nombre'
                    case 2:
                        llave = 'categoria'
                    case 3:
                        llave = 'precio'
                    case 4:
                        break
                    case _:
                        print("No ingresó una opción válida.")


                # Solicita al usuario el valor a moficiar
                nuevo_valor=input('\nPor favor, ingrese la modificación a realizar: ').strip()
                # Si es de tipo string lo usamos para modificar el 'nombre' o 'categoría' (de acuerdo a lo que solicitó el usuario)    
                if type(nuevo_valor) == str:
                    nuevo_valor = nuevo_valor.lower()
                    for producto in productos:
                        if producto.get('codigo') == cod_producto_a_modificar_int:
                            # Hace las modificaciones en el producto
                            producto [f'{llave}']= f'{nuevo_valor}'
                        
                
                # Si es de tipo numérico se utiliza para modificar el 'precio', lo pasa a type int y modifica la key valor del producto
                if nuevo_valor.isdigit():
                    # Pasa el input a type int
                    nuevo_valor_int= int(nuevo_valor)
                    for producto in productos:
                        if producto.get('codigo') == cod_producto_a_modificar_int:
                            # Hace las modificaciones en el producto
                            producto[f'{llave}'] = nuevo_valor_int
            
                # Muestra al usuario cómo quedó el producto modificado
                for producto in productos:
                        if producto.get('codigo') == cod_producto_a_modificar_int:
                            print(f'\n\nA continuación le mostramos la modificación realizada: \n\tCódigo:\t{producto["codigo"]}\n\tNombre:\t{producto["nombre"].capitalize()}\n\tCategoría: {producto["categoria"].capitalize()}\n\tPrecio: ${producto["precio"]}.\n')
                break

            
            
            
# Función Nº 4 del menú, la cual elimina productos del listado general.
def eliminar_producto():
    print('\nBienvenido a la función para eleminar productos. \nA continuación le solicitamos que busque el producto a eliminar del listado.')
    buscador_de_productos()

    # Con el dato del producto, le pedimos que ingrese el código del mismo para poder acceder y eliminarlo
    while True:
        # Creamos la variable para ingresar el código del producto a eliminar
        producto_a_eliminar = input(
            '\nPor favor, ingrese el código del producto a eleminar o presione "Enter" para salir: ').strip()

        # Si el usuario no ingresa el código, se sale del bucle
        if producto_a_eliminar == "":
            break

        # Si el usario ingresa un sting, le solicita que ingrese un número y evita el error en el código
        if not producto_a_eliminar.isdigit():
            print('Ingresó un valor no válido.')
            producto_a_eliminar = input(
                '\nPor favor, ingrese el código del producto a eleminar o presione "Enter" para salir: ').strip()

        # Pasa el input a type int para poder borrar el producto.
        producto_a_eliminar_int = int(producto_a_eliminar)
        # Creamos variable para sumar el producto borrado cuando encuentra un producto con el código que da el cliente y, de ser necesario, poder recuperarlo si el usuario se arrepiente. Si ingresa un código inexistente la lista queda en 0
        producto_eliminado = []

        # Bucle para buscar y acceder al código del producto en el listado de productos
        for producto in productos:    
            # Accedemos el producto por el key 'codigo' para eliminarlo
            if producto.get('codigo') == producto_a_eliminar_int:
                
                # Obtiene índice del producto para incorporarlo en caso de que el usuario se arrepienta
                index_producto_eliminado = productos.index(producto)
                #print(index_producto_eliminado) | Se usó para verificar si la info era correcta
                
                # Elimina el producto (diccionario) de la lista de productos.
                #Ver cómo funciona con pop. Se usan los corchetes para que producto_eliminado siga siendo una lista,porque si haces producto_eliminado = productos.pop(index_producto_eliminado) producto_eliminado pasa a ser como un diccionario u objeto y cuando lo queres recorrer despues con el for itera sobre sus valores y por eso da error
                producto_eliminado = [productos.pop(index_producto_eliminado)]
                #print(productos) | Se utilizó para ver si se eliminó el producto
                #print(producto_eliminado) | Se usó para ver si funcionaba pop. Pero después no podía mostrar el producto, cosa que con append y remove si puedo.
                # Elimina el producto (diccionario) de la lista de productos. Fue la primera versión, hasta que incorporé el pop que hacía las dos cosas.
                #producto_eliminado.append(producto)
                #productos.remove(producto)
                break
            # Si se ingresa un código inexistente da mensaje de error al usuario
            if producto_eliminado == 0:
                print("Ingresó un código no válido")

        # Muestra al usuario el producto eliminado 
        for eliminado in producto_eliminado:
            print(f"\nSe eliminó el siguiente producto: \n\tCódigo:\t{eliminado['codigo']}\n\tNombre:\t{eliminado['nombre'].capitalize()}\n\tCategoría: {eliminado['categoria'].capitalize()}\n\tPrecio: ${eliminado['precio']}.\n") 

        # Le damos la posibilidad al usuario de reincorporar nuevamente el producto eliminado en la ubicación que tenía anteriormente.
        arrepentido= []
        while True:
            # Input para que el usuario decida si quiere reincorporar el producto.
            arrepentido = input('¿Te arrepentiste?\nPodemos ayudarte.\n\nSi desea reincorporar el producto, escriba "si"; y desea salir, presione "Enter": ').strip().lower()
            
            # Si el usuario escribe si, continúa el proceso de reincorporación
            if arrepentido == "si":
                # Inserta el producto en el índice correspondiente de la lista.
                productos.insert(index_producto_eliminado,eliminado)
                # Muestra al usuario el producto eliminado reincorporado
                print(f"\nSe acaba de reincorporar el siguiente producto: \n\tCódigo:\t{eliminado['codigo']}\n\tNombre:\t{eliminado['nombre'].capitalize()}\n\tCategoría: {eliminado['categoria'].capitalize()}\n\tPrecio: ${eliminado['precio']}.\n")
                break  
            # Si el usuario presiona enter, sale del ciclo while 
            elif arrepentido == "":
                break
            # Si el usuario ingresó otro dato no válido, vuelve al ciclo.
            else:
                print("No ingresó una opción válida.")
        break

    # Imprime el listado de productos luego de la modificación
    print('A continuación imprimiremos el listado completo luego de la modificación realizada.')
    mostrar_listado_de_productos()



# Llama a la función para que se ejecute y se inicie el programa
menu_de_bienvenida()
