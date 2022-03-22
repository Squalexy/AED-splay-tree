from time import perf_counter
import sys

sys.setrecursionlimit(10 ** 6)


class Node:

    def __init__(self, nome, morada, volume_compras):
        self.nome = nome
        self.morada = morada
        self.volume_compras = volume_compras
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:

    def __init__(self):
        self.root = None

    def search(self, node, nome, value):

        if node is None:
            # print("CLIENTE NAO REGISTADO")
            return node

        if nome == node.nome:
            node.volume_compras += value
            if value != 0:  # aquisicao
                pass
                # print("AQUISICAO INSERIDA")
            else:  # consulta
                # print(f"{node.nome} {node.morada} {node.volume_compras}\nFIM")
                self.splaying(node)

            return node

        if nome < node.nome:
            return self.search(node.left, nome, value)
        return self.search(node.right, nome, value)

    def left_rotation(self, parent_node):
        node_to_splay = parent_node.right
        parent_node.right = node_to_splay.left
        if node_to_splay.left is not None:
            node_to_splay.left.parent = parent_node

        node_to_splay.parent = parent_node.parent
        if parent_node.parent is None:
            self.root = node_to_splay
        elif parent_node == parent_node.parent.left:
            parent_node.parent.left = node_to_splay
        else:
            parent_node.parent.right = node_to_splay
        node_to_splay.left = parent_node
        parent_node.parent = node_to_splay

    def right_rotation(self, parent_node):
        node_to_splay = parent_node.left
        parent_node.left = node_to_splay.right
        if node_to_splay.right is not None:
            node_to_splay.right.parent = parent_node

        node_to_splay.parent = parent_node.parent
        if parent_node.parent is None:
            self.root = node_to_splay
        elif parent_node == parent_node.parent.right:
            parent_node.parent.right = node_to_splay
        else:
            parent_node.parent.left = node_to_splay

        node_to_splay.right = parent_node
        parent_node.parent = node_to_splay

    def splaying(self, node):
        while node.parent is not None:

            # ZIG ROTATION
            if node.parent.parent is None:
                if node == node.parent.left:
                    self.right_rotation(node.parent)
                else:
                    self.left_rotation(node.parent)

            # ZIG-ZIG ROTATION
            elif node == node.parent.left and node.parent == node.parent.parent.left:  # RIGHT RIGHT
                self.right_rotation(node.parent.parent)
                self.right_rotation(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.right:  # LEFT LEFT
                self.left_rotation(node.parent.parent)
                self.left_rotation(node.parent)

            # ZIG-ZAG ROTATION
            elif node == node.parent.right and node.parent == node.parent.parent.left:  # LEFT RIGHT
                self.left_rotation(node.parent)
                self.right_rotation(node.parent)
            else:  # RIGHT LEFT
                self.right_rotation(node.parent)
                self.left_rotation(node.parent)

    def listagem(self, node):
        if node is not None:
            self.listagem(node.left)
            print(f"{node.nome} {node.morada} {node.volume_compras}")
            self.listagem(node.right)

    def insert(self, nome, morada, volume_compras):
        node = Node(nome, morada, volume_compras)
        parent = None
        raiz = self.root

        # ------ percorrer a árvore recursivamente, consoante o nome do input e guardar como pai a raíz ------ #

        while raiz is not None:  # enquanto os nós estiverem todos ocupados, até encontrar um vazio
            parent = raiz  # recursivamente, a raíz é o pai para o atribuírmos ao node
            if node.nome < raiz.nome:
                raiz = raiz.left
            else:
                raiz = raiz.right

        # ------ inserção do nó ------ #

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.nome < parent.nome:
            parent.left = node
        elif node.nome > parent.nome:
            parent.right = node
        elif node.nome == parent.nome:
            # print("CLIENTE JA EXISTENTE")
            return

        # print("NOVO CLIENTE INSERIDO")
        self.splaying(node)

    def apaga(self, node):
        if node is not None:
            self.apaga(node.left)
            self.apaga(node.right)
            node.left = None
            node.right = None


if __name__ == '__main__':

    tree = SplayTree()

    total_time = 0

    while True:

        inputs = [i for i in input().split()]

        if inputs[0].lower() == "cliente":
            rua = inputs[2] + " " + inputs[3]
            tree.insert(inputs[1], rua, int(inputs[4]))

        elif inputs[0].lower() == "aquisicao":
            tree.search(tree.root, inputs[1], int(inputs[2]))

        elif inputs[0].lower() == "consulta":
            tik = perf_counter()
            tree.search(tree.root, inputs[1], 0)
            tok = perf_counter()
            total_time += tok - tik

        elif inputs[0].lower() == "listagem":
            tree.listagem(tree.root)
            print("FIM")

        elif inputs[0].lower() == "apaga":
            tree.apaga(tree.root)
            tree.root = None
            print("LISTAGEM DE CLIENTES APAGADA")

        elif inputs[0].lower() == "fim":
            print(total_time)
            break
