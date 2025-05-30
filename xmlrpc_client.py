import xmlrpc.client
from . import config

url = config.ODOO_URL
db = config.ODOO_DB
username = config.ODOO_USER
password = config.ODOO_PASSWORD

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
