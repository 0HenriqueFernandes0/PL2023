import re
def value(pessoa,key_word):
    if key_word == "Processo":
        return pessoa[0]
    elif key_word == "Ano":
        return pessoa[1][0]
    elif key_word == "Mes":
        return pessoa[1][1]
    elif key_word == "Dia":
        return pessoa[1][2]
    elif key_word == "Nome":
        return pessoa[2]
    elif key_word == "Pai":
        return pessoa[3]
    elif key_word == "Mae":
        return pessoa[4]
    elif key_word == "Observações":
        return pessoa[5]
    elif key_word == "nome propio":
        return re.match(r"\w+",pessoa[2])
    elif key_word == "apelido":
        return pessoa[5]
    
def frequencia(pessoas,key_word,tempo):
    frequencias = {}
    for pessoa in pessoas:
        valor = value(pessoa,key_word)
        if (tempo!=0):
            ano_index = value(pessoa,"Ano")//tempo
            if (ano_index in frequencias):
                if( valor in frequencias[ano_index]):
                    frequencias[ano_index][valor]+=1
                else :
                    frequencias[ano_index][valor]=1
            else :
                frequencias[ano_index]={}
                frequencias[ano_index][valor]=1
        else:
            if( valor in frequencias):
                frequencias[valor]+=1
            else :
                frequencias[valor]=1
    return frequencias

def TOP(dict,n):
    for key in list(dict.keys()):
        maiores = []
        for value in dict[key].keys():
            maiores.append(value)

        dict[key]=sorted(maiores,key=lambda x: dict[key][x],reverse=True)[:n]
    print(dict)
    return(dict)


def print_tabelas(dict1,dim):

    if dim == 1:
        if type(list(dict1.values())[0]) is dict :
            for key in list(dict1):
                dict1[key]=len(dict1[key])
    
    matrix = []
    tam = [0]
    if (len(dict1) < len(str(list(dict1.values())[0]))):
        for value in sorted(list(dict1.keys())):
            tam.append(len(str(value)))
        matrix.append(sorted(list(dict1.keys())))
        for key in sorted(list(dict1.keys())):
            i=0
            for value in dict[key]:
                if(len(matrix)<i+1):
                    matrix.append=[]
                matrix[i].append(value)
                if(len(str(value))>tam[i]):
                    tam[i]=len(str(value))
                i+=1
    else : 
        for key in sorted(list(dict1.keys())):
            line = [key]
            if tam[0]<len(str(key)):
                tam[0]=len(str(key))

            line.append(str(dict1[key]))
            i=1
            for valor in dict[key]:
                if(len(tam)<i+1): 
                    tam.append(len(str(valor)))
                elif (tam[i]<len(str(valor))):
                    tam[i]=len(str(valor))
                i+=1
            matrix.append(line)

    tam_sep = 0
    separador=""
    for i in tam:
        tam_sep+=i+1
    for i in range(tam_sep):
        separador+="-"
    separador+="\n"

    print(len(tam))
    print(len(matrix[0]))
    tabela = ""
    for line in matrix:
        colum=0
        new_line=""
        for valor in line:
            valor="|"+str(valor)
            for i in range(len(valor),tam[colum]):
                valor+=" "
            colum+=1
            new_line += valor +"|"
        tabela+=new_line +"\n"
        tabela+=separador
    print(tabela)