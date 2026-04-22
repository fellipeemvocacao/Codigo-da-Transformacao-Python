'''
Criar um Sistema de Biblioteca

Class Livro

    (Produtos) 
    Livros, Periodicos, Jornal, Maps, Gibi/Mangás

Class Biblioteca (main)

    (Processos / Serviços)
    Ler, Pesquisa, Emprestado-Devolução
'''
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [{status}]"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca {self.nome}.")

    def emprestar_livro(self, titulo_procurado):
        
        for livro in self.livros:
            if livro.titulo == titulo_procurado:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Empréstimo de '{livro.titulo}' realizado!")
                else:
                    print(f"O livro '{livro.titulo}' já está ocupado.")
                    return
        print(f"Livro não encontrado no acervo.")

biblioteca_municipal = Biblioteca()

l1 = Livro("Confissões", "Santo Agostinho")
l2 = Livro("Suma Teológica", "São Tomás de Aquino")
l3 = Livro("Imitação de Cristo", "Tomás de Kempis")

biblioteca_municipal.livros = [] 
biblioteca_municipal.nome = "Municipal"

biblioteca_municipal.adicionar_livro(l1)
biblioteca_municipal.adicionar_livro(l2)
biblioteca_municipal.adicionar_livro(l3)
biblioteca_municipal.emprestar_livro("Confissões")

print(l1)