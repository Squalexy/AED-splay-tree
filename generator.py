import random as rd


def generator90(n_fich, n_clientes):
    n = 1000
    for i in range(n_fich):
        filename = 'input' + str(i).zfill(3) + ".txt"
        with open(filename, 'w') as file:
            for j in range(n_clientes):
                cliente = 'cliente' + str(j)
                file.write("CLIENTE " + cliente + " rua douro 10000\n")
            for j in range(n):
                for k in range(9):
                    ncli = rd.randint(0, int(n_clientes * 0.05) - 1)
                    cliente = 'cliente' + str(ncli)
                    file.write("CONSULTA " + cliente + "\n")
                ncli = rd.randint(int(n_clientes * 0.05), n_clientes - 1)
                cliente = 'cliente' + str(ncli)
                file.write("CONSULTA " + cliente + "\n")
            file.write("FIM")
        n += 1000


def generator50(n_fich, n_clientes):
    n = 10000
    for i in range(n_fich):
        clientes = []
        filename = 'igual' + str(i).zfill(3) + ".txt"
        with open(filename, 'w') as file:
            for j in range(n_clientes):
                cliente = 'cliente' + str(j)
                file.write("CLIENTE " + cliente + " rua douro 10000\n")
            for j in range(n):
                ncli = rd.randint(0, n_clientes - 1)
                cliente = 'cliente' + str(ncli)
                file.write("CONSULTA " + cliente + "\n")
            file.write("FIM")
        n += 10000


if __name__ == "__main__":
    # generator90(20, 10000)
    generator50(20, 10000)
