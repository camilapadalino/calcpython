def delta(a,b,c):
    delta = b**2 - 4 * a *c
    if delta < 0:
        print("Não há raízes pois o delta é negativo.")
    elif delta == 0:
        x = -b/(2*a)
    else:
        xis1 = (-b + delta) / (2 * a)
        xis2 = (-b - delta) / (2 * a)
        print(f'A primeira raiz vale = {xis1} e a segunda vale = {xis2}')
    equacaoX =  -b / (2 * a)
    equacaoY = - delta/(4 * a)
    print(f'O X e Y da equação é {equacaoX} e {equacaoY}')



a = int(input("Insira um valor: "))
b = int(input("Insira um outro valor: "))
c = int(input("Insira um último valor: "))
delta(a,b,c)

