from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, "MainApp/index.html")


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    # if you put a '-' in front of "date_added" it would sort by descending order

    context = {"topics": topics}
    # context is our dictionary
    # the key is the variable used in the template (html) file;
    # the value of the dictionary is the variable used in the view function

    return render(request, "MainApp/topics.html", context)
    # we are passing this dictionary (context) to our html file


@login_required
# topic_id comes from urls.py
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.all()

    # key represents the variable name in the template
    # value represents the varible name in the view
    context = {"topic": topic, "entries": entries}

    return render(request, "MainApp/topic.html", context)


@login_required
def new_topic(request):
    if request.method != "POST":  # this means it's a GET request
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)  # this means it's a POST request

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # redirect the user's browser to the topics page
            return redirect("MainApp:topics")

    context = {"form": form}
    return render(request, "MainApp/new_topic.html", context)

    # context is a dictionary that allows us to pass data (to the topic.html file in this case)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            # When we call save(), we include the argument comit=False to tell Django to create
            # a new entry object and assign it to new_entry w/o saving it to the database yet.
            new_entry = form.save(
                commit=False
            )  # we aren't ready to write this to the database just yet; this is a temporary entry
            new_entry.topic = topic
            new_entry.save()
            form.save()
            return redirect("MainApp:topic", topic_id=topic_id)

    context = {"form": form, "topic": topic}
    return render(request, "MainApp/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        # This argument tells Django to create the form prefilled
        # with info from the existing entry objects.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("MainApp:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "MainApp/edit_entry.html", context)
