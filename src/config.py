from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'html'

file_contact_html = DATA_DIR / 'contact.html'
file_transaction_csv = DATA_DIR / 'transactions.csv'
file_transaction_json = DATA_DIR / 'transactions.json'
file_json_product = DATA_DIR / 'products.json'
