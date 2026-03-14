def saudacoes(nome):
    import random
    frases = ["Bom dia! meu nome é " + nome +". Como vai você?", "Olá! Tudo bem?", "Olá! Eu sou o chatbot especialista em counter strike 2!"]
    print(frases[random.randint(0,2)])

def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavrasProibidas=["Donk é melhor que FalleN", "noob", "Lol", "Valorant", "lixo"]
    for p in palavrasProibidas:
        if p in texto:
            print("Pode não man.")
            return recebeTexto()
        return texto
def buscaResposta(nome, texto):
    with open("conhecimento.txt","a+") as conhecimento:
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente: ","") == "Tchau":
                    print(nome+ ": Falou! Volte sempre que precisar!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                print("Sei lá man")
                conhecimento.write("\n" + texto)
                resposta_user = input("O que era pra eu responder?/n")
                conhecimento.write("\n" +"Chatbot: "+resposta_user)
                return "Humm..."
def exiberesposta(resposta, nome):
    print(resposta.replace("Chatbot",nome))
    if resposta == "fim":
        return "fim"
    return "continua"
            


