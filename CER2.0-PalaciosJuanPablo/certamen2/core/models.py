from django.db import models

# Create your models here.
#El tipo de temas que puede ser el proyecto
tipo_temas = [
    ("0", "tipo A"),
    ("1", "tipo B"),
    ("2", "tipo C"),
    ("3", "tipo D"),
]

tipo_user = [
    ("A", "Estudiante"),
    ("B", "Profesorado")

]

class Proyecto(models.Model):
    proyecto_name = models.CharField(max_length=80, primary_key=True, verbose_name="NOMBRE PROYECTO")    #Nombre del Proyecto
    proyecto_student = models.CharField(max_length=80, verbose_name= "Estudiante")                      #Nombre del estudiante
    proyecto_topic = models.CharField(max_length=20,choices= tipo_temas, verbose_name= "TEMA")          #El topico del proyecto
    proyecto_patrocinador= models.CharField(max_length=80, verbose_name= "PROFESOR")                    #Nombre del Profesor

    def __str__(self) -> str:
        return self.proyecto_name
    
class Profesor(models.Model):
    email = models.EmailField()
    user= models.CharField(max_length=80, verbose_name="Nombre Profesorado")
    
    
class Estudiante (models.Model):
    email= models.EmailField()
    user= models.CharField(max_length=80, verbose_name="Nombre Estudiante")

#class InicioSesion(models.Model):
