from colorama import Fore, Style, init
init()
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print(Fore.GREEN + "Equilátero" + Style.RESET_ALL)
    else:
        if a != b and b != c and a != c:
            print(Fore.YELLOW + "Escaleno" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + "Isósceles" + Style.RESET_ALL)
else:
    print(Fore.RED + "Não forma um triângulo" + Style.RESET_ALL)

