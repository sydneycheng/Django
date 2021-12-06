from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method != "POST":
        form = (
            UserCreationForm()
        )  # we are loading up a blank form for this GET request (reading from database)
    else:
        form = UserCreationForm(
            data=request.POST
        )  # if the method is POST (writing to databse)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("MainApp:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
