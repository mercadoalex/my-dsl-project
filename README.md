# My DSL Project

## Overview
This project implements a Domain Specific Language (DSL) designed for educational purposes. The DSL allows users to define and execute commands through a simple syntax, making it easier to understand the principles of language parsing and execution.

## Project Structure
```
my-dsl-project
├── src
│   ├── dsl
│   │   └── parser.py       # Implementation of the DSL parser
│   ├── scripts
│   │   ├── script1.py      # Basic script utilizing the DSL
│   │   └── script2.py      # Another script demonstrating DSL features
│   └── utils
│       └── helpers.py      # Utility functions for parsing and execution
├── tests
│   └── test_parser.py      # Unit tests for the DSL parser
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Setup
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-dsl-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the DSL, you can run the provided scripts located in the `src/scripts` directory. Each script demonstrates different aspects of the DSL and how to interact with it.

### Example
Here is a simple example of how to use the DSL:

1. Open `script1.py` or `script2.py` to see sample commands.
2. Modify the commands as needed and run the script to see the output.

## Testing
To run the unit tests for the DSL parser, execute the following command:
```
python -m unittest tests/test_parser.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.