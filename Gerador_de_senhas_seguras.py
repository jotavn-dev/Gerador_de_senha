import secrets
import string

def gerar_senha(comprimento=12):
    """
    Gera uma senha aleatória segura combinando letras, números e pontuação.
    :param comprimento: Int, define o tamanho da senha.
    :return: String, a senha gerada.
    """
    letras = string.ascii_letters
    numeros = string.digits
    pontuacao = string.punctuation
    caracteres = letras + numeros + pontuacao
    senha = "".join(secrets.choice(caracteres) for contador in range(comprimento))
    return senha


while True:
    try:
        comprimento_senha = int(input("Qual o comprimento da senha você deseja: "))
    except ValueError:
        print("Por favor, digite apenas números.")
    else:
        break

print(f"Sua senha com {comprimento_senha} digitos: {gerar_senha(comprimento_senha)}")
