import os
from pathlib import Path


DB_NAME = 'simplebit.db'
SQL_DIR = f"{(Path(__file__) / '..' / '..' / 'sql').resolve()}"
CMC_API_KEY = os.environ.get('CMC_API_KEY', 'super-secret-key')
ROOT_URL = os.environ.get('ROOT_URL', 'ROOT_URL')
