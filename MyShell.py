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
    print(
        topic
    )  # don't need topic.text bcs we define .text as a str function in Topic class
    print(topic.date_added)


# get a particular object
t = Topic.objects.get(id=1)
print(t)
# t is the chess object

# bcs of the PK and FK relationship, entry is the FK to the t PK
entries = t.entry_set.all()

# cycle through each entry
for e in entries:
    print(e)
