class Usuario:
    def __init__(self, iid, nome, email):
        self.__iid = iid
        self.nome = nome
        self.email = email
# --- GETTERS ---
    @property
    def iid(self):
        return self.__iid

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email
    
    # --- SETTERS ---
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @email.setter
    def email(self, novo_email):
        # Regra de negócio: validar o "@"
        if "@" in novo_email:
            self.__email = novo_email
        else:
            print(f"\nErro: E-mail '{novo_email}' inválido!")
            print(f"Problema com datastro id:{self.iid}")
            self.__email = "INVALIDO!"
class GerenciadorUsuario:
    def __init__(self):
        self.lista = []
    
    def adicionar_usuario(self, usuario):
        self.lista.append(usuario)
        print("usuario cadastrado")

    def remover_usuario_por_id(self, id_busca):
        tamanho_original = len(self.lista)
        self.lista = [u for u in self.lista if u.iid != id_busca]
        if len(self.lista) < tamanho_original:
            print("Id removido com sucesso")
        else:
            print("id nao encontrado")
    
    def listar_usuarios(self):
        print("--Lista de Usuarios")
        for n in self.lista:
            print(f"Id: {n.iid}\nNome:{n.nome}\nEmail:{n.email}")
            print("-----------------------------")
gerenciador = GerenciadorUsuario()
user1 = Usuario(1, "Gustavo", "gusta@email.com")
user2 = Usuario(2, "Joao", "joao.com") # Vai dar erro no futuro se usar o setter
gerenciador.adicionar_usuario(user1)
gerenciador.adicionar_usuario(user2)
gerenciador.listar_usuarios()
gerenciador.listar_usuarios()
    

