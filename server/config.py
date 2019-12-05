import os

DEBUG = os.getenv("DEBUG", True)

DATABASE = {
    'user': os.getenv('POSTGRES_USER', 'test'),
    'password': os.getenv('POSTGRES_PASSWORD', 'test'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': int(os.getenv('POSTGRES_PORT', 5432)),
    'database': os.getenv('POSTGRES_DB', 'test'),
    'pool_size_min': int(os.getenv("DB_POOL_SIZE_MIN", 1)),
    'pool_size_max': int(os.getenv("DB_POOL_SIZE_MAX", 3))
}

DASHBOARD = {'host': os.getenv('DASHBOARD_API_HOST', 'localhost'),
             'port': int(os.getenv('DASHBOARD_API_PORT', 5050)),
             'workers': int(os.getenv('DASHBOARD_WORKERS', 1)),
             'access_log': os.getenv('DASHBOARD_ACCESS_LOG', False)}

SSO = {'host': os.getenv('SSO_API_HOST'),
       'port': int(os.getenv('SSO_API_PORT', 8080))}

PARSER = {'host': os.getenv('PARSER_API_HOST'),
          'port': int(os.getenv('PARSER_API_PORT', 8000))}

AGGREGATOR = {'host': os.getenv('AGGREGATOR_API_HOST'),
              'port': int(os.getenv('AGGREGATOR_API_PORT', 3000))}