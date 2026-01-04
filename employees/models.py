from django.db import models

class employeeModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)   # Soft delete
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
