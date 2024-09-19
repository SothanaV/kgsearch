from django.db import models


# Create your models here.
class Dataset(models.Model):
    name = models.CharField(max_length=100)
    original = models.FileField(upload_to='data/original')
    pkl = models.FileField(upload_to='data/pkl', null=True, blank=True)
    
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import services
from django.core.files import File

@receiver(post_save, sender=Dataset, dispatch_uid="create_pkl")
def create_pkl(sender, instance, created, **kwargs):
    if created:
        search = services.search.Search(file=instance.original.path)
        search.save(path='/tmp.pkl')
        instance.pkl.save(f'{instance.name}-data.pkl', File(open('/tmp.pkl', 'rb')))
        instance.save() 