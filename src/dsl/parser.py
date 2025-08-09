from utils import handlers

class DSLParser:
    def __init__(self):
        # Inicializa el parser con un diccionario de comandos y una lista de comandos parseados
        self.commands = []
        self.command_map = {
            "IMPRIMIR": handlers.imprimir,
            "SUMAR": handlers.sumar,
            "SALUDAR": handlers.saludar,
            "IR_A_MEDIUM": handlers.ir_a_medium,  # Nuevo comando agregado
        }

    def parse(self, input_string):
        """
        Parsea el string de entrada en comandos individuales.
        Asume que los comandos están separados por punto y coma (;).
        """
        # Elimina espacios y divide por punto y coma
        self.commands = input_string.strip().split(';')
        return self.commands

    def evaluate(self, command):
        """
        Evalúa un solo comando parseado.
        Llama al handler correspondiente si existe, si no, devuelve mensaje de desconocido.
        """
        parts = command.strip().split()
        if not parts:
            return "Comando vacío"
        cmd = parts[0].upper()
        args = parts[1:]
        handler = self.command_map.get(cmd)
        if handler:
            return handler(args)
        else:
            return f"Comando desconocido: {command.strip()}"