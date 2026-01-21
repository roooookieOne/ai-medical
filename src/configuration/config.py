from pathlib import Path

# 目录路径
ROOT_DIR = Path(__file__).parent.parent.parent

CHECKPOINT_DIR = ROOT_DIR / "checkpoints"
DATA_DIR = ROOT_DIR / "data"

# web静态目录
WEB_STATIC_DIR = ROOT_DIR / "src" / "web" / "templates"

# 数据库连接
MYSQL_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    'database': 'edu',
}

NEO4J_CONFIG = {
    'uri': "neo4j://localhost:7687",
    'auth': ("neo4j", "12345678")
}

BASE_URL = "https://api.openai-proxy.org/v1"
API_KEY = "sk-PQDj52PeFhQ4dg7TaHg4w2uY0Y9oSWrb8YgobkXzGXgf5dYg"