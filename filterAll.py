import math
import pandas as pd
import matplotlib.pyplot as plt
import re

print("Executing")

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
    elif(nb_list[y] == 'REP' or nb_list[y] == "TE" or nb_list[y] == "RE"):
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

somTotalPrePandemia = 0
somTotalPandemia = 0
countTotalPrePandemia = 0
countTotalPandemia = 0
yesTotalPrePandemia = 0
yesTotalPandemia = 0
noTotalPrePandemia = 0
noTotalPandemia = 0
zeroTotalPrePandemia = 0
zeroTotalPandemia = 0
countTotal = 0
somaTotal = 0
notesTotalPrePandemia = []
notesTotalPandemia = []

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
                countTotalPrePandemia += 1
                if nb_list[x] != 0:
                        somPrePandemia += add_note(nb_list[x])
                        somTotalPrePandemia += add_note(nb_list[x])
                        notesPrePandemia.append(nb_list[x])
                        notesTotalPrePandemia.append(nb_list[x])
                        if st_list[x] == "Aprovado":
                            yesPrePandemia += 1
                            yesTotalPrePandemia += 1
                        else:
                            noPrePandemia += 1
                            noTotalPrePandemia += 1
                else:
                    zeroPrePandemia += 1
                    zeroTotalPrePandemia += 1
            else:
                countPandemia += 1
                countTotalPandemia += 1
                if nb_list[x] != 0:
                    somPandemia += add_note(nb_list[x])
                    somTotalPandemia += add_note(nb_list[x])
                    notesPandemia.append(nb_list[x])
                    notesTotalPandemia.append(nb_list[x])
                    if st_list[x] == "Aprovado":
                        yesPandemia += 1
                        yesTotalPandemia += 1
                    else:
                        noPandemia += 1
                        noTotalPandemia += 1
                else:
                    zeroPandemia += 1
                    zeroTotalPandemia += 1

    countNotZeroPrePandemia = len(notesPrePandemia)
    countNotZeroPandemia = len(notesPandemia)

    mediaPrePandemia = media(somPrePandemia,countNotZeroPrePandemia)
    mediaPandemia = media(somPandemia,countNotZeroPandemia)
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

    listDep.append(listActual)
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
    nome_pasta = "boxplotsExatasDep" 
    #nome_pasta = "boxplotsExatasMaterias"
    nomeLista = re.sub(r'[\\/*?:"<>|]', '_', listActual)
    nomeLista = re.sub('\t', '_', nomeLista)
    nome_arquivo = nome_pasta + "/boxplot_{}.png".format(nomeLista + "_notesPrePandemia") 
    plt.savefig(nome_arquivo) 
    print("Gráfico salvo como: ", nome_arquivo)
    plt.close() 

    plt.figure() 
    plt.boxplot(notesPandemia)
    nomeLista = re.sub(r'[\\/*?:"<>|]', '_', listActual)
    nomeLista = re.sub('\t', '_', nomeLista)
    nome_arquivo = nome_pasta + "/boxplot_{}.png".format(nomeLista + "_notesPandemia")
    plt.savefig(nome_arquivo)
    print("Gráfico salvo como: ", nome_arquivo)
    plt.close()

countTotalNotZeroPrePandemia = len(notesTotalPrePandemia)
countTotalNotZeroPandemia = len(notesTotalPandemia)

mediaTotalPrePandemia = media(somTotalPrePandemia,countTotalNotZeroPrePandemia)
mediaTotalPandemia = media(somTotalPandemia,countTotalNotZeroPandemia)
medianaTotalPrePandemia = mediana(notesTotalPrePandemia)
medianaTotalPandemia = mediana(notesTotalPandemia)
desvioPadraoTotalPrePandemia = desvio_padrao(notesTotalPandemia)
desvioPadraoTotalPandemia = desvio_padrao(notesTotalPandemia)
aprovadosTotalPrePandemia = porcentagem(yesTotalPrePandemia,countTotalPrePandemia)
reprovadosTotalNotaPrePandemia = porcentagem(noTotalPrePandemia,countTotalPrePandemia)
reprovadosTotalFreqPrePandemia = porcentagem(zeroTotalPrePandemia,countTotalPrePandemia)
aprovadosTotalPandemia = porcentagem(yesTotalPandemia,countTotalPandemia)
reprovadosTotalNotaPandemia = porcentagem(noTotalPandemia,countTotalPandemia)
reprovadosTotalFreqPandemia = porcentagem(zeroTotalPandemia,countTotalPandemia)

listDep.append("Total")
listQtPrePandemia.append(countTotalPrePandemia)
listMdPrePandemia.append(mediaTotalPrePandemia)
listMdnPrePandemia.append(medianaTotalPrePandemia)
listaDesvioPrePandemia.append(desvioPadraoTotalPrePandemia)
listApPrePandemia.append(aprovadosTotalPrePandemia)
listRepNotaPrePandemia.append(reprovadosTotalNotaPrePandemia)
listRepFreqPrePandemia.append(reprovadosTotalFreqPrePandemia)

listQtPandemia.append(countTotalPandemia)
listMdPandemia.append(mediaTotalPandemia)
listMdnPandemia.append(medianaTotalPandemia)
listaDesvioPandemia.append(desvioPadraoTotalPandemia)
listApPandemia.append(aprovadosTotalPandemia)
listRepNotaPandemia.append(reprovadosTotalNotaPandemia)
listRepFreqPandemia.append(reprovadosTotalFreqPandemia)

plt.figure()
plt.boxplot(notesTotalPrePandemia) 
nome_pasta = "boxplotTudoDep" 
#nome_pasta = "boxplotsExatasMaterias"
nome_arquivo = nome_pasta + "/boxplot_{}.png".format("Exatas_notesPrePandemia") 

plt.savefig(nome_arquivo) 
print("Gráfico salvo como: ", nome_arquivo)
plt.close() 

plt.figure() 
plt.boxplot(notesTotalPandemia)
nome_arquivo = nome_pasta + "/boxplot_{}.png".format("Exatas_notesPandemia")
plt.savefig(nome_arquivo)
print("Gráfico salvo como: ", nome_arquivo)
plt.close()

tg = pd.DataFrame.from_dict({
    #'Disciplina': listDep,
    'Departamento': listDep,
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

tg.to_excel('result_exatas_boxplot_departamentos.xlsx', header=True, index=False)
#tg.to_excel('result_exatas_boxplot_disciplinas.xlsx', header=True, index=False)

print("Done!")