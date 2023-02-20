from cache import Cache

def print_tabelas(dict):
    string = ""
    tam_1=0
    for nome in dict.keys():
        if (len(nome)>tam_1):
            tam_1 = len(nome)
    tam_1+=2

    for i in range(tam_1*2):
        string+= '-'
    keys = dict.keys()
    for i in range(len(keys)):
        string += "\n|" + keys[i]
        for n in range(len(keys[i]),tam_1):
            string+= ' '
        string += '|' + dict[keys[i]] + "|\n"
        for i in range(tam_1 * 2):
            string += '-'
def main():
    tabela = Cache()
    path="myheart.csv"
    file = open(path,"r")
    lines = file.read().split('\n')
    for line in lines:
        tabela.add(line)

    option =0
    while option!= -1:
        option=int(input("""
0 - distribuição da doença por sexo
1 - distribuição da doença por escalões etários
2 - distribuição da doença por níveis de colesterol
3 - exit
        """))
        if option == 0:
            print_tabelas(tabela.exc1())
        elif option == 1:
            tabela.exc2()
        elif option == 2:
            tabela.exc3()
        else:
            option = -1


if __name__ == '__main__':
    main()