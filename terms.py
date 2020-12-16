def obtencaotermos(docsp):
    "Organiza todos os termos possíveis da lista de documentos."
    print("===============================Obtenção de Termos===============================")
    print("================================================================================")
    k = []
    for d in docsp:
        for palavra in d:
            if palavra not in k:
                k.append(palavra)

    print(k)
    print("================================================================================")
    return k

def matriztermos(docsp, k):
    "Organiza e obtem a matriz de termos (fij) de uma lista docsp e uma lista de termos k."
    print("================================Matriz de Termos================================")
    print("================================================================================")

    f = [[0 for j in docsp] for i in k]
    N = len(docsp)
    for i in range(len(k)):
        for j in range(N):
            f[i][j] = docsp[j].count(k[i])
    print(f)
    print("================================================================================")

    return f

def frequenciatermos(docsp, k):
    "Organiza e obtem a matriz de termos (Fi) de uma lista k."

    print("==============================Frequência de Termos==============================")
    print("================================================================================")
    f = [[0 for j in docsp] for i in k]
    N = len(docsp)
    F = [0 for i in k]
    for i in range(len(k)):
        aux = 0
        for j in range(N):
          f[i][j] = docsp[j].count(k[i])
          aux += f[i][j]
        F[i] = aux

    print(F)
    print("================================================================================")
    return F