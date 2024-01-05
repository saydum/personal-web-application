from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    content = models.TextField()
    createed_at = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-createed_at']

    def __str__(self):
        return self.title