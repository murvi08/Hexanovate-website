from django.db import models

from blogs.models import Blog


class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.message
