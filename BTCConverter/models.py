from django.db import models

class Signup(models.Model):
    firstName = models.CharField(max_length=40, default='x')
    lastName = models.CharField(max_length=40, default='x')
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

