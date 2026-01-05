#%%
import math
#%%
# #### Inteiros (`int`)
#%%
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
n1 = int(input(("primeiro número: ")))
n2 = int(input("segundo núemro:"))
soma = n1 + n2
print (f'soma: {soma}')
#%%
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numerp = int(input("insira um numero:"))
resto = numerp % 5
print(f'resto da divisão por 5 é: {resto}')
#%%
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
n1 = int(input("primeiro número: "))
n2 = int(input("segundo número:"))
multiplicacao = n1 * n2
print(f'resultado: {multiplicacao}')
#%%
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)
#%%
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("numero:"))
quadrado= numero ** 2
print(f'quadrado: {quadrado}')
#%%
# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
n1 = float(input("primeiro numero: "))
n2 = float(input("segundo numero: "))
soma = n1 + n2
print(f'soma: {soma}')
#%%
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n1 = float(input("primeiro numero: "))
n2 = float(input("segundo numeor: "))
media = (n1 + n2) / 2
print(f"média: {media}")
#%%
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = numero_base ** expoente
print(f"O resultado de {numero_base} elevado a {expoente} é: {potencia}")

#%%
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")

#%%
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
numero_raio = float(input("Digite o raio do círculo: "))
area_circulo = math.pi * numero_raio ** 2
print(f"A área do círculo é: {area_circulo:.2f}")

#%%
#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)
#%%
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
s = str(input("digite um texto: "))
print(s.upper())

#%%
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as 
# letras minúsculas.

nome_completo = str(input("Digite seu nome completo: "))
print(nome_completo.lower())

#%%
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, 
# imprima esta frase sem espaços em branco no início e no final.
frase = str(input("Digite uma frase: "))
print(frase.strip())

#%%
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, 
# em seguida, imprima o dia, o mês e o ano separadamente.
data = input("digite uma data no formato dd/mm/aaaa: ")
dia = data.split("/")[0]
print(f"Dia: {dia}")
mes = data.split("/")[1]
print(f"Mês: {mes}")
ano = data.split("/")[2]
print(f"Ano: {ano}")
print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")

#%%
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
s1 = str(input("primeira string: "))
s2 = str(input("segunda string: "))
concatenacao = s1 + s2
print(f"concatenação: {concatenacao}")
#%%
# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação