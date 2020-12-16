import copy

def exiberesultados(simR, descr, docs_dic, max_rec, docs_rel):
    "Apresenta os resultados da recuperacao pelo modelo SimP."

    sim = copy.deepcopy(simR)  # Copia do vetor de similaridades (simV)
    ndr = 0  # Numero de documentos recuperados
    docs_rec = {}  # Documentos recuperados
    #max_rec = 5  # Maximo de documentos recuperados exibidos
    print("Apresentação de ate {} dos melhores resultados (modelo {})".format(max_rec, descr))
    print("================================================================================")
    print(descr)
    print("| Pos  |                                              Documento | Similaridade |")
    for i in range(0, max_rec):
        if max(sim) == [0]:
            print("|                   Nao foram recuperados mais documentos.                     |")
            break
        idx = sim.index(max(sim))
        doc = docs_dic[sim.index(max(sim))]
        print("|%4d. |%55s |%13.3f |" % (i + 1, docs_dic[idx], sim[idx][0]))
        docs_rec[idx] = doc
        sim[idx][0] = 0
        ndr += 1
    print("================================================================================")

    # Avaliando a recuperacao (modelo Vetorial)
    # Documentos avaliados (por um humano) como relevantes: 0, 9, 8, 1, 3, 2

    #docs_rel = {}

    #docs_rel[5] = docs_dic[5]
    #docs_rel[6] = docs_dic[6]
    #docs_rel[7] = docs_dic[7]
    #docs_rel[8] = docs_dic[8]
    #docs_rel[13] = docs_dic[13]
    #docs_rel[17] = docs_dic[17]
    #docs_rel[18] = docs_dic[18]

    pre_num = 0
    rev_num = 0
    pre_den = 0
    rev_den = len(docs_rel)
    prec = []  # Lista de Precisão
    rev = []  # Lista de revocação

    docs_rel_pre = {}
    rec_keys = list(docs_rec.keys())
    rel_keys = list(docs_rel.keys())
    print("Avaliacao da recuperacao (modelo {}])".format(descr))
    print("Documentos recuperados (indices): ", rec_keys)
    print("Documentos relevantes (indices):  ", rel_keys)
    print("================================================================================")
    print("| Pos | Precisao | Revocacao |")
    for i in range(0, ndr):
        if i < len(rec_keys):
            pre_den += 1
            if rec_keys[i] in rel_keys:  # Documento recuperado e relevante
                pre_num += 1
                rev_num += 1
                docs_rel_pre[rel_keys[i]] = pre_num / pre_den
        prec.append(pre_num / pre_den)
        rev.append(rev_num / rev_den)
        print("| %3d |  %2d / %2d |  %2d / %2d  |" % (i + 1, pre_num, pre_den, rev_num, rev_den))
    print("================================================================================")
    print(docs_rel_pre)

    print("==============================Média das Precisões===============================")
    print("================================================================================")

    soma = 0
    for i in docs_rel:
        if i in docs_rel_pre:
            soma += docs_rel_pre[i]

    map = soma / len(docs_rel)
    print("\nMedia das precisoes medias:")
    print(map)
    print("================================================================================")


    rj = 5  # Padrao de revocacao 5 (recupera pelo menos 50% dos documentos relevantes)
    prec_max_rj = -float("inf")
    for i in range(len(prec)):
        if prec[i] > prec_max_rj and rev[i] >= rj / 10:
            prec_max_rj = prec[i]
    print("\nPrecisao interpolada no %d%%-esimo nivel padrao de revocacao:" % (rj * 10))
    print("================================================================================")
    print(prec_max_rj)
    print("================================================================================")


