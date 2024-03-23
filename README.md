# Desafio_teia

# API de Análise de Strings

Este repositório contém uma API Flask projetada para analisar strings enviadas através de requisições POST. A API oferece duas funcionalidades principais:

Verificação de Palíndromo: Determina se a string de entrada é um palíndromo, ou seja, se é lida da mesma forma de trás para frente.
Histograma de Caracteres: Cria um histograma que conta a ocorrência de cada caractere na string de entrada.


# Endpoint da API

A API possui um único endpoint:


POST /analyze_string: Analisa a string de entrada e retorna informações sobre se ela é um palíndromo e seu histograma de caracteres.

# Uso


Envie uma requisição POST para https://victor-bruno85.github.io/Desafio_teia/analyze_string com o seguinte payload JSON:


# JSON

{
    "texto": "sua_string_de_entrada_aqui"
}


A API responderá com um objeto JSON contendo as seguintes informações:

JSON

{
    "is_palindrome": true,
    "histogram": {
        "a": 2,
        "b": 1,
        ...
    }
}



# Adaptação para Java

Neste repositório, você encontrará um arquivo adicional chamado teia.txt. Esse arquivo contém uma adaptação do código original em Python para a linguagem de programação Java. A adaptação foi realizada por uma IA
