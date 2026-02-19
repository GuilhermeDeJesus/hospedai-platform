import redis
import json
from app.domain.repositories.conversation_cache_repository import ConversationCacheRepository

class RedisRepository(ConversationCacheRepository):
    def __init__(self, host='redis-10759.c11.us-east-1-3.ec2.cloud.redislabs.com', port=10759, decode_responses=True, username="default", password='aqy2CKJYV5GTim5Nc0T899YOK9L60a4O'):
        self.client = redis.Redis(host=host, port=port, decode_responses=decode_responses, username=username, password=password)

    def get(self, phone: str) -> None:
        data = self.client.get(phone)
        if data:
            return json.loads(data)
        return None
    
    def set(self, phone: str, data: str) -> None:
        self.client.set(phone, json.dumps(data), ex=3600)
        
        
#### Eu vou usar o Redis hospedado mesmo, então me ajuda a configurar a conexão com o Redis hospedado no meu projeto ?
# Para configurar a conexão com o Redis hospedado no seu projeto, você precisará seguir os seguintes passos:
# 1. Crie uma conta em um serviço de Redis hospedado, como o Redis Cloud ou Heroku Redis, e configure uma instância de Redis, anotando as credenciais de acesso (host, porta, senha).
# 2. No seu projeto, modifique a classe `RedisConversationRepository` no arquivo `redis_repository.py` para aceitar as credenciais de conexão do Redis hospedado:
# class RedisConversationRepository(ConversationCacheRepository):   
#     def __init__(self, host='seu_host_redis', port=6379, password='sua_senha_redis', db=0):
#         self.client = redis.Redis(host=host, port=port, password=password, db=db)
# 3. Substitua os valores padrão de `host`, `port` e `password` pelos valores fornecidos pelo serviço de Redis hospedado.
# 4. Certifique-se de que a instância do Redis hospedado esteja acessível a partir do ambiente onde seu projeto está rodando, e teste a conexão para garantir que tudo esteja configurado corretamente.


#### o db fica zerado ?
# O parâmetro `db` na configuração do Redis é usado para especificar qual banco de dados dentro do Redis você deseja usar. O Redis suporta múltiplos bancos de dados, numerados de 0 a 15 por padrão. Se você definir `db=0`, isso significa que você estará usando o banco de dados número 0, que é o banco de dados padrão. Se você quiser usar um banco de dados diferente, basta alterar o valor do `db` para o número correspondente ao banco de dados que deseja utilizar.

#### Lá no Redis o nome do meu banco é database-MLQRKK6L
# Se o nome do seu banco de dados no Redis é `database-MLQRKK6L`, isso significa que você está usando um serviço de Redis hospedado que pode ter uma configuração diferente dos bancos de dados tradicionais do Redis.
# Nesse caso, você deve verificar a documentação do serviço de Redis que está utilizando para entender como configurar a conexão corretamente, pois pode ser necessário usar um endpoint específico ou fornecer credenciais adicionais para acessar esse banco de dados específico. Certifique-se de seguir as instruções fornecidas pelo serviço de Redis para garantir que sua aplicação possa se conectar ao banco de dados `database-MLQRKK6L` corretamente.