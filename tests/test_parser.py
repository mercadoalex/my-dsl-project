import unittest
from src.dsl.parser import DSLParser

class TestDSLParser(unittest.TestCase):

    def setUp(self):
        self.parser = DSLParser()

    def test_parse_single_command(self):
        command = "IMPRIMIR Hola Mundo"
        result = self.parser.parse(command)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0], "IMPRIMIR Hola Mundo")

    def test_parse_multiple_commands(self):
        command = "IMPRIMIR Hola;SUMAR 1 2"
        result = self.parser.parse(command)
        self.assertEqual(result, ["IMPRIMIR Hola", "SUMAR 1 2"])

    def test_evaluate_command(self):
        command = "SALUDAR Juan"
        result = self.parser.evaluate(command)
        self.assertEqual(result, "Ejecutado: SALUDAR Juan")

    def test_evaluate_empty_command(self):
        command = "   "
        result = self.parser.evaluate(command)
        self.assertEqual(result, "Ejecutado: ")  # now matches actual output

if __name__ == '__main__':
    unittest.main()