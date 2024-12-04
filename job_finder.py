from googlesearch import search
from colorama import Fore, Style, init

init(autoreset=True)

def exibir_ascii():
    ascii_art = f"""
{Fore.GREEN}

███████╗██╗███╗   ██╗██████╗ ███████╗██████╗          ██╗ ██████╗ ██████╗ 
██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗         ██║██╔═══██╗██╔══██╗
█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝         ██║██║   ██║██████╔╝
██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗    ██   ██║██║   ██║██╔══██╗
██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║    ╚█████╔╝╚██████╔╝██████╔╝
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚════╝  ╚═════╝ ╚═════╝ 
                                                                                                                      
    """
    print(ascii_art)
    print(f"{Fore.YELLOW}{Style.BRIGHT}Bem-vindo ao Finder Job! 🚀\n")

def buscar_vagas(site):
    queries = [
        f"site:{site} 'trabalhe conosco'",
        f"site:{site} 'carreiras'",
        f"site:{site} 'vagas'",
        f"site:{site} 'oportunidades'",
    ]
    
    results = []
    for query in queries:
        print(f"{Fore.GREEN}\n🔍 Buscando: {query}\n")
        for url in search(query, num_results=30):
            results.append(url)
            print(f"{Fore.BLUE}{url}")
    return results

def salvar_resultados(resultados, arquivo="resultados_busca.txt"):
    with open(arquivo, "w") as file:
        for link in resultados:
            file.write(link + "\n")
    print(f"\n{Fore.GREEN}✅ Resultados salvos no arquivo: {arquivo}")

def main():
    exibir_ascii()
    print(f"{Fore.CYAN}Digite o domínio do site que deseja pesquisar:")
    site = input(f"{Fore.YELLOW}Exemplo (empresa.com): ").strip()
    resultados = buscar_vagas(site)
    
    if resultados:
        print(f"\n{Fore.MAGENTA}🌟 Foram encontrados {len(resultados)} resultados.")
        salvar = input(f"{Fore.CYAN}Deseja salvar os resultados em um arquivo? (s/n): ").lower()
        if salvar == 's':
            salvar_resultados(resultados)
    else:
        print(f"{Fore.RED}⚠️ Nenhum resultado encontrado. Tente outro site ou ajuste as palavras-chave.")

if __name__ == "__main__":
    main()
