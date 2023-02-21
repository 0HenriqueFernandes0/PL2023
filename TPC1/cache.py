class Cache:
    tabela = []

    def add(self, str):
        lines = str.split(",")
        if len(lines) > 5:
            if lines[0].isdigit():
                if lines[2].isdigit() and int(lines[2]) > 0:
                    if lines[3].isdigit() and int(lines[3]) > 0:
                        if lines[4].isdigit() and int(lines[4]) > 0:
                            if lines[5].isdigit() and (int(lines[5]) == 0 or int(lines[5]) == 1):
                                if lines[1] == "F" or lines[1] == "M":
                                    lines[1] = lines[1] == "M"
                                    lines[0] = int(lines[0])
                                    lines[2] = int(lines[2])
                                    lines[3] = int(lines[3])
                                    lines[4] = int(lines[4])
                                    lines[5] = int(lines[5])
                                    self.tabela.append(lines)

    def print(self):
        for line in self.tabela:
            print(";".join(line))

    def exc1(self):
        homens = 0
        muheres = 0
        for pessoa in self.tabela:
            if pessoa[1] == 1 and pessoa[5] == 1:
                homens += 1
            elif pessoa[1] == 0 and pessoa[5] == 1:
                muheres += 1
        dict = {}
        dict['Muheres'] = muheres / (homens + muheres)
        dict['Homens'] = homens / (homens + muheres)
        return dict

    def exc2(self):
        escaloes = []
        total = 0
        for pessoa in self.tabela:
            if pessoa[5] == 1:
                for i in range(pessoa[0] // 5 - len(escaloes)-5):
                    escaloes.append(0)
                total += 1
                escaloes[pessoa[0] // 5 - 6] += 1
        print("Distribuição da doença por escalões etários:")
        i = 0
        dict = {}
        for escalao in escaloes:
            dict [f"[{i*5+30}-{i*5+34}]"] = escalao/total*100
            i += 1
        return dict

    def exc3(self):
        escaloes = []
        total = 0
        for pessoa in self.tabela:
            if pessoa[5] == 1:
                for i in range(pessoa[3] // 10 - len(escaloes)+1):
                    escaloes.append(0)
                total += 1
                escaloes[pessoa[3] // 10] += 1
        print("Distribuição da doença por escalões etários:")
        i=0
        dict ={}
        for escalao in escaloes:
            dict[f"[{i*10}-{i*10+9}]"]=escalao/total*100
            i += 1
        return dict


