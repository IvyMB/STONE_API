# STONE_API
# Projeto de Análise de Dados e Recomendação de MCC

Este projeto utiliza uma API Flask para manipular conjuntos de dados, aplicar lógica matemática e fornecer recomendações sobre os melhores MCCs (Merchant Category Codes) para determinados estados, além de identificar os itens de venda mais eficazes para lojas. Através da aplicação de algoritmos e lógica matemática, o sistema visa otimizar a tomada de decisões para estratégias de vendas e marketing.

## Funcionalidades Atuais

1. **Recomendação de MCCs:**
   - Identifica os melhores MCCs para cada estado com base em dados históricos e algoritmos matemáticos.
   
2. **Itens de Venda:**
   - Fornece uma lista dos itens mais vendidos em cada loja, ajudando a melhorar a estratégia de estoque e marketing.

## Planejamento Futuro

A API será expandida para incluir os seguintes endpoints e funcionalidades:

1. **Tendências Mensais:**
   - Visualizar tendências de cada MCC por mês para entender padrões sazonais e comportamentos de compra ao longo do ano.

2. **Melhor Horário de Venda:**
   - Determinar o melhor horário de venda para cada MCC e item, otimizando horários de operação e campanhas promocionais.

3. **Análise de Horário de Venda:**
   - Fornecer insights detalhados sobre o horário de venda de cada item, ajudando a alinhar o estoque com as horas de maior demanda.

## Configuração e Execução

### Pré-requisitos

- Python 3.7 ou superior
- Flask
- Pandas
- NumPy

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/IvyMB/STONE_API.git
   cd STONE_API

2. Crie um ambiente virtual e ative-o:

   ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows: venv\Scripts\activate

3. Instale as dependências:

   ```bash
    pip install -r requirements.txt
    
4. Inicie o servidor Flask:

    ```bash
    python app.py

## Acesse a API em nosso frontend ou usando uma ferramenta como Postman:

1. Recomendação de MCCs:

    Endpoint: /api/best_mcc_per_state
    Método: POST
    Parâmetros: state (ex: RN)

2. Itens de Venda:

    Endpoint: /api/best_items_by_document_id
    Método: POST
    Parâmetros: document_id (ex: 9202060645083883366)

## Contribuições
Se você deseja contribuir para este projeto, por favor, siga as diretrizes abaixo:

- Faça um fork do repositório.
- Crie uma branch para sua feature ou correção.
- Faça commit das suas alterações.
- Envie um pull request para o branch principal.
