from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=25)
    release_date = models.DateField()
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"Shows {self.title} {self.network} {self.release_date}"