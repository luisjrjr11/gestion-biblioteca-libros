class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

def registrar_libro(titulo, autor, isbn):
    if not titulo or not autor or not isbn:
        return False
    return Libro(titulo, autor, isbn)
