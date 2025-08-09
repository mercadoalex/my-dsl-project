from dsl.parser import DSLParser

def main():
    dsl_parser = DSLParser()
    while True:
        user_input = input("Ingrese un comando DSL (o 'salir' para terminar): ")
        if user_input.lower() == "salir":
            break
        parsed_commands = dsl_parser.parse(user_input)
        for parsed_command in parsed_commands:
            result = dsl_parser.evaluate(parsed_command)
            print(f"Resultado: {result}")

if __name__ == "__main__":
    main()