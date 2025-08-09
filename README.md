# My DSL Project

## Overview
This project implements a Domain Specific Language (DSL) designed for educational purposes. The DSL allows users to define and execute commands through a simple syntax, making it easier to understand the principles of language parsing and execution. The project is modular, with each command handled by a separate function, and includes an interactive CLI.

## Project Structure
```
my-dsl-project/
├── src/
│   ├── dsl/
│   │   └── parser.py          # Core parser logic and command dispatch
│   ├── scripts/
│   │   ├── script1.py         # Example usage with predefined commands
│   │   ├── script2.py         # Another example or test script
│   │   └── cli.py             # Interactive CLI for entering commands
│   └── utils/
│       ├── handlers.py        # Functions implementing each DSL command
│       └── helpers.py         # Utility functions (tokenization, validation, etc.)
├── tests/
│   └── test_parser.py         # Unit tests for the parser
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Supported Commands

- `IMPRIMIR <mensaje>`  
  Imprime el mensaje proporcionado.  
  Ejemplo: `IMPRIMIR Hola Mundo`

- `SUMAR <número1> <número2>`  
  Suma dos números y muestra el resultado.  
  Ejemplo: `SUMAR 5 10`

- `SALUDAR <nombre>`  
  Saluda al usuario con el nombre dado.  
  Ejemplo: `SALUDAR Juan`

- `IR_A_MEDIUM <usuario>`  
  Muestra y retorna la URL de tu perfil de Medium. Si no das usuario, te lo pedirá.  
  Ejemplo: `IR_A_MEDIUM alexmarket`

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd my-dsl-project
   ```

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Interactive CLI

To use the DSL interactively, run:
```sh
export PYTHONPATH=src
python src/scripts/cli.py
```
or
```sh
cd src
python -m scripts.cli
```
You can then enter commands like `IMPRIMIR Hola Mundo`, `SUMAR 5 10`, `SALUDAR Juan`, or `IR_A_MEDIUM alexmarket`.

### Example Scripts

You can also run the example scripts:
```sh
python src/scripts/script1.py
python src/scripts/script2.py
```

## Testing

To run the unit tests for the DSL parser, execute:
```sh
python -m unittest tests/test_parser.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Article
https://alexmarket.medium.com/a-dsl-from-scratch-with-python-3377ae3aa686