print("¡Bienvenido!")
usernames = ["admin", "noadmin"]
passwords = ["admin", "noadmin"]
def checkBox(box1,box2):
    if box1 == box2:
        return True
    else:
        return False
def intValidacion(entrada):
    try:
        int(entrada)
    except ValueError:
        print("No debes escribir letras ni simbolos")
    else:
        return True 
def userValidacion(user,password):
    intentos_user = 0
    intentos_pass = 0
    true_user = 0
    true_pass = 0
    for _ in usernames:
        intentos_user += 1
        iterable_user = usernames[intentos_user-1]
        if iterable_user == user:
            true_user += 1
            break
    if true_user == 1:
        for _ in passwords:
            intentos_pass += 1
            iterable_pass = passwords[intentos_pass-1]
            if iterable_pass == password:
                true_pass += 1
                break
    if true_pass == 1 and intentos_pass == intentos_user:
        return True
New_User_ = 0
while True:
    initial_option = ("Iniciar Sesion: 1" , "Crear Usuario: 2", "Cerrar Programa: 3")
    print(initial_option) 
    while True:
        while True:    
            eleccion = input("Que desea hacer?: ")
            if intValidacion(eleccion) == True:
                break
        if int(eleccion) > len(initial_option):
            print(f"{initial_option} no es una opcion valida")
            continue        
        else: 
            break 
    if int(eleccion) == 3:
        print("Se procedera a cerrar el programa")
        quit()
    elif int(eleccion) == 1:
        while True:
            user_name = input("Ingrese su nombre de usuario: ") 
            pass_word = input("Ingrese su contraseña: ")
            if userValidacion(user_name, pass_word) == True:
                   print("Ingreso Exitosamente")
                   break
            if user_name in usernames:
                print("Tu nombre de usuario o contraseña son incorrectas")
            else:
                print("Tu nombre de usuario no esta en nuestra base de datos")
            if userValidacion(user_name, pass_word) != True:
                while True:
                    print("Desea crear un nuevo usuario?: ")
                    new_user_ = input("Si: 1  No: 2\n")
                    if intValidacion(new_user_) == True:
                        if int(new_user_) == 1:
                            New_User_ =+ 1
                            break
                        else:
                            break
                    if int(new_user_) > 2:
                        print("Esa no es una opcion valida")
            if int(new_user_) == 1:
                break     
    if  int(eleccion) == 2 or New_User_ == 1:
        while True:
            cancelacion = 0
            cancelacion =- cancelacion
            new_user = input("Ingrese el nombre de usuario que desea: ")
            if new_user in usernames:
                    print("Ese nombre de usuario no esta disponible, por favor intenta otro")
                    continue
            check_new_user = input("Ingrese de nuevo el nombre de usuario que desea: ") #Crear Usuario
            if checkBox(new_user,check_new_user) == True:
                    usernames += [new_user]
                    break
            else:
                print("Tu entradas de nombre de usuario no concuerdan")
                while True:
                    while True:
                        print("Desea Cancelar la creacion del nuevo usuario?")    
                        cancelacion_new_user = input("Si: 1  No: 2\n")
                        if intValidacion(cancelacion_new_user) == True:
                            break
                    if int(cancelacion_new_user) > 2:
                        print("Esa no es una opcion valida")
                        continue
                    if int(cancelacion_new_user) == 1:
                        cancelacion =+ 1
                        break
                    else: 
                        break 
            if cancelacion == 1:
                break
        while True:
            new_pass = input("Ingrese la contraseña que desea: ")   # Crear Contraseña
            check_new_pass = input("Ingrese de nuevo la contraseña que desea: ")
            if checkBox(new_pass,check_new_pass) == True:
                    passwords += [new_pass]
                    print(f"El usuario {new_user} registrado correctamente") # falta validad que la entrada no sea null
                    break
            else:
                print("Tu entradas contraseña no concuerdan")
                while True:
                    while True:
                        print("Desea Cancelar la creacion del nuevo usuario?")    
                        cancelacion_new_user = input("Si: 1  No: 2\n")
                        if intValidacion(cancelacion_new_user) == True:
                            break
                    if int(cancelacion_new_user) > 2:
                        print("Esa no es una opcion valida")
                        continue
                    else: 
                        break 
        if int(cancelacion_new_user)==1: # arreglar esto para que se cancele la creacion del usuario
            New_User_ =- New_User_
