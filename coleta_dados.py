import csv

def registrar_jogo():
    print("\n📋 Registro de Dados do Jogo")
    
    time1 = input("Nome do Time 1: ")
    time2 = input("Nome do Time 2: ")
    gols1 = int(input(f"Gols do {time1}: "))
    gols2 = int(input(f"Gols do {time2}: "))
    chutes1 = int(input(f"Chutes a gol do {time1}: "))
    chutes2 = int(input(f"Chutes a gol do {time2}: "))
    posse1 = float(input(f"Posse de bola do {time1} (%): "))
    posse2 = 100 - posse1  # O outro time recebe o restante da posse
    
    with open('dados.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([time1, gols1, chutes1, posse1, time2, gols2, chutes2, posse2])

    print("✅ Dados registrados com sucesso!")
