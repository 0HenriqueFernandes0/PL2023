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
        return re.match(r"\w+",pessoa[2]).group(0)
    elif key_word == "apelido":
        lista = re.findall(r"\w+$",pessoa[2])
        return lista[len(lista)-1]
    
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

def frequencia_familiares(pessoas):
    dict1 = {}
    for pessoa in pessoas:
        type = re.findall(r"(?:,(([A-Z][a-z]+ )*([A-Z][a-z]+))\. Proc.\d+)",pessoa[5])
        for t in type:
            if(t[0] in dict1):
                dict1[t[0]]+=1
            else :
                dict1[t[0]]=1
    return dict1

def TOP(dict,n):
    for key in list(dict.keys()):
        maiores = []
        for value in dict[key].keys():
            maiores.append(value)

        dict[key]=sorted(maiores,key=lambda x: dict[key][x],reverse=True)[:n]
    return(dict)

def json(pessoas):
    pagjson="""{
                    "pessoas":[
            """
    for i in range(20):
        if(len(pessoas)>i+1):
            pagjson+="{"+f"""       "Processo":{value(pessoas[i],'Processo')},
                                    "Ano":{value(pessoas[i],'Ano')},
                                    "Mes":{value(pessoas[i],'Mes')},
                                    "Dia":{value(pessoas[i],'Dia')},
                                    "Nome":"{value(pessoas[i],'Nome')}",
                                    "Pai":"{value(pessoas[i],'Pai')}",
                                    "Mae":"{value(pessoas[i],'Mae')}",
                                    "Observações":"{value(pessoas[i],'Observações')}"
            """
            if (i==19):
                pagjson+="}"
            else :pagjson+="},"
    pagjson+="""            ]
                }"""
    file = open("output.json", "w")
    file.write(pagjson)
    file.close
        
def print_tabelas(dict1,dim):

    if dim == 1:
        if type(list(dict1.values())[0]) is dict :
            for key in list(dict1):
                dict1[key]=len(dict1[key])
    
    matrix,tam=dict_to_matriz(dict1)

    tam_sep = 0
    separador="-"
    for i in tam:
        tam_sep+=i+1
    for i in range(tam_sep):
        separador+="-"
    separador+="\n"

    tabela = separador
    for line in matrix:
        colum=0
        new_line="|"
        for valor in line:
            valor=str(valor)
            for i in range(len(valor),tam[colum]):
                valor+=" "
            colum+=1
            new_line += valor +"|"
        tabela+=new_line +"\n"
        tabela+=separador
    print(tabela)

def dict_to_matriz(dict1):
    matrix = []
    tam = []
     
    if (len(dict1) < len(str(list(dict1.values())[0]))):
        matrix.append([])
        for value in sorted(list(dict1.keys())):
            tam.append(len(str(value)))
            matrix[0].append(str(value))
        t=0
        for key in sorted(list(dict1.keys())):
            i=1
            listvalues = dict1[key]
            if(len(listvalues)>0 and type(listvalues[0])==dict):
                sorted(listvalues,key=lambda x:dict1[key][x],reverse=True)
            for value in listvalues:
                if(len(matrix)<i+1):
                    matrix.append([])
                matrix[i].append(value)
                if(len(tam)<t+1):
                    tam.append(len(str(value)))
                elif(len(str(value))>tam[t]):
                    tam[t]=len(str(value))
                i+=1
            t+=1
    else : 
        for key in sorted(list(dict1.keys())):
            line = [key]
            if(len(tam)<1):
                tam.append(len(str(key)))
            elif tam[0]<len(str(key)):
                tam[0]=len(str(key))

            line.append(str(dict1[key]))
            i=1

            listvalues = [dict1[key]]
            for valor in listvalues:
                if(len(tam)<i+1): 
                    tam.append(len(str(valor)))
                elif (tam[i]<len(str(valor))):
                    tam[i]=len(str(valor))
                i+=1
            matrix.append(line)
    return(matrix,tam)