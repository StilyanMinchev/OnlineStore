from django.contrib.auth.models import User
from django.db import models

from store_auth.models import UserProfile
from store.validators import positive_number


class Watch(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=(positive_number,))
    image = models.ImageField(
        upload_to='watches',
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    #     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Like(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    test = models.CharField(max_length=2)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like'


class Comment(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment'
