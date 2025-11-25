# Desafio Técnico - Analista de IA

Este repositório contém a solução para o **Desafio 3** do processo seletivo para Analista de IA. O objetivo foi desenvolver um script em Python para automação de análise de estoque.

## 📋 Sobre o Projeto

O script realiza a leitura de uma base de dados de produtos (`csv`), processa as informações de negócio e gera um relatório gerencial automático.

**Funcionalidades:**
* Leitura e validação de arquivo CSV.
* Cálculo do valor total em estoque.
* Identificação do produto com maior e menor valor unitário.
* Filtro de produtos com baixo estoque (abaixo de 5 unidades).
* Geração automática de arquivo de saída `relatorio.txt`.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* Bibliotecas Nativas: `csv`, `pandas`.

## 🚀 Como Executar

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/mat-dantas/desafio.sicred.git](https://github.com/mat-dantas/desafio.sicred.git)
    ```
2.  Acesse a pasta do projeto:
    ```bash
    cd desafio_python_3
    ```
3.  Certifique-se de que o arquivo `estoque.csv` está na mesma pasta.
4.  Execute o script:
    ```bash
    python3 processa_estoque.py
    ```
5.  Verifique o resultado no arquivo `relatorio.txt` gerado.

## 📦 Estrutura dos Arquivos

* `processa_estoque.py`: Código fonte principal com lógica e funções documentadas.
* `estoque.csv`: Base de dados para teste (Produto, Preço, Quantidade).
* `relatorio.txt`: Arquivo de saída gerado após a execução.

---
Desenvolvido como parte do teste técnico prático.