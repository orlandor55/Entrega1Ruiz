from email.policy import default
from ckeditor.fields import RichTextField
from django.db import models
import datetime

# Create your models here.

class Hobbies(models.Model):
    hobbies = models.CharField('Hobbies del familiar', max_length=50)

    class Meta:
        """Meta definition for Hobbies."""

        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.hobbies


class Familiar(models.Model):

    RELATIVE = (
        ('padre', 'Padre'),
        ('madre', 'Madre'),
        ('hermano', 'Hermano'),
        ('esposa', 'Esposa'),
        ('hijo', 'Hijo'),
        ('hija', 'Hija'),
        ('mascota', 'Mascota'),
    )

    first_name = models.CharField('Nombre', max_length=15)
    last_name = models.CharField('Apellido', max_length=15)
    full_name  = models.CharField('Nombre Completo', max_length=30, blank=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today)
    age = models.PositiveIntegerField('Edad', default=1)
    relative = models.CharField('Parentesco', max_length=50, choices=RELATIVE)
    foto = models.ImageField(upload_to='familia', blank=True, null=True)
    hobbies = models.ManyToManyField(Hobbies)
    bio = RichTextField('Bio', default='')
    

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Familiar'
        verbose_name_plural = 'Familiares'
        ordering = ['-id', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
