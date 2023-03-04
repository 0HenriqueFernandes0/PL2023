import re

def main():
    path="processos.txt"
    file = open(path,"r")
    lines = file.read().split('\n')
    reg_exp = r"(?P<pid>\d+)"
    for line in lines:
        coluna = re.split(r"::",line)
        if len(coluna) ==  6 or len(coluna) == 7:
            None

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
            print_tabelas(tabela.exc2())
        elif option == 2:
            print_tabelas(tabela.exc3())
        else:
            option = -1


if __name__ == '__main__':
    main()