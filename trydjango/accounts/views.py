from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register_view(request):
  form = UserCreationForm(request.POST or None)
  
  if form.is_valid():
    user_obj = form.save()
    return redirect("login_view")

  context = {
    "form" : form
  }
  return render(request, template_name="accounts/register.html", context=context)

def login_view(request):
    context = {}  # Create an empty context dictionary

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user is None:
            context["error"] = "Incorrect username or password"
            return render(request, template_name="accounts/login.html", context=context)
        else:
            login(request, user)
            return redirect('home_view')
    else:
        # Display the login form when request method is GET
        form = AuthenticationForm()
        context["form"] = form

    return render(request, template_name="accounts/login.html", context=context)


def logout_view(request):
  if request.method == "POST":
    logout(request)
    return redirect('login_view')

  return render(request, template_name="accounts/logout.html", context={})