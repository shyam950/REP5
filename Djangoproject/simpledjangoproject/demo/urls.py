from django.urls import path
from .views import myfunction
from .import views
urlpatterns = [
        path("", myfunction),
        path("add", views.add, name="add")

]
