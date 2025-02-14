menu = """
[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair
==>
"""

saldo = 0
limite = 500
extraro = ""
numero_de_saque = 0
LIMITE_DE_SAQUE = 3


while True:
    print(menu)
    numero = input()

    if numero == "s":
       
        if numero_de_saque >=  LIMITE_DE_SAQUE:
            numero_de_saque += 1
            if saldo >= valorSaque:
                valorSaque = float(input("Quanto você deseja sacar: "))
                saqueDinheiro = saldo - valorSaque
                saldo = saqueDinheiro
                print(f"Você sacou: R$ {valorSaque}Reais")
            else:
                print("Saldo insuficiente")
        else:
            print("Seu limite de saque já acabou!")
    
    elif numero == "d":
        valorDepositor = float(input("Quanto você deseja depositar: "))
        totalValor = saldo + valorDepositor
        saldo += totalValor
        print(f"Seu saldo agora é: R${saldo} Reais")
    
    elif numero  == "e":
        print(f"""
        <================= extrato =============>
        O seu saldo é: R${saldo} Reais
        <=======================================>
        """)

    elif numero == "q":
        break
    


