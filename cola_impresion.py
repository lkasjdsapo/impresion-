from collections import deque


class Cola:

    def __init__(self):
        self.documentos = deque()

    def agregar(self, documento):
        self.documentos.append(documento)

    def sacar(self):
        if len(self.documentos) > 0:
            return self.documentos.popleft()

        return None

    def vacia(self):
        return len(self.documentos) == 0

    def cantidad(self):
        return len(self.documentos)
