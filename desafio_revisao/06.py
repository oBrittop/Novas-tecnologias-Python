notas_brutas = [
    {"aluno": "Ana", 
     "materia": "Matematica", 
     "nota": 8.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 6.0},
    {"aluno": "Beatriz", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Joao", "materia": "Historia", "nota": 7.5},
    {"aluno": "Mariana", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Pedro", "materia": "Matematica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Julia", "materia": "Quimica", "nota": 6.5},
    {"aluno": "Rafael", "materia": "Historia", "nota": 9.5},
    {"aluno": "Sofia", "materia": "Biologia", "nota": 10.0},
    {"aluno": "Ana", "materia": "Fisica", "nota": 9.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 4.5},
    {"aluno": "Beatriz", "materia": "Matematica", "nota": 7.0},
    {"aluno": "Joao", "materia": "Quimica", "nota": 5.0},
    {"aluno": "Mariana", "materia": "Historia", "nota": 8.5},
    {"aluno": "Pedro", "materia": "Biologia", "nota": 6.0},
    {"aluno": "Lucas", "materia": "Matematica", "nota": 8.0},
    {"aluno": "Julia", "materia": "Fisica", "nota": 7.5},
    {"aluno": "Rafael", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Sofia", "materia": "Historia", "nota": 9.0},
    {"aluno": "Ana", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 3.0},
    {"aluno": "Beatriz", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Joao", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Mariana", "materia": "Quimica", "nota": 9.5},
    {"aluno": "Pedro", "materia": "Historia", "nota": 4.0},
    {"aluno": "Lucas", "materia": "Biologia", "nota": 7.0},
    {"aluno": "Julia", "materia": "Matematica", "nota": 8.5},
    {"aluno": "Rafael", "materia": "Fisica", "nota": 6.0},
    {"aluno": "Sofia", "materia": "Quimica", "nota": 9.5},
    {"aluno": "Ana", "materia": "Matematica", "nota": 4.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 5.0},
    {"aluno": "Beatriz", "materia": "Historia", "nota": 7.5},
    {"aluno": "Joao", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 6.0},
    {"aluno": "Pedro", "materia": "Fisica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Julia", "materia": "Historia", "nota": 8.0},
    {"aluno": "Rafael", "materia": "Biologia", "nota": 7.5},
    {"aluno": "Sofia", "materia": "Matematica", "nota": 10.0},
    {"aluno": "Ana", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Carlos", "materia": "Historia", "nota": 6.5},
    {"aluno": "Beatriz", "materia": "Biologia", "nota": 9.5},
    {"aluno": "Joao", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Pedro", "materia": "Quimica", "nota": 6.0},
    {"aluno": "Lucas", "materia": "Historia", "nota": 8.5},
    {"aluno": "Julia", "materia": "Biologia", "nota": 9.0},
    {"aluno": "Rafael", "materia": "Matematica", "nota": 5.0},
    {"aluno": "Sofia", "materia": "Fisica", "nota": 8.5},
    {"aluno": "Ana", "materia": "Historia", "nota": 9.0},
    {"aluno": "Carlos", "materia": "Biologia", "nota": 5.5},
    {"aluno": "Beatriz", "materia": "Matematica", "nota": 8.5},
    {"aluno": "Joao", "materia": "Quimica", "nota": 6.0},
    {"aluno": "Mariana", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Pedro", "materia": "Historia", "nota": 7.0},
    {"aluno": "Lucas", "materia": "Biologia", "nota": 7.5},
    {"aluno": "Julia", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Rafael", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Sofia", "materia": "Historia", "nota": 10.0},
    {"aluno": "Ana", "materia": "Biologia", "nota": 8.5},
    {"aluno": "Carlos", "materia": "Quimica", "nota": 4.0},
    {"aluno": "Beatriz", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Joao", "materia": "Historia", "nota": 8.5},
    {"aluno": "Mariana", "materia": "Biologia", "nota": 9.0},
    {"aluno": "Pedro", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Lucas", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Julia", "materia": "Quimica", "nota": 7.0},
    {"aluno": "Rafael", "materia": "Historia", "nota": 6.0},
    {"aluno": "Sofia", "materia": "Biologia", "nota": 9.5},
    {"aluno": "Ana", "materia": "Matematica", "nota": 9.5},
    {"aluno": "Carlos", "materia": "Fisica", "nota": 5.0},
    {"aluno": "Beatriz", "materia": "Quimica", "nota": 8.0},
    {"aluno": "Joao", "materia": "Matematica", "nota": 7.0},
    {"aluno": "Mariana", "materia": "Historia", "nota": 8.5},
    {"aluno": "Pedro", "materia": "Biologia", "nota": 5.0},
    {"aluno": "Lucas", "materia": "Matematica", "nota": 9.0},
    {"aluno": "Julia", "materia": "Fisica", "nota": 8.5},
    {"aluno": "Rafael", "materia": "Quimica", "nota": 7.5},
    {"aluno": "Sofia", "materia": "Historia", "nota": 9.0},
    {"aluno": "Ana", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Carlos", "materia": "Matematica", "nota": 6.0},
    {"aluno": "Beatriz", "materia": "Matematica", "nota": 9.0},
    {"aluno": "Joao", "materia": "Quimica", "nota": 5.5},
    {"aluno": "Mariana", "materia": "Fisica", "nota": 7.0},
    {"aluno": "Pedro", "materia": "Historia", "nota": 6.5},
    {"aluno": "Lucas", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Julia", "materia": "Matematica", "nota": 7.5},
    {"aluno": "Rafael", "materia": "Fisica", "nota": 8.0},
    {"aluno": "Sofia", "materia": "Quimica", "nota": 10.0},
    {"aluno": "Ana", "materia": "Quimica", "nota": 9.0},
    {"aluno": "Carlos", "materia": "Historia", "nota": 4.5},
    {"aluno": "Beatriz", "materia": "Biologia", "nota": 8.5},
    {"aluno": "Joao", "materia": "Fisica", "nota": 6.5},
    {"aluno": "Mariana", "materia": "Matematica", "nota": 9.0},
    {"aluno": "Pedro", "materia": "Quimica", "nota": 5.5},
    {"aluno": "Lucas", "materia": "Historia", "nota": 7.0},
    {"aluno": "Julia", "materia": "Biologia", "nota": 8.0},
    {"aluno": "Rafael", "materia": "Matematica", "nota": 6.5},
    {"aluno": "Sofia", "materia": "Fisica", "nota": 9.5}
]

def media(notas,qtde_prova):
    for n in notas:
        n += n
        nota_media = (n/qtde_prova)

boletins = {
    "Ana" : {
        "medias_dis":{
            "matematica": 0.0,
            "fisica" : 0.0 
        },
        "media_geral":0.0,
        "status":"aproavdo"
    }
}
    # {"aluno": "Ana", 
    #  "materia": "Matematica", 
    #  "nota": 8.5},


for n in notas_brutas:
    nome_aluno = n["aluno"]
    if nome_aluno in n["aluno"]:
        #daqui pra baixo e para guardar a qtde de prova por materia 
        dic_materias={
                     "Matematica": 0,
                     "Fisica": 0,
                     "Biologia": 0,
                      "Quimica": 0,
                     "Historia": 0
            }
        for materia in dic_materias:
                if n["materia"] == materia:
                    qtde_prova += 1
        media = media(n["nota"], qtde_prova)   



        medias_diciplinas = {
            "media" : media,
            

        }