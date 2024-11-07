from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'choice_text',
        'vote',
    ]

class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'question_text',
        'pub_date',
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)