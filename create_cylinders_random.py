# Create randomly generated cylinders within a 2-D domain
# Bulut Tekgul, Aalto University, 2019

import sys


def main(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-nCyl",
        action="store",
        dest="cylNumber",
        required=True,
        help="Number of cylinders",
    )

    parser.add_argument("-x0", action="store", dest="x0", required=True)
    parser.add_argument("-x1", action="store", dest="x1", required=True)
    parser.add_argument("-y0", action="store", dest="y0", required=True)
    parser.add_argument("-y1", action="store", dest="y1", required=True)

    parser.add_argument(
        "-rad", action="store", dest="radius", required=True, help="Cylinder radius"
    )

    parser.add_argument(
        "-tol",
        action="store",
        dest="tolerance",
        required=True,
        help="Minimum distance between 2 cylinders",
    )
    args = parser.parse_args()


if __name__ == "__main__":
    locals().update(main(sys.argv[1:]))
