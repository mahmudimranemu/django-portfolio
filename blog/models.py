from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=60)

    class Meta:
        verbose_name_plural="categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=255)
    featured_image=models.FileField(upload_to="blog/featured_images/")
    body=models.TextField()
    categories=models.ManyToManyField("Category", related_name="posts")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
