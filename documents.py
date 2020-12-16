import os
import textract

def buscadocumentos(endereco_docs, docs_dic):
    "Busca os documentos do caminho endereco_docs e armazena em uma lista chamada docs"
    # Coleta dos documentos e armazenamento em uma lsita
    docs = []

    source_directory = os.path.join(os.getcwd(), endereco_docs)
    i = 0
    dir_files = sorted(os.listdir(source_directory))

    print("==============================Coleta de Documentos==============================")
    print("================================================================================")

    for process_file in dir_files:
        print(process_file)
        file, extension = os.path.splitext(process_file)
        text = textract.process(os.path.join(source_directory, process_file)).decode('utf-8', 'ignore')
        text = file + "\n" + text
        docs.append(text)
        docs_dic[i] = process_file
        i += 1
    return docs
    print("================================================================================")