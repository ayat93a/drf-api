from pickle import TRUE
from re import M
from django.db import models
from django.contrib.auth import get_user_model


class Show(models.Model):
    show_name = models.CharField(max_length= 64)
    show_time = models.TimeField()
    show_length = models.IntegerField()
    review = models.TextField(null= True)
    reviewer = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , null= True)


    def __str__(self) :
        return self.show_name