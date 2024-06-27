import socket

def enviar_mensaje(mensaje):
    host = 'localhost'
    port = 12345

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        client_socket.sendall(mensaje.encode())

        data = client_socket.recv(1024)
        print("Recibido del servidor:", data.decode())
        print(f"El mensaje enviado y almacenado fue el siguiente:{mensaje}")
    except ConnectionResetError:
        print("Conexión interrumpida por el servidor")
    except Exception as e:
        print(f"Error en el cliente: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    sentencias={
        "SELECT empl_primer_nombre, empl_segundo_nombre FROM empleados WHERE empl_ID=1"
    }
    for element in sentencias:
        mensaje = element
        enviar_mensaje(mensaje)