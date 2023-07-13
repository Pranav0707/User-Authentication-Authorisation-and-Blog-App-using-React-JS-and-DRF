from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Blog(BaseModel):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255,null=True,blank=True)
    slug=models.SlugField(unique=True,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    image=models.URLField(null=True,blank=True)


    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
       self.slug=slugify(self.title)
       super(Blog, self).save(*args, **kwargs) 

class Comments(BaseModel):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,null=True,blank=True)
    content=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return "Comment on {} ".format(self.blog.title)