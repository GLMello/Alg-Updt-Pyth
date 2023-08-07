<h1>Algoritmo para atualizar arquivos de texto de acesso através do Python</h1>

### You can also read this in: [English](https://github.com/GLMello/Pyth-Updt-Alg)

<h2>Descrição</h2>
Desenvolvendo um algoritmo responsável por atualizar um arquivo contendo IPs autorizados em uma rede, verificando seu acesso e removendo endereços banidos deste arquivo. <br> <br />

**Observação:** Para melhor visualizar o código, foram utilizados IPs fictícios e um arquivo de exemplo. Mais tarde, no desenvolvimento, os IPs apresentados são substituídos por um arquivo para permitir escalabilidade. <br>
<h2>Passo a passo</h2>
Comecei desenvolvendo um código curto que abriu o arquivo original e exibiu seu conteúdo, também realizei inserção de uma lista de IPs banidos fictícios:
<br/>

```python
# Atribuindo variável ao nome do arquivo.

import_file = "allow_list.txt"

# Lista de endereços IP que não têm mais permissão para acessar informações restritas.

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:

  # Lê e armazena o conteúdo do arquivo importado em uma variável como uma string.

  ip_addresses=file.read()

print(ip_addresses)
```
<br/>
Em seguida, adicionei as seguintes linhas para converter o conteúdo em uma lista, iterar pela 'lista de remoção' e remover os endereços IP correspondentes do conteúdo:  
<br/>

```python
# Converte o conteúdo de uma string para uma lista.

ip_addresses = ip_addresses.split()

# Percorre a `lista de remoção`, procura por correspondências e as remove da lista.

for element in remove_list:
    if element in ip_addresses: 
        ip_addresses.remove(element)
```
<br />
Convertendo a lista de volta para uma string e atualizando, podemos atualizar o arquivo original:
<br />

```python
# Converte a lista de volta para uma string.

ip_addresses = "\n".join(ip_addresses)

# Reescreve o arquivo, substituindo seu conteúdo por `ip_addresses`.

with open(import_file, "w") as file:
  file.write(ip_addresses)
```
<br />
Para finalizar, transformei o código em uma função que recebe dois arquivos como parâmetros, um contendo uma lista de IPs autorizados e outro contendo endereços IP banidos. Terminando com o algoritmo completo:
<br/>

```python
def update_file(import_file, remove_file):

# Atribui variáveis para receber o conteúdo dos arquivos.

    with open(import_file, "r") as allow_file:
        ip_addresses = allow_file.read()
    
    with open(remove_file, "r") as remove_list: 
        remove_list = remove_file.read()

# Converte o conteúdo de uma string para uma lista.

    remove_list = remove_list.split()

    ip_addresses = ip_addresses.split()

# Percorre a `lista de remoção`, procura por correspondências e as remove da lista.

    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)

# Converte a lista de volta para uma string.

    ip_addresses = "\n".join(ip_addresses)

# Reescreve o arquivo, substituindo seu conteúdo pelo da lista.

    with open(import_file, "w") as allow_file:
        allow_file.write(ip_addresses)
```
