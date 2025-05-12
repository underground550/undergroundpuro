# undergroundpuro
import os
import itertools
from time import sleep
from colorama import Fore, Style, init

init()

def banner():
    os.system('clear')
    print(Fore.GREEN + """
====================================
       UndergroundPuro Painel
====================================""" + Style.RESET_ALL)

def nmap():
    alvo = input(Fore.GREEN + "\n[+] Digite o IP ou domínio para escanear: " + Style.RESET_ALL)
    os.system(f"nmap -sV {alvo}")

def hydra():
    print(Fore.GREEN + "\n[+] Modo de testes de quebra de senhas - Apenas para fins educacionais" + Style.RESET_ALL)
    dicas = input("[+] Dicas de senhas (separadas por vírgulas): ").split(',')
    min_chars = int(input("[+] Número mínimo de caracteres: "))
    max_chars = int(input("[+] Número máximo de caracteres: "))
    url = input("[+] URL do alvo (exemplo: http://alvo.com/login): ")

    print(Fore.YELLOW + "\n[*] Gerando combinações..." + Style.RESET_ALL)
    combinacoes = set()

    for i in range(min_chars, max_chars + 1):
        for combo in itertools.product(dicas, repeat=i):
            tentativa = ''.join(combo)
            combinacoes.add(tentativa)

    print(f"\n[*] Total de combinações geradas: {len(combinacoes)}")

    print(Fore.CYAN + f"\n[*] Iniciando testes na URL: {url} (modo simulado)\n" + Style.RESET_ALL)
    for senha in list(combinacoes)[:15]:  # simular apenas 15 tentativas
        print(f"[TESTE] Tentando senha: {senha}")
        sleep(0.2)  # simulação
    print(Fore.GREEN + "\n[FIM] Teste concluído (modo simulado)." + Style.RESET_ALL)

def bot():
    print(Fore.CYAN + "\n[+] Bot beta ainda em construção..." + Style.RESET_ALL)

def main():
    while True:
        banner()
        print(Fore.GREEN + """
[1] Nmap (varredura de redes)
[2] Hydra (quebra de senhas)
[3] Bot (beta)
[0] Sair
""" + Style.RESET_ALL)

        opcao = input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL)

        if opcao == '1':
            nmap()
        elif opcao == '2':
            hydra()
        elif opcao == '3':
            bot()
        elif opcao == '0':
            print(Fore.RED + "\nSaindo..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nOpção inválida!" + Style.RESET_ALL)
        input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    main()# undergroundpuro
