import re


cadena = "Esta es la clase numero 5 del modulo 3 repasando el import re"

# busqueda en base a un patron

texto = """
La fecha de vencimiento es 2023-12-31 y la
fecha de inicio fue 2023-01-15 y se renovo el 2024-01-02"""
pantron_de_fecha = r"\d{4}-\d{2}-\d{2}"
fechas_encontradas = re.findall(pantron_de_fecha, texto)
print(fechas_encontradas)

# remplazo de texto con patrones

texto2 = "El numero del telefono es 231-345-5678"
pantron_de_numero = r'\d{3}-\d{3}-\d{4}'
remplazo = re.sub(pantron_de_numero, "#####", texto2)
print(remplazo)

# Capturar link

html = '<p>Enlace uno <a href="http://www.google.com">Enlace 1</a>'
patron_url = r'<a href="(.*?)">"(.*?)"</a>'
enlaces = re.findall(patron_url, html)
for enlace in enlaces:
    url, texto = enlace
    print(f"URL : {url}, texto : {texto}")
