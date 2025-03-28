import os
import time
from getpass import getuser

# Obtém o nome do usuário do sistema
usuario = getuser()
start_time = time.time()

# Nome do código
nome_codigo = "Nuker Tool by 1nstagram"  

def mudar_nome_aba():
    tempo_uso = int(time.time() - start_time)  # Tempo em segundos
    novo_nome = f"{nome_codigo} | User: {usuario} | Time: {tempo_uso}s"
    os.system(f'echo -ne "\\033]0;{novo_nome}\\007"')

if __name__ == "__main__":
    mudar_nome_aba()
