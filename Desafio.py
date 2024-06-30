CONSTANTE_BONUS = 1000

nome = input("Digite o seu nome: ")
salario = float(input("Insira o valor do seu salário: "))
bonus  = float(input ("Digite o seu bonus: "))
                

valor_do_bonus = CONSTANTE_BONUS + salario * bonus

print (f"O usuário {nome} possui o bonus de {valor_do_bonus}")