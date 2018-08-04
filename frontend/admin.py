from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Quote)