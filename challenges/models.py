from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=20)
    idea = models.CharField(max_length=200)
    position = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    isGoodIdea = models.BooleanField(default=False)
    created_on = models.DateTimeField(null=True ,auto_now_add=True)
    updated_on = models.DateTimeField(null=True, auto_now=True)
    
    
    def __str__(self):
        return f"{self.name} // '{self.idea}' // {self.position} // {self.isGoodIdea} // {self.created_on} // {self.updated_on}"