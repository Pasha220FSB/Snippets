from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.forms import SnippetForm, UserRegistrationForm
from MainApp.models import Snippet
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def login_page(request):
    from pprint import pprint
    print(vars(request))
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username,
            password=password)
        if user is not None:
            auth.login(request, user)
            

        else:
            # Return error message
            context = {
                "pagename": "PythonBin",
                "errors": ['wrong username or password'],

            }
            return render(request, "pages/index.html", context)
    return redirect('home')


def logout_page(request):
    auth.logout(request)
    return redirect('home')

def add_snippet_page(request):
    # Создаем пустую форму при запросе GET
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
            }
        return render(request, 'pages/add_snippet.html', context)
    
    # Получаем данные из формы и на их основе создаем новый Сниппет в БД
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect("snippets-list")  # GET /snippets/list
        return render(request,'pages/add_snippet.html', {'form': form})


def snippets_page(request):
    snippets = Snippet.objects.filter(public=True)
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
        }
    return render(request, 'pages/view_snippets.html', context)

@login_required
def my_snippets_page(request):
    snippets = Snippet.objects.filter(user=request.user)
    print(snippets)
    context = {
        'pagename': 'Просмотр моих сниппетов',
        'snippets': snippets
        }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    context = {'pagename': 'Просмотр сниппета'}
    try:
        snippet = Snippet.objects.get(pk=snippet_id)
    except Snippet.DoesNotExist:
        return render(request, "pages/errors.html", context | {"error": f"Snippet with id={snippet_id} not found."})
    else:
        context["snippet"] = snippet
        return render(request, "pages/snippet_detail.html", context)

    
# def create_snippet(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("snippets-list")
#         return render(request,'pages/add_snippet.html', {'form': form})

@login_required
def delete_snippet(request,snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id, user=request.user)
    snippet.delete()
    return redirect('snippets-list')


@login_required
def update_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id, user=request.user)

    if request.method == "GET":
        form = SnippetForm(instance=snippet)
        return render(request, "pages/update_snippet.html",
                      context = {'form':form})
    
    elif request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippets-list')
        
def creat_user(request):
    context = {"pagename":"Регистрация нового пользователя"}
    if request.method == "GET":
        form = UserRegistrationForm()
        context["form"] = form
        return render(request, "pages/register.html", context)
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect("home")
    
    context["form"] = form
    return render(request, "pages/register.html",context)
