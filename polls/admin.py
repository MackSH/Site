from django.contrib import admin
from mongoengine.django.admin import DocumentAdmin
from .models import Question, Choice

# Enregistrez les modèles MongoEngine avec l'admin Django
@admin.register(Question)
class QuestionAdmin(DocumentAdmin):
    pass

@admin.register(Choice)
class ChoiceAdmin(DocumentAdmin):
    pass
