from BinaryTree import BinaryTree

def readData(nome_do_arquivo: str)->dict:

    try:
        
        dominios = {}
        with open(nome_do_arquivo, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            line_format = line.strip("\n")
            line_format = line_format.split("/")
            if len(line_format) == 1:
                dominios[line_format[0]] = BinaryTree(line_format[0]) 
            else:
                arvore = dominios.get(line_format[0])  
                arvore.addDomain(line_format)

        return  dominios
   
    except FileNotFoundError as fnfe:
        print('ERRO:', fnfe)
    
# Inicio do Programa Principal

dominios = readData('urls.txt')

print("+------Opções de comandos------+")
print("| Busca de URL                 |")
print("| #viewtree - percorrer árvore |")       
print("| #sair - encerrar programa    |")
print("|______________________________|")    
print()

while(True):

    print("Digite a URL de pesquisa ou #sair para encerrar o programa.")
    
    input_url = input("URL: ").lower()
    print()

    if input_url[0:1] == "#":
        if input_url.lower() == "#sair": 
            print("Encerrando o programa...")
            print()
            break
        
        elif input_url.lower().split()[0] == "#viewtree":  
            try:  
                arv = dominios[input_url.split()[1]]
                arv.viewtree()
                print() 

            except KeyError:
                print("O domínio solicitado não consta no arquivo. Tente novamente!")
                print() 
            
            except IndexError:
                print("É necessário inserir o comando seguido de um domínio. Tente novamente!")
                print()

    else:
        try:  
            entrada_sites = input_url.split("/")
            site = dominios[entrada_sites[0]].match(entrada_sites)

            if site:
                print("200 OK - Requisição bem-sucedida!")
                print()
            else:
                print("400 Bad Request - Servidor não atendeu a requisição.") 
                print()

        except KeyError: 
            print("É necessário digitar uma URL ou comando válido. Tente novamente!")
            print()
