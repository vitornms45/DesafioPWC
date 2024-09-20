

# DESAFIO DE CODIGO_PWC_PROGRAMA DE ESTÁGIO EM TECH

# DESAFIO DE CÓDIGO
# Pedimos que você resolva o seguinte desafio de código como parte de nosso
# processo de seleção. Você precisará apresentar o resultado desse desafio na entrevista.
# Endereço
# Um provedor de endereços retorna endereços apenas com ruas concatenadas,
# nomes e números em uma única string. Nosso próprio sistema, por outro lado, tem
# campos específicos para armazenar o nome da rua e o número da rua.
# Portanto, se faz necessário escrever um código simples que processe a entrada e retorne esses campos
# na saída.
# Entrada: string de endereço com os dados concatenados.
# Saída: string da rua e string do número da rua.

# 1. Casos Simples:
# a. “Miritiba 339” -> {“Miritiba”, “339”}
# b. “Babaçu 500” -> { “Babaçu”, “500”}
# c. “Cambuí 804B” -> {“Cambuí”, “123B”}

# 2. Considere os casos mais complicados:
# a. “Rio Branco 23” -> {“Rio Branco”, “23”}
# b. “Quirino dos Santos 23 b” -> {“Quirino dos Santos”, ”23 b”}

# 3. Considere endereços de outros países (casos complexos)
# a. “4, Rue de la République” -> {"Rue de la République", "4"}
# b. “100 Broadway Av” -> {"Broadway Av", "100"}
# c. “Calle Sagasta, 26” -> {“Calle Sagasta”, “26”}
# d. “Calle 44 No 1991” -> {“Calle 44”, “No 1991”}

# Sua tarefa:
# Escreva uma aplicação executável, na linguagem de programação de sua escolha, incluindo casos de
# teste, utilizando os exemplos informados acima.
# Esteja preparado para apresentar e explicar sua solução para o entrevistador.
# Boa Sorte!
# Equipe PwC.

def extrair_endereco(endereco):

    if type(endereco) is not str:
        raise TypeError('Endereço deve ser uma string')

    # padronizar as strings
    endereco = endereco.replace(",", "").strip()
    
    # Fatiamento da string
    palavras = endereco.split()
    
    # Se a primeira palavra for "No", o número pode estar nas próximas palavras

    if palavras[0].lower() == 'no':
        numero = palavras[0] + " " + palavras[1]
        rua = " ".join(palavras[2:]).strip()  # O restante é a rua

    elif palavras[0].isdigit():
        # Se a primeira palavra for um número, é um endereço onde o número está no início
        numero = palavras[0]
        rua = " ".join(palavras[1:]).strip()

    else:
        # Certezas - Número está no final
        # Verificar se as últimas duas palavras formam o número com uma possível letra (ex: "23 b")
        if palavras[-2].isdigit() or palavras[-2].lower() == 'no':
            numero = " ".join(palavras[-2:]).strip()
            rua = " ".join(palavras[:-2]).strip()
        else:
            numero = palavras[-1]
            rua = " ".join(palavras[:-1]).strip()
    

    return rua, numero

# Testes com base nos exemplos fornecidos e com ajustes para "No" com letras

enderecos = [
    "Miritiba 339",
    "Babaçu 500",
    "Cambuí 804B",
    "Rio Branco 23",
    "Quirino dos Santos 23 b",
    "4, Rue de la République",
    "100 Broadway Av",
    "Calle Sagasta, 26",
    "Calle 44 No 1991",
    "No 56, Avenida Paulista",

]


for endereco in enderecos:
    rua, numero = extrair_endereco(endereco)
    print(f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'")
