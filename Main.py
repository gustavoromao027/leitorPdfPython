import pdfplumber
import collections
#PDFPLUMBER É UMA BIBLIOTECA DO PYTHON PARA EXTRAIR INFORMAÇÕES DE PDF
#UTILIZADO NO SISTEMA PARA BASICAMENTE CONTAR OCORRENCIAS DE PALAVRAS

#FUNÇÃO PARA CONTAR PALAVRAS NO TEXTO
def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)
#FUNÇÃO PARA LISTAR AS 20 PALAVRAS QUE MAIS APARECEM NO TEXTO
#UTILIZANDO DA BIBLIOTECA "COLLECTIONS" PARA REALIZAR A CONTAGEM DE CADA PALAVRA E EM UM TOTAL DE 20 AS QUE MAIS APARECEM E DPS RETORNAR ISSO.
def listar_palavras_mais_frequentes(texto):
    palavras = texto.split()
    contagem = collections.Counter(palavras)
    palavras_mais_frequentes = contagem.most_common(20)
    return palavras_mais_frequentes
#FUNÇÃO PARA EXIBIR A QUANTIDADE TOTAL DE PALAVRAS NO PDF
#SIMPLESMENTE PERCORRE TODO O DOCUMENTO E ARMAZENA O TOTAL DE PALAVRAS ENCONTRADAS E RETORNA O VALOR
def quantidade_total_de_palavras(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        total_palavras = 0
        for page in pdf.pages:
            total_palavras += contar_palavras(page.extract_text())
        return total_palavras
#FUNÇÃO PARA CONTAR PALAVRAS EM UMA SEÇÃO DO SUMARIO
#ARMAZENANDO EM UMA VARIAVEL LOCAL O VALOR INICIAL, E PERCORRENDO E ITERANDO ATRAVES DE CADA PAGINADO DOCUMENTO
#EXTRAINDO O TEXTO DA PAGINA ATUAL, ALEM DE VERIFICAR SE A SEÇÃO ESPECIFICADA ESTÁ NA PAGINA, CASO ESTEJA, RETORNAR O VALOR.
def contar_palavras_em_secao(pdf_path, secao):
    with pdfplumber.open(pdf_path) as pdf:
        total_palavras_secao = 0
        for page in pdf.pages:
            text = page.extract_text()
            if secao in text:
                total_palavras_secao += contar_palavras(text)
        return total_palavras_secao
#FUNÇÃO DE MENSAGEM DE AJUDA PRO USUARIO
def exibir_mensagem_de_ajuda():
    print("Este programa permite acessar a meta informação do arquivo PDF:")
    print("1. Quantidade total de palavras no documento.")
    print("2. Quantidade de palavras na seção do sumário.")
    print("3. As 20 palavras de maior ocorrência no documento.")
#FUNÇÃO PRINCIPAL DO SISTEMA
def menu(pdf_path):
    while True:
        exibir_mensagem_de_ajuda()
        opcao = input("Digite o número da opção (ou 's' para sair): ")
        if opcao == 's':
            break
        elif opcao == '1':
            print(f"Quantidade total de palavras: {quantidade_total_de_palavras(pdf_path)}")
        elif opcao == '2':
            secao = input("Digite a seção do sumário: ")
            print(f"Quantidade de palavras na seção: {contar_palavras_em_secao(pdf_path, secao)}")
        elif opcao == '3':
            with pdfplumber.open(pdf_path) as pdf:
                texto_completo = ""
                for page in pdf.pages:
                    texto_completo += page.extract_text()
                palavras_mais_frequentes = listar_palavras_mais_frequentes(texto_completo)
                print("As 20 palavras de maior ocorrência no documento:")
                for palavra, frequencia in palavras_mais_frequentes:
                    print(f"{palavra}: {frequencia}")
#CAMINHO DO PDF DO SISTEMA
pdf_path = "manualaluno-157.pdf"
#INICIANDO O PATH
menu(pdf_path)