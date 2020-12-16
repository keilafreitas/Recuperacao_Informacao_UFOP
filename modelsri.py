import math
import numpy as np


def ponderacaoTFIDF(docsp, f, k):
    "Retorna a ponderação TFIDF como w."
    print("===============================Ponderação TF-IDF================================")
    print("================================================================================")
    # Calculando frequencia de termo logarítimica (TF) (eq. 3.7)
    tf = [[0 for j in docsp] for i in k]
    N = len(docsp)
    for i in range(len(k)):
        for j in range(N):
            if f[i][j] != 0:
                tf[i][j] = 1 + math.log2(f[i][j])
            else:
                tf[i][j] = 0
    print("TF: {}".format(tf))

    # Calculando frequencia inversa de documentos (IDF) (eq. 3.8)
    n = [0 for i in k]
    for i in range(len(k)):
        for j in range(N):
            if f[i][j] > 0:
                n[i] += 1
    print(n)

    idf = [0 for i in k]
    for i in range(len(k)):
        idf[i] = math.log2(N / n[i])
    print("IDF: {}".format(idf))

    # Calculando a ponderação TF-IDF (eq. 3.9)
    tf_idf = [[0 for j in docsp] for i in k]
    for i in range(len(k)):
        for j in range(N):
            if f[i][j] > 0:
                tf_idf[i][j] = (1 + math.log2(f[i][j])) * math.log2(N / n[i])
            else:
                tf_idf[i][j] = 0
    w = tf_idf
    print("TF-IDF (w): {}".format(w))
    print("================================================================================")
    return w

def wconsulta(consultas, docsp, k, f):
    "Retorna o w referente a consulta."
    print("===================================w Consulta===================================")
    print("================================================================================")
    f_cons = [[0 for q in consultas] for i in k]
    w_cons = [[0 for q in consultas] for i in k]
    N = len(docsp)
    n = [0 for i in k]
    for i in range(len(k)):
        for j in range(N):
            if f[i][j] > 0:
                n[i] += 1

    print(consultas)
    for i in range(len(k)):
        for q in range(len(consultas)):
            f_cons[i][q] = consultas[q].count(k[i])
            if f_cons[i][q] > 0:
                w_cons[i][q] = (1 + math.log2(f_cons[i][q])) * math.log2(len(docsp) / n[i])
    print(w_cons)
    print("================================================================================")
    return w_cons


def modeloBM25(docsp, consultas, k, f):
    "Recuperação da informação pelo Modelo Probabilistivo BM25."
    print("==================================Modelo BM25===================================")
    print("================================================================================")
    # avg_doclen
    doclen = 0
    for j in range(len(docsp)):
        doclen += len(docsp[j])
    avg_doclen = doclen / len(docsp)
    #print(avg_doclen)

    # Modelo BM25 parcial
    b = 0.75
    k1 = 1
    N = len(docsp)
    Ba = [[0 for j in docsp] for i in k]

    n = [0 for i in k]
    for i in range(len(k)):
        for j in range(N):
            if f[i][j] > 0:
                n[i] += 1

    for i in range(len(k)):
        for j in range(len(docsp)):
            if f[i][j] == 0:
                Ba[i][j] = 0
            else:
                aux1 = (k1 + 1) * f[i][j]
                aux2 = b * (len(docsp[j]) / avg_doclen)
                Ba[i][j] = aux1 / (k1 * ((1 - b) + aux2) + f[i][j])
    print ('BAAAAAA')
    print (Ba)
    # Modelo BM25 Completo
    simBM25 = [[0 for q in consultas] for j in docsp]
    for i in range(len(k)):
        for q in range(len(consultas)):
            for j in range(len(docsp)):
                if k[i] in consultas[q] and k[i] in docsp[j]:
                    simBM25[j][q] += Ba[i][j] * (math.log2((N + 0.5) / (n[i] + 0.5)))
    print("\nSimilaridade no modelo BM25 (simBM):")
    print(np.array(simBM25))
    print("================================================================================")
    return simBM25
