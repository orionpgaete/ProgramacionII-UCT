class Notificacion:
    def __init__(self, destinatario):
        self._destinatario = destinatario

    def enviar(self, mensaje):
        return f"Notificacion para {self._destinatario}: {mensaje}"

class Correo(Notificacion):
    def enviar(self,mensaje):
        return f"Correo: {self._destinatario}: {mensaje}"

class SMS(Notificacion):
    def enviar(self,mensaje):
        return f"SMS: {self._destinatario}: {mensaje}"




def main():

if __name__ == "__main__":
    main()