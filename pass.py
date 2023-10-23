# Abre el archivo de entrada en modo lectura con codificación 'utf-8' (ajusta esto según la codificación de tu archivo)
with open('rockyou.txt', 'r', encoding='utf-8') as archivo_entrada:
    contraseñas = archivo_entrada.read().splitlines()

# Filtra y modifica las contraseñas
contraseñas_filtradas = []
for contraseña in contraseñas:
    if contraseña and contraseña[0].isalpha():
        contraseña_modificada = contraseña[0].upper() + contraseña[1:] + '0'
        contraseñas_filtradas.append(contraseña_modificada)

# Abre un archivo de salida en modo escritura
with open('rockyou_mod.dic', 'w', encoding='utf-8') as archivo_salida:
    for contraseña_modificada in contraseñas_filtradas:
        archivo_salida.write(contraseña_modificada + '\n')

# Cuenta la cantidad de contraseñas en el archivo modificado
cantidad_contraseñas = len(contraseñas_filtradas)

print("Contraseñas procesadas y guardadas en 'rockyou_mod.dic'")
print(f"Cantidad de contraseñas en el archivo modificado: {cantidad_contraseñas}")
