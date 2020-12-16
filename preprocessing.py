import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation

#nltk.download()


def preprocessamento(docs):
    "Preprocessa os documentos da lista docs para a lista docsp, eliminando stopwords, pontuação e 1 unico caracter."
    # Pre-processamento de uma lista de documentos
    # docs = []
    docsp = []
    print("=========================Preprocessamento de Documentos=========================")
    print("================================================================================")
    caracteres = ['!', '?', ',', '.', ':', ';', '-', '/', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '[', ']', '{', '}']

    for d in docs:
        # Remoção de pontuação
        for p in caracteres:
            d = d.replace(p, "")
        d = d.replace("\n", " ")
        d = d.replace("\r", "")
        d = d.strip()
        # Remoção de caixa alta
        d = d.lower()
        # Quebra por palavras
        d = d.split(" ")
        docsp.append(d)
        print("Doc:", d)

    stopwords = []
    stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))

    for d in docsp:
        for p in d:
            if p in stopwords:
                d.remove(p)
            elif len(p) <= 1:
                d.remove(p)
        # print("Doc:", d)
    print("================================================================================")

    return docsp