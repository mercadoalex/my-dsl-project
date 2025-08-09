from dsl.parser import DSLParser

def main():
    dsl_parser = DSLParser()

    # Comandos de ejemplo en español para ilustrar el uso del DSL
    commands = [
        "IMPRIMIR Hola Mundo",
        "SUMAR 5 10",
        "SALUDAR Juan",
        "IR A mi perfil de Medium",
        "GOTO mi perfil de Medium"
    ]

    for command in commands:
        # Parse returns a list of commands; we process each one
        parsed_commands = dsl_parser.parse(command)
        for parsed_command in parsed_commands:
            result = dsl_parser.evaluate(parsed_command)
            print(f"Comando: {parsed_command} | Resultado: {result}")

if __name__ == "__main__":
    main()