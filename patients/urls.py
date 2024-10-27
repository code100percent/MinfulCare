from django.urls import path
from . import views
urlpatterns=[
    path('',views.show_homepage),
    path('account/',views.show_accountpage),
    path('account/tell_mood/',views.tell_mood, name = "tell_mood" ),
    path('account/tell_mood/instant_relief/',views.instant_relief)
]