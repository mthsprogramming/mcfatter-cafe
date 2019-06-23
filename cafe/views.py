from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import BlogPost, MenuItem, Ticket, Specials, Menu, Order
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ContactForm
import json


# Views for the cafe app


# News / Home
# Models used: BlogPost
# BlogPost - Author, Category, Body, Title, Date


class IndexView(generic.ListView):
    template_name = 'cafe/index.html'
    context_object_name = 'home_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cafe_specials'] = Specials.objects.all()
        context['cafe_menu_object'] = Menu.objects.filter(location_name__contains="Cafe")
        return context

    def get_queryset(self):
        return BlogPost.objects.filter(pub_date__lte=timezone.localtime(timezone.now()),
                                       category__title__contains="News").order_by('-pub_date')[:5]


# About
# Models used: BlogPost, TeamMembers
# TeamMember - Name, Image, Roles, Bio


class AboutView(generic.ListView):
    template_name = 'cafe/about.html'
    context_object_name = 'about_post_list'

    def get_queryset(self):
        return BlogPost.objects.filter(pub_date__lte=timezone.localtime(timezone.now()),
                                       category__title__contains="About").order_by('-pub_date')


# Menu
# Models used: Menu, MenuItem
# Menu - Location
# MenuItem - Name, Price, Calories, Protein, Carbohydates, Sugar, Fat
# Uses a JavaScript to add things to order


class MenuView(generic.ListView):
    template_name = 'cafe/menu.html'
    context_object_name = 'menu_item_list'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['cafe_menu_object'] = Menu.objects.filter(location_name__contains="Cafe")
        return context

    def get_queryset(self):
        return MenuItem.objects.all()


# Order / Cart
# Models used:
# View order via a JavaScript


class OrderView(generic.TemplateView):
    template_name = 'cafe/order.html'


# Confirm order
# Redirected to this view from order


def checkout(request):
    if request.method == 'POST':
        data = request.POST
        pickup_time_fixed = '{} {}'.format(timezone.localtime(timezone.now()).date(), data['pickupTime'])
        cart = json.loads(data['cart'])  # pass the json string here
        items = ''
        total = 0.0
        instructions = ''
        for item in cart:
            if items == '':
                items = '{}x {}'.format(item['qty'], item['item'])
                instructions = item['instructions']
            else:
                items = '{}; {}x {}'.format(items, item['qty'], item['item'])
                instructions = '{}; {}'.format(instructions, item['instructions'])
            total += float(item['price'])

        order = Order.objects.create(order_for=data['orderFor'], pickup_time=pickup_time_fixed,
                                     time_placed=timezone.localtime(timezone.now()), items=items, total=total,
                                     instructions=instructions)
        if request.user.is_authenticated:
            order.user = request.user.cafeprofile
        order.save()
    else:
        print('User tried to circumvent POST')
    return redirect('cafe:index')


# Submit a support ticket
# Validates and processes a ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket = Ticket.objects.create(first_name=data['first_name'], last_name=data['last_name'],
                                           phone_number=data['phone_number'], email=data['email'],
                                           subject=data['subject'],
                                           ticket_text=data['comments'], date=timezone.localtime(timezone.now()),
                                           category=data['category'])
            if request.user.is_authenticated:
                ticket.user = request.user.cafeprofile
            ticket.save()
            return redirect('cafe:index')
    else:
        if request.user.is_authenticated:
            user = request.user
            data = {'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'phone_number': user.cafeprofile.phone_number}
            form = ContactForm(initial=data)
        else:
            form = ContactForm()
    return render(request, 'cafe/contact.html', {'form': form})


# Generic view for Login page

class LoginView(generic.TemplateView):
    template_name = 'cafe/login.html'


# Registration page
# Validates and processes a SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.cafeprofile.birth_date = form.cleaned_data.get('birth_date')
            user.cafeprofile.phone_number = form.cleaned_data.get('phone_number')
            user.cafeprofile.save()
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('cafe:index')
    else:
        form = SignUpForm()
    return render(request, 'cafe/register.html', {'form': form})


# Profile view, just renders the template

def profile(request):
    return render(request, 'cafe/profile.html')


# Update profile view, invoked from profile page

def update_profile(request):
    if request.method == 'POST':
        data = request.POST

        if request.user.is_authenticated:
            request.user.email = data['email']
            request.user.cafeprofile.phone_number = data['phonenumber']
            request.user.save()
            request.user.cafeprofile.save()

        return redirect('cafe:profile')
    else:
        return redirect('cafe:profile')
