from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.message


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
