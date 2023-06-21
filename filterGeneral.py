import math
import pandas as pd
import matplotlib.pyplot as plt

print("Executing")

#dc = pd.read_excel("testeDP.xlsx")
#dc = pd.read_excel('notas_alunos_graduacao_ufjf_2019_2022.xlsx')
dc = pd.read_excel("result_filtrados_soExatas.xlsx")

dp_list = dc.DISCIPLINA.values.tolist()
#nm_list = dc.NOME.values.tolist()
yr_list = dc.ANO.values.tolist()
sm_list = dc.SEMESTRE.values.tolist()
nb_list = dc.NOTA.values.tolist()
st_list = dc.SITUACAO.values.tolist()

for y in range(len(dp_list)):
    dp_list[y] = dp_list[y][0:3]


listNod = list(dict.fromkeys(dp_list))
#listNod = list(dict.fromkeys(nm_list))

for y in range(len(nb_list)):
    if(nb_list[y] == 'APR'):
        nb_list[y] = 100
    elif(nb_list[y] == 'REP' or nb_list[y] == "TE"):
        nb_list[y] = 0
    else:
        nb_list[y] = int(nb_list[y])

def divide(n1, n2):
    if n2 == 0:
        return 0
    else:
        return n1/n2
    
def porcentagem(n1, n2):
    div = divide(n1,n2)
    return '{:.2f}'.format(div*100) + '%'

def media(n1,n2):
    div = divide(n1,n2)
    return '{:.2f}'.format(div)

def add_note(n):
    try:
        return int(n)
    except:
        return 0

def mediana(lista):
    if lista == []:
        return 0
    
    lista = sorted(lista)
    tamanho = len(lista)

    if tamanho % 2 == 0:
        mediana1 = lista[tamanho//2]
        mediana2 = lista[tamanho//2 - 1]
        mediana = ((int(mediana1) + int(mediana2)) / 2)
    else:
        mediana = lista[tamanho//2]   
    return mediana

def desvio_padrao(dados):
    n = len(dados)
    if n == 0:
        return 0
    media = sum(dados) / n
    somatorio = sum((x - media) ** 2 for x in dados)
    desvio_padrao = math.sqrt(somatorio / n)
    desvio_padrao_arredondado = math.ceil(desvio_padrao * 100) / 100
    return "{:.2f}".format(desvio_padrao_arredondado)

listDep = []
listMdPrePandemia = []
listMdnPrePandemia = []
listMdPandemia = []
listMdnPandemia = []
listQtPrePandemia = []
listQtPandemia = []
listApPrePandemia = []
listApPandemia = []
listaDif = []
listRepNotaPrePandemia = []
listRepFreqPrePandemia = []
listRepNotaPandemia = []
listRepFreqPandemia = []
listaDesvioPrePandemia = []
listaDesvioPandemia = []

for listActual in listNod:
    x = 0
    somPrePandemia = 0
    somPandemia = 0
    countPrePandemia = 0
    countPandemia = 0
    yesPrePandemia = 0
    yesPandemia = 0
    noPrePandemia = 0
    noPandemia = 0
    zeroPrePandemia = 0
    zeroPandemia = 0
    count = 0
    soma = 0
    notesPrePandemia = []
    notesPandemia = []

    #list = nm_list
    list = dp_list

    for x in range(len(list)):
        if list[x] == listActual:
            if yr_list[x] == 2019:
                countPrePandemia += 1
                if nb_list[x] != 0:
                        somPrePandemia += add_note(nb_list[x])
                        notesPrePandemia.append(nb_list[x])
                        if st_list[x] == "Aprovado":
                            yesPrePandemia += 1
                        else:
                            noPrePandemia += 1
                else:
                    zeroPrePandemia += 1
            else:
                countPandemia += 1
                if nb_list[x] != 0:
                    somPandemia += add_note(nb_list[x])
                    notesPandemia.append(nb_list[x])
                    if st_list[x] == "Aprovado":
                        yesPandemia += 1
                    else:
                        noPandemia += 1
                else:
                    zeroPandemia += 1

    mediaPrePandemia = media(somPrePandemia,countPrePandemia)
    mediaPandemia = media(somPandemia,countPandemia)
    medianaPrePandemia = mediana(notesPrePandemia)
    medianaPandemia = mediana(notesPandemia)
    desvioPadraoPrePandemia = desvio_padrao(notesPandemia)
    desvioPadraoPandemia = desvio_padrao(notesPandemia)
    aprovadosPrePandemia = porcentagem(yesPrePandemia,countPrePandemia)
    reprovadosNotaPrePandemia = porcentagem(noPrePandemia,countPrePandemia)
    reprovadosFreqPrePandemia = porcentagem(zeroPrePandemia,countPrePandemia)
    aprovadosPandemia = porcentagem(yesPandemia,countPandemia)
    reprovadosNotaPandemia = porcentagem(noPandemia,countPandemia)
    reprovadosFreqPandemia = porcentagem(zeroPandemia,countPandemia)

    listDep.append(list)

    listQtPrePandemia.append(countPrePandemia)
    listMdPrePandemia.append(mediaPrePandemia)
    listMdnPrePandemia.append(medianaPrePandemia)
    listaDesvioPrePandemia.append(desvioPadraoPrePandemia)
    listApPrePandemia.append(aprovadosPrePandemia)
    listRepNotaPrePandemia.append(reprovadosNotaPrePandemia)
    listRepFreqPrePandemia.append(reprovadosFreqPrePandemia)

    listQtPandemia.append(countPandemia)
    listMdPandemia.append(mediaPandemia)
    listMdnPandemia.append(medianaPandemia)
    listaDesvioPandemia.append(desvioPadraoPandemia)
    listApPandemia.append(aprovadosPandemia)
    listRepNotaPandemia.append(reprovadosNotaPandemia)
    listRepFreqPandemia.append(reprovadosFreqPandemia)


    plt.figure()
    plt.boxplot(notesPrePandemia) 
    nome_pasta = "boxplotsDep" 
    #nome_pasta = "boxplotsMaterias"
    nome_arquivo = nome_pasta + "/boxplot_{}.png".format(list + "_notesPrePandemia") 

    plt.savefig(nome_arquivo) 
    print("Gráfico salvo como: ", nome_arquivo) 

    plt.figure() 
    plt.boxplot(notesPandemia)
    nome_arquivo = nome_pasta + "/boxplot_{}.png".format(list + "_notesPandemia")
    plt.savefig(nome_arquivo)
    print("Gráfico salvo como: ", nome_arquivo)

tg = pd.DataFrame.from_dict({
    #'Disciplina': listDep,
    'Departamnto': listDep,
    'Pre Pandemia Quant': listQtPrePandemia, 
    'Pre Pandemia Media': listMdPrePandemia, 
    'Pre Pandemia Mediana': listMdnPrePandemia, 
    'Pre Pandemia Desvio Padrao': listaDesvioPrePandemia, 
    'Pre Pandemia Aprov': listApPrePandemia, 
    'Pre Pandemia Rep por Nota': listRepNotaPrePandemia,
    'Pre Pandemia Rep por Freq': listRepFreqPrePandemia,
    'Pandemia Quant': listQtPandemia, 
    'Pandemia Media': listMdPandemia, 
    'Pandemia Mediana': listMdnPandemia, 
    'Pandemia Desvio Padrao': listaDesvioPandemia, 
    'Pandemia Aprov': listApPandemia, 
    'Pandemia Rep por Nota': listRepNotaPandemia, 
    'Pandemia Rep por Infreq': listRepFreqPandemia
})

tg.to_excel('result_boxplot_departamentos2.xlsx', header=True, index=False)

print("Done!")