import pyshark
import codecs
import difflib
from termcolor import colored

def read_pcapng(file_path):
    packets = []
    # Lee el archivo .pcapng
    cap = pyshark.FileCapture(file_path)
    for packet in cap:
        # Solo considera los paquetes con destino a "8.8.8.8"
        if 'IP' in packet and packet.ip.dst == '8.8.8.8':
            data = packet.layers[-1].data
            # Extrae el primer byte de la capa de datos y lo convierte a ASCII
            byte = int(data[0:2], 16)
            char = chr(byte)
            packets.append(char)
    return ''.join(packets)

def caesar_decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            else:
                if shifted < ord('a'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def find_best_decryption(encrypted_text):
    best_decryption = ''
    best_score = 0
    for shift in range(26):
        decryption = caesar_decrypt(encrypted_text, shift)
        # Puedes usar alguna biblioteca de procesamiento de lenguaje natural aquí para mejorar la detección
        # En este ejemplo, simplemente comparamos con un diccionario de palabras en español
        spanish_words = set(["el", "la", "los", "las", "un", "una", "de", "en", "y", "a", "para", "por"])
        words = decryption.split()
        common_words = sum(1 for word in words if word in spanish_words)
        if common_words > best_score:
            best_score = common_words
            best_decryption = decryption
    return best_decryption

if __name__ == "__main__":
    file_path = input("Ingrese la ruta del archivo .pcapng: ")
    encrypted_text = read_pcapng(file_path)

    best_decryption = find_best_decryption(encrypted_text)

    # Imprime todas las combinaciones posibles con su llave, pero marca en verde la que tiene más sentido
    for shift in range(26):
        decryption = caesar_decrypt(encrypted_text, shift)
        if decryption == best_decryption:
            print(f'Llave {shift}: {colored(decryption, "green")}')
        else:
            print(f'Llave {shift}: {decryption}')


if __name__ == "__main__":
    file_path = input("Ingrese la ruta del archivo .pcapng: ")
    encrypted_text = read_pcapng(file_path)

    # Imprime todas las combinaciones posibles con su llave
    for shift in range(26):
        decryption = caesar_decrypt(encrypted_text, shift)
        if shift == 0:
            print(f'Llave {shift}: {colored(decryption, "green")}')
        else:
            print(f'Llave {shift}: {decryption}')

    # Imprime la opción con más sentido en verde
    decrypted_text = find_best_decryption(encrypted_text)
    print("\nDecodificación con mejor sentido:")
    print(colored(decrypted_text, "green"))
