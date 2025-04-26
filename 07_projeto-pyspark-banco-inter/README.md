
# Teste PySpark - Banco Inter

Este repositório contém a solução do **Teste de Conhecimentos em PySpark** proposto pelo Banco Inter.  
O objetivo foi aplicar conceitos de manipulação de dados, funções avançadas, performance, integração e processamento de grandes volumes de dados utilizando PySpark.

---

## Estrutura do Projeto

```
projeto-pyspark-banco-inter/
│
├── src/
│   ├── parte1_manipulacao_dados.py          # Criação, seleção, filtragem, agrupamento e ordenação de DataFrame
│   ├── parte2_funcoes_avancadas.py           # UDFs e Funções de Janela
│   ├── parte3_performance_otimizacao.py      # Particionamento e Broadcast Join
│   ├── parte4_integracao.py                  # Leitura de CSV, Escrita em Parquet, Integração com HDFS
│   └── parte5_problema_caso.py               # Processamento de Logs e Análise de Atividades
│
├── data/
│   ├── input/    # Arquivos CSV de entrada
│   └── output/   # Resultados gerados (Parquet e CSV)
│
└── README.md     # Este arquivo
```

---

## Implementação

### Parte 1: Manipulação de Dados
- Criação de DataFrame com colunas `Name`, `Age` e `Occupation`.
- Seleção apenas das colunas `Name` e `Age`.
- Filtragem dos registros onde `Age` > 30 anos.
- Agrupamento por `Occupation` e cálculo da média de idade.
- Ordenação dos resultados pela média de idade de forma decrescente.

### Parte 2: Funções Avançadas
- Criação de uma **User Defined Function (UDF)** para classificar idade em:
  - Jovem (< 30)
  - Adulto (30-40)
  - Sênior (> 40)
- Uso de **Window Functions** para calcular a diferença entre a idade do indivíduo e a média de idade por ocupação.

### Parte 3: Performance e Otimização
- **Particionamento** dos dados para otimizar leitura e escrita no armazenamento.
- **Broadcast Join** para otimizar junções de DataFrames onde um deles é pequeno.

### Parte 4: Integração com Outras Tecnologias
- Leitura de arquivos CSV.
- Escrita de resultados no formato Parquet.
- Exemplo de integração e leitura/escrita em **Hadoop HDFS**.

### Parte 5: Problema de Caso - Processamento de Logs
- Carga de arquivo de log com `timestamp`, `user_id`, `action`.
- Contagem de número de ações realizadas por cada usuário.
- Identificação dos 10 usuários mais ativos.
- Escrita do resultado final em arquivo CSV.

---

## Como executar localmente

1. Instale as dependências:
    ```bash
    pip install pyspark
    ```

2. Inicie o ambiente PySpark (ou Databricks, ou ambiente Hadoop configurado).

3. Execute cada script da pasta `src/` de acordo com a parte do teste que deseja validar:
    ```bash
    python src/parte1_manipulacao_dados.py
    python src/parte2_funcoes_avancadas.py
    ...
    ```

---

## Boas Práticas Aplicadas

- **Modularização:** Scripts separados por tema para organização e melhor manutenção.
- **Uso de UDFs e Window Functions:** Aplicações práticas para processamento avançado.
- **Performance:** Estratégias de particionamento e Broadcast Joins para otimização.
- **Integração:** Pronto para ler e escrever em Hadoop HDFS e formatos otimizados como Parquet.
- **Documentação:** Cada etapa do processo foi comentada para facilitar o entendimento.

---

##  Melhorias Futuras

- Automatizar testes unitários em PySpark (ex: `pytest + chispa`).
- Implementar logging estruturado (com `log4j` ou `logging` Python).
- Integrar orquestração de tarefas com **Apache Airflow** ou **Databricks Workflows**.

---

## Contato

Caso tenha interesse em discutir mais sobre este projeto:

- **Lindberg Gualberto Ferreira**
- 📧 Email: lindberggf@gmail.com
- 💼 LinkedIn: [(https://www.linkedin.com/in/lindberg-gualberto-ferreira-57a80078)](https://www.linkedin.com/in/lindberg-gualberto-ferreira-57a80078)

---

> Projeto desenvolvido com dedicação e foco em boas práticas de engenharia de dados.
