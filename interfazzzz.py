
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
            else:
                print("Tu usuario o contraseña son erroneos")

    elif  int(eleccion) == 2:
        while True:
            new_user = input("Ingrese el nombre de usuario que desea: ")
            if new_user in usernames:
                    print("Ese nombre de usuario no esta disponible, por favor intenta otro")
                    continue
            check_new_user = input("Ingrese de nuevo el nombre de usuario que desea: ")
            if checkBox(new_user,check_new_user) == True:
                    usernames += [new_user]
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
                    else: 
                        break 
            if int(cancelacion_new_user) == 1:
                break
        while True:
            new_pass = input("Ingrese la contraseña que desea: ")
            check_new_pass = input("Ingrese de nuevo la contraseña que desea: ")
            if checkBox(new_pass,check_new_pass) == True:
                    passwords += [new_pass]
                    print(f"El usuario {new_user} registrado correctamente") ## Borrar al final
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
