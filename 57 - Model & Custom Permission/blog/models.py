from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Artikel(models.Model):
    judul       = models.CharField(max_length=255)
    isi         = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    is_publish  = models.NullBooleanField(default=False)
    published   = models.DateTimeField(null=True)
    slug        = models.SlugField(blank=True, editable=False)

    class Meta:
        default_permissions = ('add', 'change', 'delete')
        permissions = (
            ('publish_artikel', 'Can publish artikel'),
        )

    def save(self):
        self.slug = slugify(self.judul)
        if self.is_publish == True:
            self.published = timezone.now()
        else:
            self.published = None
        super().save()

    def __str__(self):
        return '{}. {}'.format(self.id, self.judul)
