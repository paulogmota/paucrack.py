# pcrack.py
Crack simples de senhas salt:hash usando wordlist

Uso: 
1. Escolha a wordlist contendo as senhas
2. Copie o salt + hash da senha desejada

$ cat /etc/shadow
test:$y$j9T$FOlH17SkYipEtrmPpW6uH.$UXvqsQ1AXiLMq7KgNcB6Vn8AeX/mzrC11boonUqQyx7:19743:0:99999:7:::

$python3 paucrack.py senhas.txt

Digite o salt: $y$j9T$FOlH17SkYipEtrmPpW6uH.$

Digite o hash: $y$j9T$FOlH17SkYipEtrmPpW6uH.$UXvqsQ1AXiLMq7KgNcB6Vn8AeX/mzrC11boonUqQyx7

Senha:  79994455
