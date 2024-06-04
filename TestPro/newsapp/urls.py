from django.urls import path
from .views import NewsP,Home,Contact,NewsDate,SignUp
urlpatterns = [
    path("news/",NewsP,name ='news'),
    path("contact/",Contact,name ='contact'),
    path("",Home,name="home"),
    path("newsdate/<int:year>",NewsDate,name="newsDate"),
    path("signup/",SignUp,name="registration")
]
