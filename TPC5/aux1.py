import re

def ligar(numero,saldo):
    sucesso=1
    m = re.match("^00",numero)
    if m:
        saldo_t = saldo[1]*100+saldo[0]
        if saldo_t>150:
            saldo_t-=150
            saldo[0]=saldo_t % 100
            saldo[1]=saldo_t//100
            print(f"""saldo = {saldo[1]}e{saldo[0]}c" """)
        else:
            print(f"saldo insuficiente")
            sucesso=0
    else:
        len(numero)
        m = re.match("^601",numero)
        n = re.match("^641",numero)
        if m or n or len(numero)!= 9:
            print("""maq: "Esse número não é permitido neste telefone. Queira discar novo número!" """)
        else:
            m = re.match("^2",numero)
            if m:
                saldo_t = saldo[1]*100+saldo[0]
                if saldo_t>25:
                    saldo_t-=25
                    saldo[0]=saldo_t % 100
                    saldo[1]=saldo_t//100
                    print(f"""saldo = {saldo[1]}e{saldo[0]}c" """)
                else:
                    print(f"saldo insuficiente")
                    sucesso=0
            else:
                m = re.match("^808",numero)
                if m:
                    saldo_t = saldo[1]*100+saldo[0]
                    if saldo_t>10:
                        saldo_t-=10
                        saldo[0]=saldo_t % 100
                        saldo[1]=saldo_t//100
                        print(f"""saldo = {saldo[1]}e{saldo[0]}c" """)
                    else:
                        print(f"saldo insuficiente")
                        sucesso=0
                else:
                    m = re.match("^800",numero)
                    if m:
                        print(f"""saldo = {saldo[1]}e{saldo[0]}c" """)

    return sucesso



def inserir(groups,saldo):
    texto = """maq: " """
    for moeda in groups:
        if moeda:
            m =re.split("c",moeda)
            if len(m)>1:
                m=int(m[0])
                if m == 1 or m == 5 or m == 10 or m == 20 or m == 50:
                    saldo[0]+=m
                else:
                    texto+=f"{m}c - moeda inválida; "
            else:
                m =re.split("e",moeda)
                if len(m)>1:
                    m=int(m[0])
                    if m == 1 or m == 2:  
                        saldo[1]+=m
                    else:
                        texto+=f"{m}c - moeda inválida; "
    texto+=f"""saldo = {saldo[1]}e{saldo[0]}c" """
    print(texto)

