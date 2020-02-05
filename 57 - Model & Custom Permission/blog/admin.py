from django.contrib import admin
from .models import Artikel
# Register your models here.

class ArtikelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj):
        current_user = request.user

        if obj != None:
            if current_user.has_perm('blog.publish_artikel'):  # ini untuk editor
                readonly_fields = [
                    'created',
                    'updated',
                    'published',
                    'slug',
                ]
                return readonly_fields
            elif current_user.has_perm('blog.add_artikel'): # ini adalah untuk penulis
                if obj.is_publish:
                    return [data.name for data in self.model._meta.fields]
                else:
                    readonly_fields = [
                        'created',
                        'updated',
                        'is_publish',
                        'published',
                        'slug',
                    ]
                    return readonly_fields
        else:
            readonly_fields = [
                'created',
                'updated',
                'is_publish',
                'published',
                'slug',
            ]
            return readonly_fields


admin.site.register(Artikel, ArtikelAdmin)
