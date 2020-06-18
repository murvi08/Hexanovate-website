from django.db import models


class Question(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    guidance = models.CharField(max_length=300)
    phone = models.CharField(max_length=11)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + "--" + self.guidance


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
