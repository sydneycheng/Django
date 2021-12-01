from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
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


def new_topic(request):
    if request.method != "POST":  # this means it's a GET request
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)  # this means it's a POST request

        if form.is_valid():
            form.save()

            return redirect("MainApp:topics")

    context = {"form": form}
    return render(request, "MainApp/new_topic.html", context)

    # context is a dictionary that allows us to pass data (to the topic.html file in this case)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(
                commit=False
            )  # we aren't ready to write this to the database just yet; this is a temporary entry
            new_entry.topic = topic
            new_entry.save()

            return redirect("MainApp:topic", topic_id=topic_id)

    context = {"form": form, "topic": topic}
    return render(request, "MainApp/new_entry.html", context)
