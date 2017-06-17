from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="todo"

urlpatterns=[

    url(r"^$", views.IndexView, name="index"),
    url(r'^(?P<id>[0-9]+)/$', views.DetailToDo, name="detail"),
    url(r"^add/$", views.AddTodo, name="create"),
    url(r"^addbooks/$", views.addbooks, name="createbook"),
    url(r"^search/$", views.SearchTodo, name="search"),
    url(r'^(?P<id>[0-9]+)/done/$', views.TodoDone, name="done"),

    url(r'^deleteitem/(?P<id>[0-9]+)/$', views.TodoDelete, name="deleteitem"),
    url(r"^profile/$", views.ProfileView, name="profile"),
    url(r"^search/$", views.SearchTodo, name="search"),
    url(r"^listbooks/$", views.listbooks, name="listbooks"),
    url(r"^bookdetail/(?P<id>[0-9]+)/$", views.bookdetail, name="bookdetail"),
    url(r"^dataframetest/$", views.dataframe, name = "dataframetest"),

]