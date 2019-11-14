import os

DEBUG = True
DATABASE = {
    'user': os.getenv('POSTGRES_USER', 'test'),
    'password': os.getenv('POSTGRES_PASSWORD', 'test'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': int(os.getenv('POSTGRES_PORT', 5432)),
    'database': os.getenv('POSTGRES_DB', 'test')
}

DB_POOL_SIZE_MIN = int(os.getenv("DB_POOL_SIZE_MIN", 1))
DB_POOL_SIZE_MAX = int(os.getenv("DB_POOL_SIZE_MAX", 6))

DASHBOARD_PORT = int(os.getenv('DASHBOARD_PORT', 5000))
DASHBOARD_WORKERS = int(os.getenv('DASHBOARD_WORKERS', 1))
DASHBOARD_ACCESS_LOG = os.getenv('DASHBOARD_ACCESS_LOG', False)