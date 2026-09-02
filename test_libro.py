from src.libro import registrar_libro

def test_registrar_libro_datos_completos():
    libro = registrar_libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
    assert libro is not False
    assert libro.titulo == "Cien Años de Soledad"

def test_registrar_libro_sin_datos():
    resultado = registrar_libro("", "Autor", "1234567890")
    assert resultado == False
