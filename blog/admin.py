from django.contrib import admin
from .models import Post #w pythonie sa 2 rodzaje importów jawne jak powyższy z "from django...", a niejawny to np. *.models - ta . to ścieżka relacyjna, tak jak .. wchodza wyżej



admin.site.register(Post)
# Register your models here.
