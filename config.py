import os
from dotenv import load_dotenv
from pathlib import Path

# Muat file .env

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# Konfigurasi Odoo XML-RPC
ODOO_URL = os.getenv("ODOO_URL")
ODOO_DB = os.getenv("ODOO_DB")
ODOO_USER = os.getenv("ODOO_USER")
ODOO_PASSWORD = os.getenv("ODOO_PASSWORD")

# Token API
Secret = os.getenv("Secret")
