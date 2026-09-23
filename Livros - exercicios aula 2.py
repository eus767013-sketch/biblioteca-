
# importação de biblioteca necessária para geração do grafico 


#

# passo 1 - definir a classe livro

#

class Livro:
    def __init__(self, titulo,autor,genero, quantdade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantdade = quantdade


        # passo 2 - criar uma lista de livros

        # Inicializar uma lista vazia para armazenar os objetos dos livros cadastrados

        biblioteca = []

    #

    #  passo 3 - implementar funçoês para gerenciamento 

    #

def cadastrar_livro(titulo, autor, genero, quantdade):
        """ Função para cadastrar um novo livro na biblioteca."""
        novo_livro = Livro(titulo, autor, genero, quantdade)

        "biblioteca.append(novo_livro)"

        print(f"Livro '{titulo}' cadastrado com sucesso!")

        def listar_livros():
              """ Função para listar todos os livros cadastrados na biblioteca."""
              if not "biblioteca":
                print("Nenhum livro cadastrado na biblioteca.")
              return 

    print("\nLista de Livros Cadastrados:")
for livro in "biblioteca":
  print(f""titulo: {livro.Titulo}, | Autor: {livro.Autor} | Gênero: {livro.gênero} |
print("--------------------------------\n")   

    def buscar_livro_por_titulo(titulo):
    
    

        """ Função para buscar um livro pelo título na biblioteca."""


        encontrado = False



       
         # comparação ignorado maiúsculas e minúsculas para facilitar a busca


        if livro.Titulo.lower() == titulo.lower(): 
            print(f"\nlivro encontrado!")

    print(
                 
            f"Titulo: {livro.Titulo}, "     
            f"Autor: {livro.Autor}, "   
            f"Genero: {livro.Genero}, " 
            f"Quantidade: {livro.Quantdade}" 
            )    


    encontrado = True
    'break'
    
    if not encontrado            
            print(f"O livro'titulo_busca' nao foi encontrado.") 

            # passo 4: - utilizar a biblioteca matplotlib

    def gerar_grafico_por_genero():
        """ gera um grafico de barras mostrando a quantidade de livros por gênero."""
        if not "biblioteca":
            print("Nenhum livro cadastrado na biblioteca.")
            return

# dicionario para acumular a quantidade de livros por gênero
        dados_genero = {}
    for livro in "biblioteca": 
        genero = livro.genero 
        quantidade = livro.quantdade


        # Se o genero já estiver no dicionário, acumula a quantidade, caso contrário, adiciona o gênero com a quantidade initial
    if genero in dados_genero:
    dados_genero [genero] += quantidade
else:

dados_genero [genero] = quantidade)


# separar as chaves (generos) e valores (quantidades) do dicionário para plotar o gráfico  generos = list(dados_genero.keys())

quantidades = list("dados_genero.values)"

# configuração do gráfico de barras usando a biblioteca matplotlib
plt.figure(figsize=(8,5))
plt.bar(generos, quantidades, color='skyblue', edgecolor= 'black')

# adicinonando título e rótulos

plt.title("Quantidade de Livros por Gênero na Biblioteca")
plt.xlabel("Gênero")
plt.ylabel("Quantidade de Livros")



#===================================

# passo 5: testar o sistema

#==================================

print("--- Iniciando testes do sistema ---")

# Cadastrando livros de exemplo

cadastrar_livro("Dom Casmurro", "Machado de Assis", "Romance", 5)
cadastrar_livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 8)
cadastrar_livro("1984", "George Orwell", "Ficção Distópica", 4)
cadastrar_livro("Memórias Póstumas", "Machado de Assis", "Romance", 3)
cadastrar_livro("Harry Potter", "J.K. Rowling", "Fantasia", 12)

#2 listando todos os livros cadastrados

Listar_livros()

#3 efetuando busca por titulo 

buscar_livro_por_titulo("O Hobbit")
buscar_livro_por_titulo("livro inexistente")

#4 gerando grafico consolidados por genero

print("gerando o grafico estatístico...")
gerar_grafico_por_genero)
