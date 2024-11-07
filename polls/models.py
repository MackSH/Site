from mongoengine import Document, StringField, DateTimeField, IntField, ReferenceField

# Modèle Question
class Question(Document):
    question_text = StringField(max_length=200)
    pub_date = DateTimeField()

    def __str__(self):
        return self.question_text

# Modèle Choice
class Choice(Document):
    question = ReferenceField(Question, reverse_delete_rule=4)  # reverse_delete_rule=4 simule l'on_delete=models.CASCADE
    choice_text = StringField(max_length=200)
    vote = IntField(default=0)

    def __str__(self):
        return self.choice_text
