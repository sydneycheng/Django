from django.shortcuts import render

from .models import Topic


# Create your views here.
def index(request):
    return render(request, "MainApp/index.html")


def topics(request):
    topics = Topic.objects.order_by(
        "date_added"
    )  # if you put a '-' in front of "date_added" it would sort by descending order

    context = {"topics": topics}
    # context is our dictionary
    # the key is the variable used in the template (html) file;
    # the value of the dictionary is the variable used in the view function

    return render(request, "MainApp/topics.html", context)
    # we are passing this dictionary (context) to our html file


# topic_id comes from urls.py
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.all()

    # key represents the variable name in the template
    # value represents the varible name in the view
    context = {"topic": topic, "entries": entries}

    return render(request, "MainApp/topic.html", context)
