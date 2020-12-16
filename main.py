# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import documents
from documents import buscadocumentos
from modelsri import ponderacaoTFIDF, modeloBM25, wconsulta
from preprocessing import preprocessamento
from resultsri import exiberesultados
from terms import obtencaotermos, matriztermos, frequenciatermos


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Inicio do aplicativo')
    # docs = []         # Receberá todos os documentos da base da pesquisa
    # docsp = []        # Receberá todos os documentos preprocessados
    # k = []            # Receberá todos os termos dos documentos
    # f[i][j]           # Receberá a matriz de termos
    # F[i]              # Receberá uma lista com a freqeuncia dos termos K nos documentos

    docs_dic = {} # Dicionario de documentos, usado na avaliação dos resultados.

    max_rec = 7  # Maximo de documentos recuperados exibidos

    endereco_docs = "collection" #efinição dos documentos a serem usados na pesquisa

    docs = buscadocumentos(endereco_docs, docs_dic)   # Busca os documentos definidos acima

    docsp = preprocessamento(docs)          # Preprocessa todos os documentos da lista docs[]

    k = obtencaotermos(docsp)               # Termos
    f = matriztermos(docsp, k)              # fij
    F = frequenciatermos(docsp, k)          # Fi

    # Solicitação para o usuário digitar os termos da consulta
    # Termo utilizado windows xp
    c = input("\nDigite os termos que deseja consultar nos documentos: ")
    consultas = preprocessamento([c])  # Preprocessa a consulta
    print(consultas)

    w = ponderacaoTFIDF(docsp, f, k)        # TF-IDF
    w_cons = wconsulta(consultas, docsp, k, f)

    simBM25 = modeloBM25(docsp, consultas, k, f)

    # Avaliação do especialista para consulta XPTO
    docs_rel = {}

    docs_rel[5] = docs_dic[5]
    docs_rel[6] = docs_dic[6]
    docs_rel[7] = docs_dic[7]
    docs_rel[8] = docs_dic[8]
    docs_rel[13] = docs_dic[13]
    docs_rel[17] = docs_dic[17]
    docs_rel[18] = docs_dic[18]

    docs_rec = exiberesultados(simBM25, 'BM25', docs_dic, max_rec, docs_rel)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
