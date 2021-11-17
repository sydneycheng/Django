import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

# can't have these 2 import statements together
import django

django.setup()

from MainApp.models import Topic, Entry

# similar to SQL's: SELECT * FROM Topic
topics = Topic.objects.all()

for topic in topics:
    print(topic.id)
    print(topic.text)
    print(topic.date_added)
