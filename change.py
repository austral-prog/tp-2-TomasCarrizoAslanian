def change():
    gasto = 23.75
dinero_recibido = 100

vuelto_total = dinero_recibido - gasto
pesos = int(dinero_recibido - gasto)
centavos = int(round((vuelto_total - pesos) * 100))

print("Ingresar gasto:")
print(gasto)
print("Dinero Recibido:")
print(dinero_recibido)
print()
print("Vuelto")
print()
print("Pesos:")
print(pesos)
print("Centavos:")
print(centavos)
