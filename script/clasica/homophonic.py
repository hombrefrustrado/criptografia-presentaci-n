import argparse
import random

# Mapa homofónico ejemplo: cada letra tiene varios posibles códigos
HOMOPHONIC_MAP = {
    'A': [11, 12, 13],
    'B': [21, 22],
    'C': [31, 32, 33, 34],
    'D': [41, 42],
    'E': [51, 52, 53, 54, 55],
    'F': [61, 62],
    'G': [71, 72],
    'H': [81, 82, 83],
    'I': [91, 92, 93],
    'J': [101],
    'K': [111, 112],
    'L': [121, 122, 123],
    'M': [131, 132],
    'N': [141, 142, 143],
    'O': [151, 152, 153],
    'P': [161, 162],
    'Q': [171],
    'R': [181, 182, 183],
    'S': [191, 192, 193, 194],
    'T': [201, 202],
    'U': [211, 212],
    'V': [221],
    'W': [231, 232],
    'X': [241],
    'Y': [251, 252],
    'Z': [261],
    ' ': [1, 110, 120, 187]
}

# Crear un mapa inverso para descifrar
INV_MAP = {}
for k, vlist in HOMOPHONIC_MAP.items():
    for code in vlist:
        INV_MAP[str(code)] = k

def cifrado_homofonico(args):
    mensaje = args.m.upper()
    resultado = []
    for letra in mensaje:
        if letra in HOMOPHONIC_MAP:
            codigo = random.choice(HOMOPHONIC_MAP[letra])
            resultado.append(str(codigo))
        else:
            resultado.append(letra)
    print(" ".join(resultado))

def descifrado_homofonico(args):
    texto = args.m.split()
    resultado = ''
    for codigo in texto:
        letra = INV_MAP.get(codigo, codigo)
        resultado += letra
    print(resultado)

def build_parser():
    parser = argparse.ArgumentParser(description='Cifrado Homofónico')
    sub = parser.add_subparsers(dest='cmd')

    # Cifrar
    cifrar_parser = sub.add_parser('cifrar', help='Cifrar mensaje')
    cifrar_parser.add_argument('-m', type=str, required=True, help='Mensaje a cifrar')
    cifrar_parser.set_defaults(func=cifrado_homofonico)

    # Descifrar
    descifrar_parser = sub.add_parser('descifrar', help='Descifrar mensaje')
    descifrar_parser.add_argument('-m', type=str, required=True, help='Mensaje cifrado (números separados por espacio)')
    descifrar_parser.set_defaults(func=descifrado_homofonico)

    return parser

if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
    else:
        args.func(args)
