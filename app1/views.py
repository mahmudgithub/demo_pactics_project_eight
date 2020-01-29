
from django.views.generic import ListView
from .models import Mahmud, Hossain, Lamyaa, Nowsin

class HomePage(ListView):
    model = Mahmud
    template_name = "index.html"
    context_object_name='app1'


class AboutPage(ListView):
    template_name = "about.html"
    model = Hossain
    context_object_name='app1'

class ViewPage(ListView):
    template_name = "home.html"
    model = Lamyaa
    context_object_name='app1'

class BasePage(ListView):
    template_name = "base.html"
    model = Nowsin
    context_object_name='app1'