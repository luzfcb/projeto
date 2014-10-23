import sys


def verifica_igual(a, b):
    return True if a == b else False

def soma(a, b)
    return a + b

def subtracao(a, b)
    return a - b

def faz_algo(faz=False, p=False):
    """
    >>> faz_algo(faz=True)
    """
    valor = 0
    if faz:
        if p:
            print("estou em P")
            return True
        print("Estou em Faz")
        valor = 1
    print("passou no final")
    return valor
 
 
# if __name__ == "__main__": # pragma: no cover
#     if len(sys.argv) > 1:
#         faz_algo(faz=True, p=True)
#     elif len(sys.argv) > 1:
#         faz_algo(faz=True)
#     else:
#         faz_algo(faz=False)
# 
#     print(verifica_igual(2, 2))
#     print(verifica_igual(2, 3))    
     
 
