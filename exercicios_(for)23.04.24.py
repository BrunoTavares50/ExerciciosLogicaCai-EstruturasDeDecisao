# -*- coding: utf-8 -*-
"""Atividades (for)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nmHI3nXxg1gt9YFgAGpiYkqSTwQfna48
"""

maior_numero = 0
for contador in range(5):
  numero = int(input("Digite um numero: "))
  if numero > maior_numero:
   maior_numero = numero

print("O maior numero é:",maior_numero)

for contador in range(1000, 2001):
  if contador % 11 == 2:
   print(contador)

soma = 0
for i in range(5):
  numero = float(input(f"Digite o {i+1}º numero: "))
  soma += numero #soma = soma + numero
  media = soma/5
print(f"A soma dos numeros é: {soma}")
print(f"A media dos numeros é: {media}")

#Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
numero = int(input("Digite um numero: "))
for i in range(0,11):
 tabuada = numero * i
 print(f" {numero} x {i} = {tabuada}")

#Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.
for numero in range(1,11):
  print("--------------")
  print(f"{numero}")
  print()
  for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    print()

#6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
for i in range(1, 21):
 print(i)

#7. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for numero in range(1,51,2):
  print(f"{numero}")

#8. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
num1 = int(input("Digite o 1º numero inteiro: "))
num2 = int(input("Digite o 2º numero inteiro: "))
for numero in range(num1+1, num2):
  print(numero)

#9. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado ofaturamento.
lojaB = 54000
lojaA = 0
for i in range(5):
 cliente = float(input(f"Digite o seu {i+1}º faturamento: "))
 lojaA += cliente
if lojaA > lojaB:
  diferenca = lojaA - lojaB
  print(f"Foi superado o valor em {diferenca} reais.")
else:
  print("O faturamento da loja A não superou o faturamento da loja B")

#10. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
par = 0
impar = 0
for i in range(10):
  numero = int(input(f"Digite o {i+1}º numero: "))
  if numero % 2 == 0:
     par += 1
  else:
     impar += 1
print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")

salario = float(input("Digite o salario inicial do funcionario: "))
percentual = 0.015

for i in range(1996,2025):
  aumento = salario * percentual
  salario += aumento
  percentual *= 2
  print(f"Salario em {i} = {salario:.2f}")

#12. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
for i in range(99999):
  nota = int(input(f"Digite uma nota entre zero e dez: "))
  if nota >= 0 and nota <= 10:
   print(f"Nota valida: {nota}")
   break
  else:
   print(f"Nota invalida.")

#13. Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500. A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%.
valor = float(input("Digite o valor da compra: "))
contagem = 1 # inicia a variavel de contagem com valor 1

if valor >= 600 and contagem: # verifica se o valor da compra é maior que 600 e se a contagem é diferente de zero
#o que sempre sera verdadeiro, pois a contagem comeca com 1
  reduzido = valor - 500 # calcula o valor reduzido subtraindo 500 do valor da compra
  if reduzido >= 100 or contagem <= 24: # vifica se o valor reduzido é maior ou igual a 100 ou se a contagem é menor ou igual a 24
   for x in range(999): # loop que itera 999 vezes
    contagem += 1 # incrementando a contagem
    reduzido -= 100 # reduz o valor em R$100
    if reduzido < 100 or contagem == 24: # verifica se o valor reduzido é menor que R$100 ou se a contagem é igual a 24
     break # sai do loop

porcentagem = contagem/100
desconto = valor * porcentagem
final = valor - desconto
print(f"O produto de R${valor:.2f} ficará a partir de R${final} com {contagem:.0f}% de desconto")

#14. Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
#a) A quantidade de pessoas em cada faixa etária;
#b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:
# Até 15 anos
# De 16 a 30 anos
# De 31 a 45 anos
# De 46 a 60 anos
# Acima de 61 anos
idade_ate_15 = 0
idade_16_30 = 0
idade_31_45 = 0
idade_46_60 = 0
idade_acima_61 = 0
for i in range(15):
 idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
 if idade <= 15:
  idade_ate_15 += 1
 elif idade <= 30:
  idade_16_30 += 1
 elif idade <= 45:
  idade_31_45 += 1
 elif idade <= 60:
  idade_46_60 += 1
 elif idade >= 61:
  idade_acima_61 += 1
total_pessoas = idade_ate_15 + idade_16_30 + idade_31_45 + idade_46_60 + idade_acima_61
percentagem_primeira_faixa = (idade_ate_15 / total_pessoas) * 100
percentagem_segunda_faixa = (idade_acima_61 / total_pessoas) * 100
print()
print("Quantidade de pessoas em cada faixa etária:")
print(f"Até 15 anos: {idade_ate_15}")
print(f"De 16 a 30 anos: {idade_16_30}")
print(f"De 31 a 45 anos: {idade_31_45}")
print(f"De 46 a 60 anos: {idade_46_60}")
print(f"Acima de 61 anos: {idade_acima_61}")
print()
print(f"Percentagem de pessoas na primeira faixa etária: {percentagem_primeira_faixa}%")
print(f"Percentagem de pessoas na primeira faixa etária: {percentagem_segunda_faixa}%")

#15. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
resultado = 1

for i in range(expoente):
  if base == 1:
    resultado = base
  else:
    resultado *= base
print(f"Resultado {resultado}")

#16. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
n = int(input("Digite um numero: "))
for numerotestado in range(1,n+1):
  for numerodivisor in range(numerotestado):
    print(f"{numerotestado}/{numerodivisor+1} = {numerotestado%(numerodivisor+1)}")
    if numerotestado % (numerodivisor+1) == 0:
      if 1 != numerodivisor+1 != numerotestado:
        print("Não é primo")
        break
      elif numerodivisor+1 == numerotestado:
        print("É primo")