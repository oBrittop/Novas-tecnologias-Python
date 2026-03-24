dicionario1 = [
    {"nome": "Gustavo Brito", "email":"gustavo@gmail.com", "status_ativo":True},
    {"nome": "Leticia Brito", "email":"let@gmail.com", "status_ativo":False},
    {"nome": "Anna Brito", "email":"anna@gmail.com", "status_ativo":True},
    {"nome": "Sandra Brito", "email":"sandy@gmail.com", "status_ativo":True},
    {"nome": "Ailton Brito Junior", "email":"jr@gmail.com", "status_ativo":True},
    {"nome": "Ailton Brito", "email":"dufrete@gmail.com", "status_ativo":True}
]

def limpar_dados(lista):
    lista_filtrada = list(filter(lambda u: u["status_ativo"] == True, lista))
    
    for usuario in lista_filtrada:
        usuario["nome"] = usuario["nome"].upper()
        usuario["email"] = usuario["email"].lower()
        
    return lista_filtrada


resultado = limpar_dados(dicionario1)

for item in resultado:
    print(item)

