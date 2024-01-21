import warnings
#Tirar o warning da lib crypt
warnings.filterwarnings("ignore", category=DeprecationWarning)
import crypt
import sys


if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "wordlist")
    sys.exit(1)

salt = input("Digite o salt: ")
haxx = input("Digite o hash: ")
wordlist = sys.argv[1]

with open(wordlist) as file:
    for line in file:
        line = line.strip()
        hashlinha = crypt.crypt(line,salt)
        if hashlinha == haxx:
            print("Senha: ", line)
            exit()

print("Senha não encontrada na wordlist.")
