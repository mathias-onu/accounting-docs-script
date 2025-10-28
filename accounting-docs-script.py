import os
import shutil

DOWNLOADS_DIR_PATH = os.environ['DOWNLOADS_DIR_PATH']
ACCOUNTING_DIR_PATH = os.environ['ACCOUNTING_DIR_PATH']

for file_name in os.listdir(DOWNLOADS_DIR_PATH):
    # 1. Identifies client invoices
    if 'e-Factura_client' in file_name:
        # 2. Get the invoice month
        invoice_date = file_name.split('__')[1].split('-')
        invoice_path = f'{DOWNLOADS_DIR_PATH}/{file_name}'
        invoice_month_directory_exists = False

        # 3. Checks if invoice target directory exists
        for month_directory in os.listdir(ACCOUNTING_DIR_PATH):
            if f'{invoice_date[2]}-{invoice_date[1]}' in month_directory:
                invoice_month_directory_exists = True
        
        if invoice_month_directory_exists == False:
            os.makedirs(f'{ACCOUNTING_DIR_PATH}/{invoice_date[2]}-{invoice_date[1]}')

        # 4. Moves the file
        shutil.move(f'{DOWNLOADS_DIR_PATH}/{file_name}', f'{ACCOUNTING_DIR_PATH}/{invoice_date[2]}-{invoice_date[1]}')
    