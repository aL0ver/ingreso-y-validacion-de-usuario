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

def userValidacion(user,password):
    intentos_user = 0
    intentos_pass = 0
    true_user = 0
    true_pass = 0
    
    for _ in usernames:
        intentos_user += 1
        iterable_pass = usernames[intentos_user-1]
        if iterable_pass == user:
            true_user += 1
            break
    if true_user == 1:
        for _ in passwords:
            intentos_pass += 1
            iterable_pass = passwords[intentos_pass-1]
            if iterable_pass == password:
                true_user += 1
                break
    if true_pass == 1 and intentos_pass == intentos_user:      # arreglar esta mierda :v
        return True
    else:
        return False


while True:
    
    initial_option = ("Iniciar Sesion: 1" , "Crear Usuario: 2", "Cerrar Programa: 3")
    print(initial_option)
    
    while True:
        eleccion = input("Que desea hacer?: ")
        intValidacion(eleccion)
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
            intentos = 1
            while intentos >= 1:
                intentos += 1
                new_user = input("Ingrese el nombre de usuario que desea: ")
                if new_user in usernames:
                        print("Ese nombre de usuario no esta disponible, por favor intenta otro")
                        continue
                check_new_user = input("Ingrese de nuevo el nombre de usuario que desea: ")
                if checkBox(new_user,check_new_user) == True:
                        usernames += new_user
                        print(f"{new_user} registrado correctamente")
                        break
                else:
                    print("Tu entradas de nombre de usuario no concuerdan")
                if intentos >= 5:
                    print("Desea Cancelar la creacion del nuevo usuario?")
                    while True:
                        cancelacion_new_user = input("Si: 1  No: 2\n")
                        intValidacion(cancelacion_new_user)
                        if int(cancelacion_new_user) > 2:
                            print("Esa no es una opcion valida")
                        elif int(cancelacion_new_user) == 1:
                            break
                        else:
                            intentos -= 4
                            break 
