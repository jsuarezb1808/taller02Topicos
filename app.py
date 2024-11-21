from flask import Flask 
import os
import random
import platform
from model import pokenea
from flask_restful import Resource, Api

app = Flask(__name__) 
api = Api(app)

#array de pokeneas
pokeneas=[]
#añadir datos
pokeneas.append(pokenea(71,"Maicol ","1.0","fanatico: la pokenea puede hacerse matar por un equipo de futbol","pendiente","no sea sapo pa") )
pokeneas.append(pokenea(63,"Bairon Esneider","1.70","falta de educación","pendiente","Se me baja de los tenis") )
pokeneas.append(pokenea(12,"Yaris Yusbleidy","1.75","tener calle: la pokenea no puede ser robada, la pokenea roba al ladron ","pendiente","su cucha es severa lámpara") )
pokeneas.append(pokenea(34,"Bratzedys","1.76","etilico: la pokenea no se queda cieg@ al tomar chamber","pendiente","Una cosa es una cosa y otra cosa es otra cosa") )
pokeneas.append(pokenea(64,"Kevin","1.78","navaja: vuelve cualquier objeto en una navaja","pendiente","El que le tenga miedo a morir que no nazca") )
pokeneas.append(pokenea(74,"sneider","1.72","duplicar: la pokenea se duplica si entra en contacto con otro pokenea de genero opuesto, tarda 9 turnos","pendiente","Sin riesgo no hay ganancia") )
pokeneas.append(pokenea(79,"Douglas","1.60","ojo de aguila: le permite identificar cualquier objeto en un bolsillo ","pendiente","Sin mente como el demente") )
pokeneas.append(pokenea(34,"jenderson","1.73","guaracha:la pokenea puede prender un bafle a las 3AM sin consecuencia aparente","pendiente","El que se asusta, se quema") )
pokeneas.append(pokenea(65,"briyid ","1.70","","pendiente","pa q zapatos si no hay ksa") )
pokeneas.append(pokenea(40,"Venegas","1.75","motero:puede acelerar la moto sin romperse la jeta permanentemente","pendiente","esta gñorrea") )


class frases(Resource):
    def get(self):
        nea = random.choice(pokeneas)
        container_id = platform.node() 
        data={
            "imagen":nea.imagen,
            "frase":nea.frase,
            "container_id":container_id
        }
        return data

class neas(Resource):
    def get(self):
        nea = random.choice(pokeneas)
        container_id = platform.node() 
        data = {
            "id": nea.id,
            "nombre": nea.nombre,
            "altura": nea.altura,
            "habilidad": nea.habilidad,
            "container_id": container_id
        }
        return data

api.add_resource(frases, '/frases')
api.add_resource(neas, '/neas')

if __name__ == '__main__':
    app.run(debug=True)