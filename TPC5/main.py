import re
from aux1 import*
def main():
    #0-LEVANTAR -> 1,3
    #1-MOEDA -> 2,3
    #2-T= -> 1,2,3,4
    #3-ABORTAR -> 0
    #4-POUSAR -> 0
    #5- fechar pograma(nao é um estado como os outros)
    Estado = 4
    saldo = [0,0]
    while Estado < 5 :
        text = input()
        if Estado == 0:
            m = re.match("^MOEDA( \d+c,| \d+e,)*( \d+c| \d+e)\.?$",text)
            if m:
                m=re.split(",",re.split("A",text)[1])
                inserir(m,saldo)
                Estado = 1
            elif re.match("ABORTAR",text):
                Estado = 3
                print(f"""maq: "troco={saldo}; Volte sempre!" """)
                saldo=0
            else:
                print("Só pode inserir moedas ou entao abortar.")
        elif Estado == 1:
            m = re.match("^T=(\d+)$",text)
            if m:
                sucesso = ligar(m.group(1),saldo)
                Estado = 2
                if not sucesso:
                    print("""maq: "Introduza moedas." """)
                    
            elif re.match("ABORTAR",text):
                Estado = 3
                print(f"""maq: "troco={saldo}; Volte sempre!" """)
                saldo=0
            else:
                print("Só pode ligar ou entao abortar.")
        elif Estado == 2:
            m = re.match("T=(\d+)",text)
            if m:
                sucesso = ligar(m.group(1),saldo)
                if not sucesso:
                    print("""maq: "Introduza moedas." """)
            else:
                m = re.match("^MOEDA( \d+c,| \d+e,)*( \d+c| \d+e)$",text)
                if m:
                    m=re.split(",",re.split("A",text)[1])
                    inserir(m,saldo)
                elif re.match("ABORTAR",text):
                    Estado = 3
                    print(f"""maq: "troco={saldo[1]}e{saldo[0]}c; Volte sempre!" """)
                    saldo=0
                elif re.match("POUSAR",text):
                    Estado = 4
                    print(f"""maq: "troco={saldo[1]}e{saldo[0]}c; Volte sempre!" """)
                    saldo=0
                else:
                    print("Só pode ligar ou entao pousar/abortar.")
        elif Estado == 3 or Estado == 4:
            if re.match("LEVANTAR",text):
                Estado = 0
                print("""maq: "Introduza moedas." """)
            else:
                print("Telefone ainda nao foi levantado.")
        else:
            Estado=5



if __name__ == '__main__':
    main()