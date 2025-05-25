def valida_extensao(nome_arquivo: str, extensoes_validas: list[str]):
    return any(nome_arquivo.endswith(ext) for ext in extensoes_validas)
