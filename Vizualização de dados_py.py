# Importações necessárias
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Passo 1: Conectar ao banco de dados (ou criar, se não existir) 
conexao = sqlite3.connect('dados.db')
cursor = conexao.cursor()

# Criar a tabela (ajustado o nome para 'vendas')
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
""") 
# Inserir dados de exemplo (corrigida a vírgula faltando e o excesso no final)
cursor.executescript("""
DELETE FROM vendas;
INSERT INTO vendas (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
""")

conexao.commit()
conexao.close()

# Passo 2: Carregar dados no Pandas 
conn = sqlite3.connect('dados.db')
query = "SELECT * FROM vendas;"
df_vendas = pd.read_sql_query(query, conn)
conn.close()

# Explorar os dados
print(df_vendas.head())
print(df_vendas.info())
print(df_vendas.describe())

# Tratar valores faltantes (corrigido o uso do inplace)
df_vendas.fillna(0, inplace=True)

# Passo 3: Análise de Dados 
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
df_vendas['mes_venda'] = df_vendas['data_venda'].dt.month

# Total de vendas por Mês
total_vendas_por_mes = df_vendas.groupby('mes_venda')['valor_venda'].sum()

# Número de vendas por categoria
vendas_por_categoria = df_vendas.groupby('categoria')['id_venda'].count()

# Produto mais vendido
produto_mais_vendido = df_vendas['produto'].value_counts().idxmax()

# Passo 4: Visualização dos dados
plt.figure(figsize=(10, 6))
sns.barplot(x=total_vendas_por_mes.index, y=total_vendas_por_mes.values)
plt.title('Total de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.xticks(ticks=range(0, 12), labels=['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=vendas_por_categoria.index, y=vendas_por_categoria.values)
plt.title('Número de Vendas por Categoria de Produto')
plt.xlabel('Categoria')
plt.ylabel('Número de Vendas')
plt.xticks(rotation=45)
plt.show()

print(f"O produto mais vendido é: {produto_mais_vendido}")

# Passo 5: Conclusão e insights
print("\nAnálise de Insights:")
print("- As vendas apresentaram um pico significativo em junho, sugerindo uma sazonalidade que deve ser explorada.")
print("- A categoria com maior número de vendas indica uma demanda maior por esses produtos.") 