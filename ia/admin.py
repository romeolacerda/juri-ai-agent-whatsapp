from django.contrib import admin

from ia.models import ContextRag, Pergunta

# Register your models here.
admin.site.register(Pergunta)
admin.site.register(ContextRag)