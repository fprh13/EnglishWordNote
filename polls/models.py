from django.db import models

# Create your models here.
class  EnglishWord(models.Model):
    word = models.CharField(max_length=200)

    mean = models.CharField(max_length=200)

    def __str__(self):
        return self.word

    def summary(self):
        return self.word[:100]