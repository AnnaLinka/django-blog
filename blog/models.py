from django.db import models

from django.utils import timezone
# w django importuje się moduły i całe sekcje
# powyższe czyli z django/utils/timzezone.py i tu są funkcje klasy itp.

# Create your models here.
# Poniżej tworzymy swój models

class Post(models.Model): # tworzymy klasę post (nazwa tabeli w bazie danej), dziedziczymy po models.Model
    author = models.ForeignKey('auth.User') #django tworzy automatycznie relację, by móc powiazać dwa obiekty
    #w polu autor powinna być referencja do uzytkownika
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
