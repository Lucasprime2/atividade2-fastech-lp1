r= []  

while True:
    nome = input("Nome (enter para sair): ").strip()
    if nome == "":
        break

    while True:
        s = input("Peso (kg): ").strip().replace(",", ".")
        try:
            peso = float(s)
            if peso <= 0:
                print("Peso deve ser > 0.")
                continue
            break
        except:
            print("Valor inválido.")

    while True:
        s = input("Altura (m): ").strip().replace(",", ".")
        try:
            altura = float(s)
            if altura <= 0:
                print("Altura deve ser > 0.")
                continue
            break
        except:
            print("Valor inválido.")

    idade_txt = input("Idade: ").strip()
    idade = int(idade_txt) if idade_txt != "" else None

    imc = peso / (altura ** 2)

    if imc < 16:
        categoria = "Baixo peso (grau I)"
    elif imc < 17:
        categoria = "Baixo peso (grau II)"
    elif imc < 18.5:
        categoria = "Baixo peso (grau III)"
    elif imc < 25:
        categoria = "Peso adequado"
    elif imc < 30:
        categoria = "Sobrepeso"
    elif imc < 35:
        categoria = "Obesidade (grau I)"
    elif imc < 40:
        categoria = "Obesidade (grau II)"
    else:
        categoria = "Obesidade (grau III)"

    r.append([nome, idade, peso, altura, round(imc, 2), categoria])
    print(f"{nome} registrado: IMC {imc:.2f} - {categoria}\n")

print("\nRelatório final:")
for item in r:
    nome, idade, peso, altura, imc, categoria = item
    idade_text = f"{idade} anos" if idade is not None else "idade n/d"
    print(f"{nome} - {idade_text} - IMC: {imc:.2f} - {categoria}")