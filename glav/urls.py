from django.urls import path

from glav.views import get_page_1, get_plus, get_capitalize

urlpatterns = [
    path('',get_page_1),
    path('pl',get_plus,name='plus'),
    path('cp/<int:id>/',get_capitalize,name='c'),
]