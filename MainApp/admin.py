from django.contrib import admin

# Register your models here.
from .models import Topic

# allows us to access model on admin side
admin.site.register(Topic)
