import sys

def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26  # Maneja desplazamientos mayores a 25
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python cesar_codificador.py <texto> <numero>")
        sys.exit(1)

    texto = sys.argv[1]
    try:
        numero = int(sys.argv[2])
    except ValueError:
        print("El número debe ser un entero")
        sys.exit(1)

    texto_codificado = caesar_encrypt(texto, numero)
    print("Texto codificado:", texto_codificado)
