# Ransomware Educativo em Python 🔵

Este repositório contém dois scripts Python, `encrypter.py` e `decrypter.py`, que demonstram como funciona um ransomware básico, implementado de forma educativa.

## **Melhorias Implementadas**

### 1. Substituição do `pyaes` por `cryptography`

- A biblioteca `cryptography` é mais robusta e amplamente suportada.
- Utiliza AES no modo CTR (Counter) para criptografia e descriptografia.

### 2. Obfuscação da chave de criptografia

- A chave é codificada e decodificada com `base64`, dificultando a identificação direta no código.

### 3. Suporte à escolha de formatos de arquivo (encrypter.py)

- O script de criptografia permite selecionar arquivos com extensões específicas para processar.

### 4. Processamento automático de arquivos (decrypter.py)

- O script de descriptografia identifica automaticamente arquivos com a extensão `.ransomwaretroll`.
- Nenhuma interação do usuário é necessária para especificar os arquivos a descriptografar.

### 5. Logs informativos

- Ambos os scripts usam a biblioteca `logging` para informar o progresso e registrar erros.

## **Passo-a-Passo para Utilizar**

### **Requisitos**

- Python 3.6 ou superior.
- Biblioteca `cryptography` (já incluída em distribuições modernas, mas pode ser instalada com `pip install cryptography`).

### **Encrypter (Criptografando Arquivos)**

1. Coloque os arquivos que deseja criptografar na mesma pasta do script `encrypter.py`.

2. Execute o script:

   ```bash
   python3 encrypter.py
   ```

3. Insira a extensão do arquivo que deseja criptografar (por exemplo, `.txt`).

![Demonstração Encrypter](https://github.com/daferreira23/cibersecurity-desafio-ransomware-aprimorado/blob/master/Ransomware.png?raw=true)

4. O script irá:

   - Ler os arquivos especificados.
   - Criptografar seus conteúdos.
   - Salvar os arquivos com a extensão adicional `.ransomwaretroll`.
   - Excluir os arquivos originais.

### **Decrypter (Descriptografando Arquivos)**

1. Certifique-se de que os arquivos `.ransomwaretroll` estejam na mesma pasta do script `decrypter.py`.

2. Execute o script:

   ```bash
   python3 decrypter.py
   ```

3. O script irá automaticamente:

   - Identificar os arquivos `.ransomwaretroll`.
   - Descriptografar seus conteúdos.
   - Restaurar os nomes originais dos arquivos.
   - Excluir os arquivos criptografados.

## 🚨 Aviso Importante

**Este projeto foi criado exclusivamente para fins educacionais.**

- Seu uso em atividades maliciosas é estritamente proibido e pode resultar em penalidades legais severas.
- Teste esses scripts apenas em ambientes controlados e **nunca em sistemas ou arquivos reais sem autorização.**

## 🔴 Dica: Use em uma Máquina Virtual

- Para evitar riscos ao sistema principal, execute esses scripts em uma máquina virtual (como VirtualBox ou VMware).
- Use uma distribuição Linux (como Kali Linux) para facilitar os testes.
- Certifique-se de isolar o ambiente da rede principal.

---
