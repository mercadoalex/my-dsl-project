# script2.py

from dsl.parser import DSLParser

def main():
    dsl_parser = DSLParser()
    
    # Sample DSL commands
    commands = [
        "command1 arg1 arg2",
        "command2 arg1",
        "command3"
    ]
    
    for command in commands:
        try:
            parsed_command = dsl_parser.parse(command)
            result = dsl_parser.evaluate(parsed_command)
            print(f"Result of '{command}': {result}")
        except Exception as e:
            print(f"Error processing command '{command}': {e}")

if __name__ == "__main__":
    main()