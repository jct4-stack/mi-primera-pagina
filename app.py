from flask import Flask 

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
     <html>
     <head>
         <title>Mi primera web</title>
         </head>
         <body>
             <h1>hola, mundo</h1>
             <p>Estoy creando mi primera pagina web.</p>
             </body>
             </html>
             """

app.run(debug=True)
