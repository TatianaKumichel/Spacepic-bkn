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
        usuarios = [Usuario(id=row[0], nombre=row[1], email=row[2]) for row in rows]
        cursor.close()
        return usuarios
        
    def save(self):
        ##logica para INSERT/UPDATE en base datos
        pass   
    
    def delete(self):
        #logica para hacer un DELETE en la BASE
        pass 
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email
            
        
        }
    