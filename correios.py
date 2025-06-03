
pacotes= ( "ABC123"), ("XYZ789"),("DEF456"),("JKL321"), ("MNO654"),("PQR987"),("STU741")
rastreio= ("Enviado", "Recebido", "Em transito", "Enviado", "Recebido",         "Em transito", "Enviado")

# 1- Conte quantos pacotes estão em cada status: "Enviado", "Recebido",e "Em transito".
status_enviado = print ("quantos pacotes estao enviados?", rastreio.count("Enviado"))
status_recebido = print ("quantos pacotes estao recebidos?", rastreio.count("Recebido"))
status_transito = print ("quantos pacotes estao em transito?", rastreio.count("Em transito"))
#2- listar apenas os codigos dos pacotes com status "Em Transito".
pacotes_em_transito = [pacotes[i] for i in range(len(rastreio)) if rastreio[i] == "Em transito"]
print (" Codigos dos pacotes com status em transito", pacotes_em_transito) 
#3- Use uma funçao que recebe um codigo de rastreamento e retorna o status do pacote, ou uma mensagem informando que o pacote nao esta cadastrado.
codigo= input("Digite o codigo de rastreamento: ")

if codigo in pacotes:
    status = rastreio[pacotes.index(codigo)]
    print(f"O pacote {codigo} esta no status {status}")
else:
    print(f"O pacote {codigo} nao esta cadastrado")
#4- Ordenar os pacotes pelo codigo de rastreamento e exiba a tupla ordenada. Desenvolva um programa que execute essas operaçoes e exiba os resultados, explicando 
# o que cada linha exibe.

pacotes_ordenados = sorted(rastreio)
print("Pacotes ordenados pelo codigo de rastreamento:", pacotes_ordenados)












    

  