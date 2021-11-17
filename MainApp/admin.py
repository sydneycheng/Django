from django.contrib import admin

# Register your models here.
from .models import Topic
from .models import Entry

# allows us to access model on admin side
admin.site.register(Topic)
admin.site.register(Entry)
