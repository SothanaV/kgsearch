from django.core.files import File
from kgsearch import models

if not models.Dataset.objects.filter(name='example').exists():
    with open('./script/dsi310.csv', 'rb') as f:
        models.Dataset.objects.create(**{
            'name': 'example',
            'original': File(f)
        })