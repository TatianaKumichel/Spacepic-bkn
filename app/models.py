from app.database import get_db

class Usuario:
    def __init__(self,id=None, nombre=None, email=None):
        self.id= id
        self.nombre = nombre
        self.email = email
        
     
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios")#consulta mysql
        rows = cursor.fetchall()#trae todos los resultados de la consulta
        usuarios = [Usuario(id=row[0], nombre=row[1], email=row[2]) for row in rows] #crea una lista usuarios donde cada elemento es un objeto de la clase Usuario
        cursor.close()
        return usuarios
        
    def save(self):
        ##logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id_usuario:
            query = """ UPDATE usuario SET nombre = %s, email = %s WHERE id_usuario = %s
            """, (self.nombre, self.email)
            cursor.execute(query)
            #query = ... es lo mismo que :
            #cursor.execute(""" UPDATE usuario SET nombre = %s, email = %s WHERE id_usuario = %i
            #""", (self.nombre, self.email))
        else:
            cursor.execute("""INSERT INTO usuario (nombre, email) VALUES (%s, %s) """, (self.nombre, self.email))
            self.id_usuario = cursor.lastrowid
            db.commit()
            cursor.close()
        pass   
    
    def delete(self):
        #logica para hacer un DELETE en la BASE
        pass 
    
    #metodo para ordenar la representacion de la clase
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email
            
        
        }
    