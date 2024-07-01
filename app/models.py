from app.database import get_db

class Usuario:
    def __init__(self,id=None, nombre=None, email=None):
        self.id = id
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

    @staticmethod
    def get_by_id(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id= %s", (id,))#consulta mysql
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id=row[0], nombre=row[1], email=row[2])
        return None
        
    def save(self):
        ##logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id:
            query = """ UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s"""
            params = (self.nombre, self.email, self.id)
            cursor.execute(query, params)
        else:
            query = """INSERT INTO usuarios (nombre, email) VALUES (%s, %s) """
            params = (self.nombre, self.email)
            cursor.execute(query, params)
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()
    
    def delete(self):
        #logica para hacer un DELETE en la BASE
        db = get_db()
        cursor = db.cursor()
        query = f" DELETE FROM usuarios WHERE id = {self.id}"
        cursor.execute(query)
        db.commit()
        cursor.close()

    #metodo para ordenar la representacion de la clase
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email
        }
    
class Picture:
    def __init__(self, id, name ,url ):
        self.id = id
        self.name = name
        self.url = url
        
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pictures")#consulta mysql
        rows = cursor.fetchall()#trae todos los resultados de la consulta
        pictures = [Picture(id=row[0], name=row[1], url=row[2]) for row in rows]
        cursor.close()
        return pictures
               
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }