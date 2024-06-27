import socket
import pymysql


def manejar_cliente(conn, cursor, connection):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            mensaje = data.decode()
            print(f"Recibido: {mensaje}")

            # Aquí puedes procesar el mensaje y hacer operaciones con la base de datos
            # Por ejemplo, insertar el mensaje en una tabla:
            cursor.execute(mensaje)
            connection.commit()
            resultados = cursor.fetchall()
            print(resultados)
            respuesta = "Mensaje recibido y almacenado en la base de datos"

            conn.sendall(respuesta.encode())

    except ConnectionResetError:
        print("Conexión interrumpida por el cliente")
    except Exception as e:
        print(f"Error al manejar al cliente: {e}")
    finally:
        conn.close()


def iniciar_servidor():
    # Configuración de la base de datos
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            db="segundaentrega"
        )
        cursor = connection.cursor()

    except pymysql.MySQLError as e:
        print(f"Error al conectar con la base de datos: {e}")
        return

    # Configuración del servidor
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Servidor escuchando en el puerto", port)

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Conexión aceptada de {addr}")
            manejar_cliente(client_socket, cursor, connection)
    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        # Cierra la conexión de la base de datos cuando termines
        cursor.close()
        connection.close()
        server_socket.close()


if __name__ == "__main__":
    iniciar_servidor()