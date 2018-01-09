"""Ayuda a construir proyectos de Visual Studio desde la línea de comando"""

import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('proyecto', type=str, default=None,
                    help='Fichero del proyecto o solución, si se quiere indicar manualmente')

args = parser.parse_args()
