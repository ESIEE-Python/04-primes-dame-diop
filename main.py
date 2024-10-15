from math import sqrt

#### Fonction secondaire


def isprime(p):

    # votre code ici

    if p < 2:
        return False

    if p == 2:
        return False

    # si p a un divisuer autre que 1 et lui meme il est pas premier
    if p % 2 == 0:
        return False

    # si p a unn diviseur entre 3 et 
    for i in range(3, int(sqrt(p)) + 1, 2):
        if p % i == 0:
            return False
        else:
            return True

        pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
