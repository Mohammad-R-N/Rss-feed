from django.db import models
from accounts.models import Follow

class Category(models.Model):

    name = models.CharField(max_length=70)


class XML(models.Model):

    link = models.URLField(max_length=255, unique=True)
    name = models.CharField(max_length=50, unique=True, default="Untitled")

    def __str__(self):
        return self.name
    

class Channel(models.Model):

    title = models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    language = models.CharField(max_length=5, null=True, blank=True)
    copyright = models.CharField(max_length=50, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=50, null=True)
    summary = models.TextField(null=True, blank=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    keywords=models.TextField(null=True, blank=True)
    ownerName = models.CharField(max_length=50, null=True, blank=True)
    ownerEmail = models.EmailField(null=True, blank=True)
    isExplicit = models.CharField(max_length=3, default="no")
    xml=models.ForeignKey(XML,on_delete=models.PROTECT)
    follow=models.ForeignKey(Follow,on_delete=models.PROTECT)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    

class Episode(models.Model):

    title = models.CharField(max_length=50,null=True, blank=True)
    link=models.URLField(max_length=255, null=True, blank=True)
    guid=models.CharField(max_length=60)
    pubdate = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    enclosure=models.URLField(max_length=255, null=True, blank=True)
    subtitle=models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=25)
    isExplicit = models.CharField(max_length=3, default="no")
    description = models.TextField(null=True, blank=True)
    keywords=models.TextField(null=True, blank=True)
    encoded=models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    player = models.URLField(max_length=255)
    image = models.URLField(max_length=255, null=True, blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT)

    def __str__(self):
        return self.title