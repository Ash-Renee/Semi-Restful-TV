from django.db import models
import re

class ShowsManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if 'title' not in post_data:
            errors['title'] = "Show title should be at least 2 characters"
        elif len(post_data['title']) < 2:
            errors['title'] = "Show title should be at least 2 characters"

        if 'network' not in post_data:
            errors['network'] = "Show network should be at least 3 characters"
        elif len(post_data['network']) < 3:
            errors['network'] = "Show network should be at least 3 characters"

        if 'desc' not in post_data:
            errors['desc'] = "Show description should be at least 10 characters"
        elif len(post_data['desc']) < 10:
            errors['desc'] = "Show description should be at least 10 characters"

        return errors

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=25)
    release_date = models.DateField()
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ShowsManager()

    def __repr__(self):
        return f"Shows {self.title} {self.network} {self.release_date}"


