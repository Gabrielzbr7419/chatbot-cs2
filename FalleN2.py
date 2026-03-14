import chat.py as pc

nome_maquina = "FalleN2"
pc.saudacoes(nome_maquina)
while True:
    texto = pc.pcrecebeTexto()
    resposta = pc.exibeResposta(nome_maquina, texto)
    if pc.exibeResposta(resposta, nome_maquina) == 'fim':
        break