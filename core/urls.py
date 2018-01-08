from django.urls import path


from . import views

urlpatterns = [
                path('home/', views.home, name = 'home'),
                path('?P<meetup_id>[0-9]+', views.meetup_detail, name = "meetup_detail"),
                ]
