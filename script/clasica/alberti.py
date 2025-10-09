import argparse

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar_alberti(args):
    mensaje = args.m.upper().replace(" ", "")
    clave = args.clave.upper()
    resultado = ""
    disco_interno = list(ALFABETO)
    
    # Posición inicial del disco interno según la primera letra de la clave
    offset = ALFABETO.index(clave[0]) if clave else 0
    disco_interno = disco_interno[offset:] + disco_interno[:offset]

    for i, letra in enumerate(mensaje):
        if letra in ALFABETO:
            index = ALFABETO.index(letra)
            resultado += disco_interno[index]
            # Opcional: rotar disco 1 posición después de cada letra
            disco_interno = disco_interno[1:] + disco_interno[:1]
        else:
            resultado += letra
    print(resultado)

def descifrar_alberti(args):
    mensaje = args.m.upper().replace(" ", "")
    clave = args.clave.upper()
    resultado = ""
    disco_interno = list(ALFABETO)
    
    offset = ALFABETO.index(clave[0]) if clave else 0
    disco_interno = disco_interno[offset:] + disco_interno[:offset]

    for letra in mensaje:
        if letra in ALFABETO:
            index = disco_interno.index(letra)
            resultado += ALFABETO[index]
            disco_interno = disco_interno[1:] + disco_interno[:1]
        else:
            resultado += letra
    print(resultado)

def build_parser():
    parser = argparse.ArgumentParser(description='Cifrado del disco de Alberti')
    sub = parser.add_subparsers(dest='cmd')

    # Subcomando cifrar
    cifrar_parser = sub.add_parser('cifrar', help='Cifrar mensaje')
    cifrar_parser.add_argument('-m', type=str, required=True, help='Mensaje a cifrar')
    cifrar_parser.add_argument('-k', '--clave', type=str, required=True, help='Letra inicial del disco interno')
    cifrar_parser.set_defaults(func=cifrar_alberti)

    # Subcomando descifrar
    descifrar_parser = sub.add_parser('descifrar', help='Descifrar mensaje')
    descifrar_parser.add_argument('-m', type=str, required=True, help='Mensaje cifrado')
    descifrar_parser.add_argument('-k', '--clave', type=str, required=True, help='Letra inicial del disco interno')
    descifrar_parser.set_defaults(func=descifrar_alberti)

    return parser

if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
    else:
        args.func(args)
