from django.db import models

class Comment(models.Model):
    apod_date = models.DateField()
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.apod_date}"
