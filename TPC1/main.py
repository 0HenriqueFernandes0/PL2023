from cache import Cache

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
            tabela.exc1()
        elif option == 1:
            tabela.exc2()
        elif option == 2:
            tabela.exc3()
        else:
            option = -1


if __name__ == '__main__':
    main()