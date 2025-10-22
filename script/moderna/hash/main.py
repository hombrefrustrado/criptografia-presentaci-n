import argparse
from Cryptodome.Hash import SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_256, SHA3_512

HASH_METHODS = {
    "SHA1": SHA1,
    "SHA224": SHA224,
    "SHA256": SHA256,
    "SHA384": SHA384,
    "SHA512": SHA512,
    "SHA3-256": SHA3_256,
    "SHA3-512": SHA3_512,
}


def hash_text(args):
    mensaje = args.m
    metodo = args.t.upper()

    if metodo in HASH_METHODS:
        h_class = HASH_METHODS[metodo]
        h = h_class.new(data=mensaje.encode('utf-8'))
        print(f"Hash {metodo} de '{mensaje}':\n{h.hexdigest()}")
    else:
        raise ValueError("Metodo no encontrado")

def generarhashImagen(args):
    imagen = args.i1
    metodo = args.t.upper()
    h_class = HASH_METHODS[metodo]

    with open(imagen, "rb") as f:  # 'rb' = read bytes
        dataImagen1 = f.read()
    h = h_class.new(data=dataImagen1)
    print(f"El hash de la imagen es:\n{h.hexdigest()}")
def compararImagen(args):
    imagen1 = args.i1
    imagen2 = args.i2

    with open(imagen1, "rb") as f:  # 'rb' = read bytes
        dataImagen1 = f.read()
    h = SHA256.new(data=dataImagen1)
    hashImagen1 = h.hexdigest()

    with open(imagen2, "rb") as f:  # 'rb' = read bytes
        dataImagen2 = f.read()
    h = SHA256.new(data=dataImagen2)
    hashImagen2 = h.hexdigest()

    if (hashImagen1==hashImagen2):
        print("Las imagenes que has introducido son iguales")
    else:
        print("Las imagenes son diferentes")

def build_parser():
    parser = argparse.ArgumentParser(description="Calculo del Hash SHA")
    sub = parser.add_subparsers(dest='cmd')

    haseo_parser = sub.add_parser('hash', help='indica el metodo de hasheo')
    haseo_parser.add_argument('-t', 
                              type=str, 
                              required=True,
                              choices=HASH_METHODS.keys(),
                              help=f"Método de hash disponible ({', '.join(HASH_METHODS.keys())}"
                              )
    
    haseo_parser.add_argument('-m', type=str, required=True, help='Mensaje a hashear')
    haseo_parser.set_defaults(func=hash_text)

    hash_imagen = sub.add_parser('hashImagen', help="Incluye el metodo de hasheo y la imagen a hashear")
    hash_imagen.add_argument('-t', 
                              type=str, 
                              required=True,
                              choices=HASH_METHODS.keys(),
                              help=f"Método de hash disponible ({', '.join(HASH_METHODS.keys())}"
                              )
    hash_imagen.add_argument('-i1', type=str, required=True, help='imagen a hashear')
    hash_imagen.set_defaults(func=generarhashImagen)

    comparador_parser = sub.add_parser('comparar', help='indica dos imagenes para comparar')
    comparador_parser.add_argument('-i1', type=str, required=True, help='imagen a hashear')
    comparador_parser.add_argument('-i2', type=str, required=True, help='imagen a hashear')
    comparador_parser.set_defaults(func=compararImagen)
    
    
    return parser

if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
    else:
        args.func(args)