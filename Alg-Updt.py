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