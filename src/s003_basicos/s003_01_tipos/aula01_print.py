"""
DocString - Não é um comentário, o Python lê isso,
mas muitos utilizam como comentário
"""

''' Usar para escrever notas (o Python também lê essa linha)'''

# Exibe uma informação na saída padrão
print("Olá Mundo")                      # Imprimindo string
print(123)                              # Imprimindo números
print("Olá", "Mundo", "Separado")       # Imprimindo strings interpoladas e separadas por espaço

# Imprimindo strings interpoladas e separadas pelo separador informado
print("Olá", "Mundo", "Separado", sep="-")

# Quebras de linha
print("Olá", "Mundo", "Separado", "com", "quebra", "de", "linha", "linha 01", end="\n")
print("Olá", "Mundo", "Separado", "com", "quebra", "de", "linha", "linha 02", end="\n")