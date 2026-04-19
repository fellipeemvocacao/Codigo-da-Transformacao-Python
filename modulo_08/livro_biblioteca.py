class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []

    def adicionar_livro(self, livro):
        
        self.catalogo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca {self.nome}.")

    def listar_livros(self):
        
        print(f"\n--- Catálogo da Biblioteca {self.nome} ---")
        for livro in self.catalogo:
            print(livro)

    def emprestar_livro(self, titulo):
        
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"\nSucesso: O livro '{livro.titulo}' foi emprestado.")
                    return
                else:
                    print(f"\nErro: O livro '{livro.titulo}' já está ocupado.")
                    return
        print(f"\nErro: Livro '{titulo}' não encontrado no catálogo.")

    def devolver_livro(self, titulo):
        
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                livro.disponivel = True
                print(f"\nObrigado: O livro '{livro.titulo}' foi devolvido.")
                return