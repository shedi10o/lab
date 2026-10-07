# Bucle interactivo para el control de movimiento del robot
while True:
    print("\n--- Menú de Control del Robot ---")
    print("A. Mover a la derecha")
    print("B. Mover a la izquierda")
    print("C. Mover hacia el frente")
    print("D. Mover hacia atrás")
    print("E. Apagar")

    # Lectura del comando ingresado por el usuario
    comando = input("Ingrese un comando (A, B, C, D o E): ").strip().upper()

    # Evaluación del comando ingresado mediante match/case
    match comando:
        case "A":
            print("El robot se desplazó a la derecha")
        case "B":
            print("El robot se desplazó a la izquierda")
        case "C":
            print("El robot se desplazó hacia adelante")
        case "D":
            print("El robot se desplazó hacia atrás")
        case "E":
            print("Apagando el robot. Fin del programa.")
            break
        case _:
            print("Comando no reconocido. Intente de nuevo.")
