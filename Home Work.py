#!/bin/python3

print("###########################      Bem-vindo a Empyre cyborg cecurity     ##################################")

print("")

# Dicionario de certificações disponíveis e seus preços
cursos = {
    "Network Penetration Testing": 13500,
    "Network Defender": 13500,
    "Network Pen Testing Advanced": 13500,
    "Web Aplication Pen Testing": 13500,
    "Web Aplication Defender": 13500,
}	

# Pergunta o nome e a idade do estudante
nome = input("Qual é o seu nome? ")
print("")
age = int(input("Quantos anos você tem? "))


# Verifica se o estudante é maior de idade
if age < 18:
    print("Desculpe, você precisa ter 18 anos ou mais para se registrar.")
    exit()

print("")


# Exibe as certificações disponíveis e pede ao estudante que escolha uma
print("Temos as seguintes certificações disponíveis:")
	
print("")


for curso, preco in cursos.items():
    print(curso  +  " : " + str(preco) + "-MT")

print("")


escolha_curso = input("Qual certificação você gostaria de obter? ")

print("")


# Verifica se a certificação escolhida está na lista
if escolha_curso not in cursos:
    print("Certificação inválida.")
    exit()

# Calcula o preço da certificação escolhida
curso_preco = cursos[escolha_curso]


print("")

# Pede ao estudante que faça o pagamento
pagamento = float(input("O preço da certificação é " + str(curso_preco) + " MT" + ". Por favor, insira o valor pago: "))

print("")

# Verifica se o pagamento é suficiente
if pagamento < curso_preco:
    print("Pagamento insuficiente.")
    exit()

print("")

# Exibe o recibo
print("##################################################   Recibo:  ###################################################")
print("")
print("Nome: " + nome)
print("")
print("Certificação: " + escolha_curso)
print("")
print("Preço pago: R$" + str(pagamento))
print("")

# Verifica se o pagamento foi feito com sucesso
if pagamento == curso_preco:
    print("#####################################   Pagamento efetuado com sucesso   ########################################")
else:
    change = pagamento - curso_preco
    print("Pagamento efetuado com sucesso. Troco: R$" + str(change))
print("")

print("##########################################   Gratos pela preferencia   ##########################################")