# Ingestão de API para O redshift

# O Projeto

Teste tecnico de engenheiro de dados.
WebScraping do github para Identificar possíveis candidatos para compor
o time Técnico da área de dados do Ifood.


# O Projeto 

![imagem](https://github.com/pandex7/Case_teste/blob/main/assets/1.png)

O projeto é hospedado na AWS e utiliza uma ampla gama de serviços disponibilizado pela Amazon, entre eles:

AWS Glue: serviço de ETL

Step Function: concentra as SFNs usadas pelo Github para processamento dos dados

AWS Redshift: banco de dados final do data warehouse

Lambda: Funções de conexões entre os serviços AWS

S3: Storage 

EventBrigde: triggers e schedules usados pelo DataLake

# Inicio do Processo

CRON no EventBridge
Atráves do Trigger a carga de dados inicia o processo de captura de dados do github para o DataLake

- GetGithubSecret > Faz a busca dos tokens no Secret Manager (aws-sdk:secretsmanager:getSecretValue")
- api-github-spectrum > ETL> carrega os dados da API do github para o S3 (os dados são consultados no Redshift via Spectrum), Mais detalhes no código
- StartCrawlerGithub > Crawler > Schemas, Metadados e Aceleração do ETL
- LoadGithubFlow > SQS(pub/sub) > Notificação em tempo real, escabilidade

Não vou me estender no processos da AWS, pois o foco seria a parte do ETL Script teste_ifood.py
Código simplista para ETL, faltando as funçoes lambda para conexão dos serviços e comentario do boto no script do teste.

mas ficaria algo assim uma ingestão completa para a camada do Datalake até o redshift.
