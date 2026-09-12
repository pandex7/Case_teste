# Ingestão de dados de API para o Amazon Redshift

## O projeto

Este é um teste técnico para Engenharia de Dados. A proposta é realizar web scraping na API do GitHub para identificar possíveis candidatos que possam compor a equipe técnica de dados do iFood.

![Arquitetura do projeto](https://github.com/pandex7/Case_teste/blob/main/assets/1.png)

O projeto é hospedado na AWS e utiliza os seguintes serviços:

- **AWS Glue:** serviço de ETL.
- **AWS Step Functions:** orquestra as funções usadas no processamento dos dados do GitHub.
- **Amazon Redshift:** camada final de armazenamento do Data Warehouse.
- **AWS Lambda:** funções de integração entre os serviços AWS.
- **Amazon S3:** armazenamento dos dados.
- **Amazon EventBridge:** gatilhos e agendamentos usados no Data Lake.

## Início do processo

Um agendamento CRON no Amazon EventBridge inicia a captura de dados do GitHub para o Data Lake.

- **GetGithubSecret:** busca os tokens no AWS Secrets Manager (`aws-sdk:secretsmanager:getSecretValue`).
- **api-github-spectrum:** processo de ETL que carrega dados da API do GitHub no Amazon S3. Os dados são consultados no Redshift por meio do Spectrum; os detalhes estão no código.
- **StartCrawlerGithub:** crawler responsável por esquemas, metadados e aceleração do ETL.
- **LoadGithubFlow:** utiliza Amazon SQS (pub/sub) para notificações em tempo real e escalabilidade.

O foco do case é o script de ETL `teste_ifood.py`. As funções Lambda de integração entre os serviços e os comentários relativos ao Boto não foram incluídos no script de teste. A solução representa uma ingestão completa, desde a camada de Data Lake até o Amazon Redshift.
