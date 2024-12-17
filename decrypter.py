import os
import logging
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def descriptografar_arquivo(file_path, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Descriptografar os dados
        cipher = Cipher(algorithms.AES(key), modes.CTR(b"0" * 16), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypt_data = decryptor.update(file_data) + decryptor.finalize()

        # Restaurar o nome original do arquivo
        original_file_path = file_path.replace(".ransomwaretroll", "")
        with open(original_file_path, "wb") as new_file:
            new_file.write(decrypt_data)

        # Remover o arquivo criptografado
        os.remove(file_path)
        logging.info(f"Arquivo descriptografado: {file_path} -> {original_file_path}")
    except Exception as e:
        logging.error(f"Erro ao descriptografar {file_path}: {e}")

# Obfuscar a chave de descriptografia usando base64
raw_key = "testeransomwares"
key = base64.b64decode(base64.b64encode(raw_key.encode()))

# Garantir que a chave tenha 16 bytes (128 bits para AES)
if len(key) != 16:
    key = key[:16] if len(key) > 16 else key.ljust(16, b"0")

# Processar todos os arquivos .ransomwaretroll no diretório
for file_name in os.listdir():
    if file_name.endswith(".ransomwaretroll"):
        descriptografar_arquivo(file_name, key)

logging.info("Processo de descriptografia concluído!")
