logs = [
    "2023-10-01 10:00:00 INFO User 105 logged in",
    "2023-10-01 10:05:23 ERROR Database connection failed",
    "2023-10-01 10:07:00 INFO User 105 requested /home",
    "2023-10-01 10:15:00 WARNING Memory usage above 80%",
    "2023-10-01 10:20:00 ERROR Timeout on API gateway",
    "2023-10-01 10:22:00 INFO User 202 logged in"
]
def analisar_logs(lista_logs):
    
    dicionario={}
    for n in lista_logs:
                frase = n.split()
                categoria = frase[2]
                if categoria in dicionario :
                    valor_aux = 1
                    dicionario[categoria] = dicionario[categoria] + valor_aux   
                else:
                    dicionario[categoria] = 1


    print(dicionario)

analisar_logs(logs)