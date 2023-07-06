# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Jonathan" # escribe tu nombre
    age = "17" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
@app.route("/Papa")
def home2():

    name = "Casimiro" # escribe tu nombre
    age = "50" # escribe tu edad

    return render_template('father.html' , name = name , age = age)


# define la ruta a la página web de tu madre.
@app.route("/Mama")
def home3():

    name = "Sonia" # escribe tu nombre
    age = "45" # escribe tu edad

    return render_template('mother.html' , name = name , age = age)

# define la ruta a la página web de tus amigos.
@app.route("/Amigo")
def home4():

    name = "__" # escribe tu nombre
    age = "__" # escribe tu edad

    return render_template('friend.html' , name = name , age = age)





# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
