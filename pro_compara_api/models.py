from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre    

    class Meta:
        verbose_name_plural = "1. Paises"
        ordering = ['id']


class Universidad(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "2. Universidades"

    def __str__(self):
        return self.nombre


class Institucion(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "3. Institucion"

    def __str__(self):
        return self.nombre        


class PlanEstudio(models.Model):
    nombre = models.CharField(max_length=120)
    fecha_vigencia = models.IntegerField()
    universidad = models.ForeignKey(Universidad, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "4. Planes"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.id, self.nombre)


class Guia(models.Model):
    nombre = models.CharField(max_length=10)
    fecha_vigencia = models.IntegerField()
    institucion = models.ForeignKey(Institucion, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "5. Guias"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.id, self.nombre)


class NodoModCurso(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    longname = models.CharField(max_length=200, default='')
    guia = models.ForeignKey(Guia, blank=True, null=True, on_delete=models.CASCADE)    
    class Meta:
        verbose_name_plural = "6.1  Nodos Guias"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)    

class EnlaceModCurso(models.Model):
    origen = models.IntegerField()
    destino = models.IntegerField()
    guia = models.ForeignKey(Guia, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "6.2  Enlaces Guias"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.origen, self.destino)  

class NodoCurso(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    longname = models.CharField(max_length=200, default='')
    plan = models.ForeignKey(PlanEstudio, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "7.1  Nodos Planes"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)    

class EnlaceCurso(models.Model):
    origen = models.IntegerField()
    destino = models.IntegerField()
    plan = models.ForeignKey(PlanEstudio, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "7.2  Enlaces Planes"
        ordering = ['id']

    def __str__(self):
        return '{}-{}'.format(self.origen, self.destino) 

    