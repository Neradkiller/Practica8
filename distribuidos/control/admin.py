from django.contrib import admin

# Register your models here.
from .models import Person
from .models import Faculty
from .models import School
from .models import Section
from .models import Enrollment


admin.site.register(Person)
admin.site.register(Faculty)
admin.site.register(School)
admin.site.register(Section)
admin.site.register(Enrollment)