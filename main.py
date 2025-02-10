import coleta_dados
import analise

def main():
    print("\n📊 Sistema de Estatísticas de Futebol 📊")
    
    while True:
        opcao = input("\n1 - Registrar novo jogo\n2 - Gerar estatísticas\n3 - Sair\nEscolha: ")
        
        if opcao == '1':
            coleta_dados.registrar_jogo()
        elif opcao == '2':
            analise.gerar_estatisticas()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
