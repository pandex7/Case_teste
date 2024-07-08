import logging
import requests
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime, to_date, regexp_replace
from pyspark.sql.types import StringType, LongType


# Configurações GitHub API
github_api_url = "https://api.github.com"
username = "marciocl"
authorization_token = "Bearer (Use_o_Seu)"

# Função para obter detalhes dos seguidores
def get_followers_details(username):
    followers_url = f"{github_api_url}/users/{username}/followers"
    headers = {
        "Authorization": authorization_token,
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Obtendo lista de seguidores
        followers_response = requests.get(followers_url, headers=headers)
        followers_data = followers_response.json()

        follower_details = []

        # Iterando sobre cada seguidor para obter detalhes
        for follower in followers_data:
            follower_url = f"{github_api_url}/users/{follower['login']}"
            follower_response = requests.get(follower_url, headers=headers)
            follower_data = follower_response.json()

            # Construindo um dicionário com os dados do seguidor
            follower_details.append({
                'name': follower_data['name'],
                'company': follower_data['company'],
                'blog': follower_data['blog'],
                'email': follower_data['email'],
                'bio': follower_data['bio'],
                'public_repos': follower_data['public_repos'],
                'followers': follower_data['followers'],
                'following': follower_data['following'],
                'created_at': follower_data['created_at']
            })

        return follower_details

    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao acessar a API do GitHub: {e}")
        return None



# Configuração do Spark Session
spark = SparkSession.builder \
    .appName("GitHub Followers Analysis") \
    .getOrCreate()

# Obtendo os detalhes dos seguidores
followers_details = get_followers_details(username)

if followers_details:

    df = spark.createDataFrame(followers_details)

    #Convertendo Coluna para Bigint
    df = df.withColumn('public_repos', col('public_repos').cast(LongType()))
    df = df.withColumn('followers', col('followers').cast(LongType()))
    df = df.withColumn('following', col('following').cast(LongType()))


    # Salvar como CSV
    #df.coalesce(1).write.option("header", "true").csv("github_followers.csv")
    df.show()
    # Mensagem de conclusão
    logging.info(f"Dados salvos com sucesso")

    # Encerrando a sessão do Spark
    spark.stop()

else:
    logging.error(f"Verifique a conexão com a API do GitHub.")
