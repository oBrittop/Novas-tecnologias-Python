dicionario1=[
    {"nome": "Gustavo Brito", "email":"gustavo@gmail.com", "status_ativo":True},
    {"nome": "Leticia Brito", "email":"let@gmail.com", "status_ativo":False},
    {"nome": "Anna Brito", "email":"anna@gmail.com", "status_ativo":True},
    {"nome": "Sandra Brito", "email":"sandy@gmail.com", "status_ativo":True},
    {"nome": "Ailton Brito Junior", "email":"jr@gmail.com", "status_ativo":True},
    {"nome": "Ailton Brito", "email":"dufrete@gmail.com", "status_ativo":True}

]
for nome in dicionario1:
    dicionario1[nome]["nome"]= nome["nome"].upper()
    
for email in dicionario1:
    dicionario1[email]["email"] = email["email"].lower()
   
lista = dicionario1
listatrue = list(filter(lambda lista: lista["status_ativo"] == True, lista))
print(lista)
print("\n\n")
print(listatrue)