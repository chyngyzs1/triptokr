from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import DetailView

from .forms import CreateUserForm
from django.contrib.auth.models import auth
from .forms import ReviewForm
from .models import Tours, Review



def index(request):
    return render(request, 'blog/index.html')

# User register
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            messages.error(request, form.errors)
            return redirect('register_page')
    form = CreateUserForm()

    return render(request, 'blog/register.html', {'form': form})


# User login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('registrEmail')
        password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'username or password is incorrect!')
    context = {}
    return render(request, 'blog/login.html', context)

#User logout
def logout(request):
    auth.logout(request)
    return redirect('home_page')


def tours_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tours = Tours.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        tours = Tours.objects.all()

    s_chbx = Tours.objects.all()

    paginator = Paginator(tours, 6)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        's_chbx': s_chbx,
    }

    return render(request, 'blog/tours.html', context=context)


def reviews_list(request):


    posts = Review.objects.all()
    return render(request, 'blog/review_list.html', {'posts': posts})

def rev_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews_list')
    form = ReviewForm()
    return render(request, 'blog/review_create.html', {'form': form})


# class ToursDetail(DetailView):
#     model = Tours
#     template_name = 'blog/tours_detail.html'
#     context_object_name = ''
