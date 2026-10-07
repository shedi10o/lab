# Lista de pesos generada por el sistema de pesaje
pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]

# Contador de piezas aprobadas (ligeras y pesadas)
piezas_validas = 0

# Recorrer la lista para evaluar y clasificar cada pieza
for peso in pesos_piezas:
    if peso <= 0:
        print("Error de lectura: Flujo negativo descartado.")
    elif 1 <= peso <= 13:
        print("Pieza Ligera aprobada.")
        piezas_validas += 1
    elif peso > 13:
        print("Pieza Pesada aprobada.")
        piezas_validas += 1

# Conteo final de piezas válidas
print(f"\nTotal de piezas válidas aprobadas: {piezas_validas}")
