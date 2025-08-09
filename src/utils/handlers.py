def imprimir(args):
    """
    Imprime el mensaje proporcionado por el usuario.
    """
    output = " ".join(args)
    print(output)
    return f"IMPRIMIR: {output}"

def sumar(args):
    """
    Suma dos números proporcionados como argumentos.
    """
    try:
        result = int(args[0]) + int(args[1])
        print(f"Resultado: {result}")
        return f"SUMAR: {result}"
    except (ValueError, IndexError):
        return "Error: argumentos inválidos para SUMAR"

def saludar(args):
    """
    Saluda al usuario con el nombre proporcionado.
    """
    if args:
        saludo = f"Hola, {args[0]}!"
        print(saludo)
        return f"SALUDAR: {saludo}"
    return "Error: falta el nombre para SALUDAR"

def ir_a_medium(args):
    """
    Genera y muestra una URL clickeable al perfil de Medium del usuario.
    Si no se proporciona el nombre de usuario, lo solicita por consola.
    """
    if args:
        username = args[0]
    else:
        username = input("Por favor, ingrese el nombre de usuario de Medium: ").strip()
    if username:
        url = f"https://{username}.medium.com/"
        print(f"Abre tu perfil de Medium aquí: {url}")
        return f"MEDIUM: {url}"
    else:
        return "Error: falta el nombre de usuario para Medium"