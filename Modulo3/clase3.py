text = """
Python es uno de los lenguajes de programación dinámicos más populares
que existen entre los que se encuentran Java, Javascript, Go y C#.
Aunque es considerado a menudo como un lenguaje "scripting",
es realmente un lenguaje de propósito general. En la actualidad,
Python es usado para todo, desde simples "scripts",
hasta grandes servidores web que proveen servicio ininterrumpido 24×7.
Es utilizado para la programación de interfaces gráficas y bases de datos,
programación web tanto en el cliente como en el servidor (véase Django o
Flask) y
testing de aplicaciones. Además tiene una amplia aceptación por científicos que
hacen aplicaciones para las supercomputadores más rápidas del
mundo y por los niños que recién están comenzando a programar."""


word_search = input("Introduce la palabra que quiere buscar: ")
index = text.find(word_search)
total_word = text.count(word_search)

if index != -1:
    print(f"La palabra que busca se encuentra en el {index}")
    print(f"esta palabra se repite {total_word}")
else:
    print("La palabra que busca no se encontro :c")
