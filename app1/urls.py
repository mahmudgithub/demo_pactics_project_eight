from django.urls import path
from .views import HomePage, AboutPage, ViewPage, BasePage

urlpatterns = [
	path('',HomePage.as_view(),name='home'),
	path('about/',AboutPage.as_view(),name='about'),
	path('about/view/',ViewPage.as_view(),name='view'),
	path('about/view/base/',BasePage.as_view(),name='base'),
]