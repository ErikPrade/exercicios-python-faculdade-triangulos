from colorama import Fore, Style, init
init()

# Entrada de dados
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# PRIMEIRO TESTE: É um triângulo?
if (a + b > c) and (a + c > b) and (b + c > a):
    
    # SEGUNDO TESTE: São todos iguais?
    if a == b and b == c:
        print(Fore.GREEN + "Equilátero" + Style.RESET_ALL)
    else:
        # Se não são todos iguais, vamos ver se são todos diferentes
        if a != b and b != c and a != c:
            print(Fore.YELLOW + "Escaleno" + Style.RESET_ALL)
        else:
            # Se não é equilátero nem escaleno, só pode ser...
            print(Fore.BLUE + "Isósceles" + Style.RESET_ALL)

else:
    # Caso falhe no primeiro teste de todos
    print(Fore.RED + "Não forma um triângulo" + Style.RESET_ALL)

