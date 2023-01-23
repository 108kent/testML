from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
import pickle
import pandas as pd

# Create your models here.
GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)


class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    sex = models.PositiveIntegerField(choices=GENDER, null=True)
    age = models.PositiveIntegerField(null=True)
    year_in_germany = models.PositiveIntegerField(null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = pd.read_pickle('ml_model/model.pkl')
        self.predictions = ml_model.predict(
            [[self.age, self.year_in_germany, self.sex]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
