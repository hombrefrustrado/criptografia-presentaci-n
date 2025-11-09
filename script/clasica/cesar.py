import argparse

def letraMayuscula(letra):
    return ord(letra) >= 65 and ord(letra) < 91

def cifradoCesarAlfabetoInglesMAYGeneralizado(args):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    cadena = args.m
    pos = args.c
    # Definir la nueva cadena resultado
    resultado = ''

    i = 0
    while i < len(cadena):
        
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + pos) % 26) + 65

        elif( ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + pos) % 26) + 97
        else:
            ordenCifrado = ordenClaro
        resultado = resultado + chr(ordenCifrado)
        i = i + 1

    print(resultado)

def descifradoCesarAlfabetoInglesMAYGeneralizado(args):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    cadena = args.m
    pos = args.c

    resultado = ''

    i = 0
    while i < len(cadena):
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0

        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) - pos) % 26) + 65

        elif( ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) - pos) % 26) + 97
        else:
            ordenCifrado = ordenClaro
        resultado = resultado + chr(ordenCifrado)
        i = i + 1

    print(resultado)
    
def build_parser():
    parser = argparse.ArgumentParser(description='Cifrado cesar, necesario especificar le numero de saltos')
    sub = parser.add_subparsers(dest='cmd')
    
    cifrar_parser = sub.add_parser('cifrar', help='Cifrar mensaje con César')
    cifrar_parser.add_argument('-c', type=int, default=3, help='Cantidad de saltos en el cifrado')
    cifrar_parser.add_argument('-m', type=str, required=True, help='Mensaje a cifrar')
    cifrar_parser.set_defaults(func=cifradoCesarAlfabetoInglesMAYGeneralizado)

    descifrar_parser = sub.add_parser('descifrar', help='Descifrar mensaje con César')
    descifrar_parser.add_argument('-c', type=int, default=3, help='Cantidad de saltos en el descifrado')
    descifrar_parser.add_argument('-m', type=str, required=True, help='Mensaje a descifrar')
    descifrar_parser.set_defaults(func=descifradoCesarAlfabetoInglesMAYGeneralizado)
    
    return parser

if __name__== '__main__':
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
    else:
        args.func(args)