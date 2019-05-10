from random import randint
from csv import *
from scipy.spatial import distance
import sys


def generator(densite):
    xMain = 1024
    yMain = 800

    taille = 50

    if (densite == "petite"):
        nb = 30
        file = open("littleBubble.csv", "w")
    else:
        nb = 60
        file = open("bigBubble.csv", "w")

    filewriter = writer(file, delimiter=",", quotechar='"')

    targets = list()
    for i in range(nb):
        while(True):
            x = randint(taille, xMain-taille)
            y = randint(taille, yMain-taille)

            if(isPossible(targets, x, y, taille)):
                filewriter.writerow([str(x), str(y), str(taille)])
                targets.append((x, y))
                break

    file.close()


def isPossible(targets, x, y, taille):
    for target in targets:
        a = (target[0], target[1])
        b = (x, y)
        d = distance.euclidean(a, b)
        if (d < taille + 10):
            return False

    return True


def main(argv):
    densite = argv[1]
    generator(densite)


if __name__ == "__main__":
    print("execution du programme")
    main(sys.argv)
