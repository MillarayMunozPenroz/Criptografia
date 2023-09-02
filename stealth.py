import sys
import time
from scapy.all import *

def send_icmp_packet(destination, payload, id, seq):
    # Construye un paquete ICMP request personalizado
    icmp_packet = IP(dst=destination) / ICMP(type=8, id=id, seq=seq) / Raw(load=payload)

    # Guarda el tiempo de inicio
    start_time = time.time()

    # Envía el paquete ICMP
    send(icmp_packet)

    # Calcula el tiempo transcurrido y lo almacena en icmp.packet.time
    icmp_packet.time = time.time() - start_time

    return icmp_packet

def main():
    if len(sys.argv) != 2:
        print("Uso: python send_icmp_packets.py <texto>")
        sys.exit(1)

    texto = sys.argv[1]

    # Identificación inicial y secuencia
    id = 1
    seq = 1

    for char in texto:
        # Inicializa el payload con el byte que representa el carácter cifrado
        payload = bytes([ord(char)])

        # Agregar los 5 bytes nulos después del byte del carácter cifrado
        payload += b'\x00\x00\x00\x00\x00'

        # Llenar el patrón desde 0x10 al 0x37
        for i in range(0x10, 0x38):
            payload += bytes([i])

        # Envía el paquete ICMP y obtiene la respuesta
        response = send_icmp_packet("8.8.8.8", payload, id, seq)

        print(f"Enviado: {char}, ID: {id}, Seq: {seq}, Tiempo: {response.time:.4f} segundos")

        # Incrementa la secuencia y la identificación
        seq += 1
        id += 1

if __name__ == "__main__":
    main()
