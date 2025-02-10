import pandas as pd
import matplotlib.pyplot as plt

def gerar_estatisticas():
    try:
        df = pd.read_csv('dados.csv', names=["Time1", "Gols1", "Chutes1", "Posse1", "Time2", "Gols2", "Chutes2", "Posse2"])
        
        print("\n📈 Estatísticas Gerais:")
        print(df.describe())

        # Gráfico de Gols
        df[['Time1', 'Gols1']].set_index('Time1').plot(kind='bar', color='blue', legend=False)
        df[['Time2', 'Gols2']].set_index('Time2').plot(kind='bar', color='red', legend=False)
        plt.title("Gols por Time")
        plt.xlabel("Time")
        plt.ylabel("Gols")
        plt.show()

        # Gráfico de Posse de Bola
        plt.figure(figsize=(8, 5))
        plt.bar(df['Time1'], df['Posse1'], color='blue', alpha=0.6, label='Posse do Time 1')
        plt.bar(df['Time2'], df['Posse2'], color='red', alpha=0.6, label='Posse do Time 2')
        plt.title("Posse de Bola")
        plt.xlabel("Times")
        plt.ylabel("Posse (%)")
        plt.legend()
        plt.show()

    except FileNotFoundError:
        print("⚠️ Nenhum dado registrado ainda. Registre um jogo primeiro!")
