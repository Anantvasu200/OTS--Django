from django.db import models

# Create your models here.
class Candidate(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    password =models.CharField(null=False, max_length=100)
    name = models.CharField(null=False, max_length=100)
    test_attempted = models.IntegerField(default=0)
    points = models.FloatField(default=0)
    def __str__(self):
        return self.username

class question(models.Model):
    question_id = models.BigAutoField(primary_key=True, auto_created=True)
    question = models.CharField(max_length=500)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    option3= models.CharField(max_length=100)
    option4= models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

class Result(models.Model):
    Result_id = models.BigAutoField(primary_key=True, auto_created=True)
    username = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    date =models.DateField(auto_now=True)
    attempt =models.IntegerField(default=0)
    score = models.FloatField(default=0)
    wrong = models.IntegerField(default=0)
    def __str__(self):
        return self.username   


