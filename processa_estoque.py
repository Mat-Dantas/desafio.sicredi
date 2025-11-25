import pandas as pd
import locale
import os

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:

    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR')
    except locale.Error:
        # Se falhar, usa o padrão C e formata manualmente
        print("Aviso: Locale 'pt_BR' não encontrado. A formatação de moeda pode não ser ideal.")
        def format_currency(value):
            return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    else:
        def format_currency(value):
            return locale.currency(value, grouping=True, symbol=True)
else:
    def format_currency(value):
        return locale.currency(value, grouping=True, symbol=True)

def processar_estoque(arquivo_csv="estoque.csv", arquivo_relatorio="relatorio.txt"):
    """
    Processa o arquivo CSV de estoque, realiza os cálculos e gera o relatório.
    """
    if not os.path.exists(arquivo_csv):
        with open(arquivo_relatorio, "w") as f:
            f.write(f"ERRO: Arquivo de entrada '{arquivo_csv}' não encontrado.")
        print(f"ERRO: Arquivo de entrada '{arquivo_csv}' não encontrado. Relatório de erro gerado.")
        return
    
        # Ler o arquivo CSV
    try:
        df = pd.read_csv(
            arquivo_csv,
            sep=',',
            decimal='.',
            dtype={'Produto': str, 'Preço': float, 'Quantidade': int}
        )
    except Exception as e:
        with open(arquivo_relatorio, "w") as f:
            f.write(f"ERRO ao ler o arquivo CSV: {e}")
        print(f"ERRO ao ler o arquivo CSV. Verifique o formato. Relatório de erro gerado.")
        return

    # 1. Calcular o Valor Total do Estoque
    df['Valor_Total'] = df['Preço'] * df['Quantidade']
    valor_total_estoque = df['Valor_Total'].sum()

    # 2. Identificar Produto Mais Caro e Mais Barato
    produto_mais_caro = df.loc[df['Preço'].idxmax()]
    produto_mais_barato = df.loc[df['Preço'].idxmin()]

    # 3. Produtos com Quantidade Abaixo de 5 Unidades
    produtos_baixo_estoque = df[df['Quantidade'] < 5]

    # Gerar o arquivo de relatório
    with open(arquivo_relatorio, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("RELATÓRIO DE ESTOQUE\n")
        f.write("=" * 50 + "\n\n")

        # Valor Total do Estoque
        f.write(f"1. Valor Total do Estoque:\n")
        f.write(f"   {format_currency(valor_total_estoque)}\n\n")

        # Produto Mais Caro
        f.write(f"2. Produto Mais Caro:\n")
        f.write(f"   Produto: {produto_mais_caro['Produto']}\n")
        f.write(f"   Preço: {format_currency(produto_mais_caro['Preço'])}\n\n")

        # Produto Mais Barato
        f.write(f"3. Produto Mais Barato:\n")
        f.write(f"   Produto: {produto_mais_barato['Produto']}\n")
        f.write(f"   Preço: {format_currency(produto_mais_barato['Preço'])}\n\n")

        # Produtos com Quantidade Abaixo de 5 Unidades
        f.write(f"4. Produtos com Quantidade Abaixo de 5 Unidades:\n")
        if produtos_baixo_estoque.empty:
            f.write("   Nenhum produto encontrado.\n")
        else:
            for index, row in produtos_baixo_estoque.iterrows():
                f.write(f"   - {row['Produto']} (Quantidade: {row['Quantidade']} | Preço: {format_currency(row['Preço'])})\n")
        f.write("\n" + "=" * 50 + "\n")
        f.write("FIM DO RELATÓRIO\n")

    print(f"Processamento concluído. O relatório foi salvo em '{arquivo_relatorio}'.")

if __name__ == "__main__":

    processar_estoque()