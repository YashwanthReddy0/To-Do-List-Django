from django.db import models

# Create your models here.
class Todolist(models.Model):
    task = models.TextField()
    description =models.TextField()
    
class DeletedTask(models.Model):
    task = models.CharField(max_length=200)
    description = models.TextField()
    deleted_at = models.DateTimeField(auto_now_add=True)    