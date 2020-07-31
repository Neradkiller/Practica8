from django.db import models

# Create your models here.

class BaseEntity(models.Model):
    OPTIONS = [('Enabled','enabled'),
               ('Dissabled','Disabled')]
    status = models.CharField(choices = OPTIONS, max_length = 9)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_eliminacion = models.DateTimeField(blank = True, null = True)

    class Meta:
        abstract = True

class Entity(BaseEntity):
    name = models.CharField(max_length = 50)
    description = models.TextField()

    class Meta:
        abstract = True


class Person(BaseEntity):
    dni = models.CharField(max_length = 30)
    firt_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.firt_name

class Faculty(Entity):
    pass

class School(Entity):
    facultad = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Section(Entity):
    OPTIONS2 = [('Mandatory','Mandatory'),
                ('Elective','Elective')]
    uc = models.IntegerField()
    semester = models.IntegerField()
    tipo = models.CharField(choices = OPTIONS2, max_length = 9)
    ht = models.DecimalField(max_digits=4, decimal_places = 2)
    hp = models.DecimalField(max_digits=4, decimal_places = 2)
    hl = models.DecimalField(max_digits=4, decimal_places = 2)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Enrollment(BaseEntity):
    OPTIONS2 = [('Student','Student'),
                ('Teacher','Teacher')]
    tipo = models.CharField(choices = OPTIONS2, max_length = 9)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)