import rpyc
from constRPYC import * 

class Client:
    conn = rpyc.connect(SERVER, PORT)

    print("Valor inicial:", conn.root.exposed_value())

    conn.root.exposed_append(5)
    conn.root.exposed_append(10)
    conn.root.exposed_append(5)
    conn.root.exposed_append(20)
    conn.root.exposed_append(5)
    conn.root.exposed_append("abc")  # valor não numérico

    print("Após append:", conn.root.exposed_value())

    print("Tamanho:", conn.root.exposed_length())
    print("Média:", conn.root.exposed_average())
    print("Moda:", conn.root.exposed_mode())
    print("Valores únicos:", conn.root.exposed_unique())

    conn.root.exposed_sort()
    print("Ordenado:", conn.root.exposed_value())

    conn.root.exposed_remove(10)
    print("Após remover 10:", conn.root.exposed_value())

    conn.root.exposed_clear()
    print("Após limpar:", conn.root.exposed_value())
