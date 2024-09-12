from modelo.curso import curso

class CursoServicio:
    @staticmenthod
    def crear_curso(nombre,descrpcion,fecha_inicio,fecha_inicio_fin,horas):
        curso=curso.create(nombre=nombre,descripcion=descripcion , fecha_inicio_fin=fecha_inicio_fin,horas=horas)
        return curso
    
    @stationmethod
    def mostrar_cursos():
        return list(curso.select())
    
    

