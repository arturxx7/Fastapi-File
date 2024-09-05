import csv
import os
from fastapi import HTTPException, status


class FileProcessor:
        #Manager of files and folders processor.

    def __init__(self):
        self.file_path = 'data/seu_file.csv'
        self.directory = 'data'

    def create_file(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', newline='') as file:
                writer= csv.writer(file)
                writer.writerow(['conta','agencia', 'texto','valor'])
                return{"mensagem": f"Arquivo{self.file_path} criado com sucesso."}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Arquivo já existe")
