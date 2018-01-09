from django.urls import path


from . import views

urlpatterns = [
                path('home/', views.home, name = 'home'),
                path('?P<meetup_id>[0-9]+', views.meetup_detail, name = "meetup_detail"),
                path('create_meetup/', views.create_meetup, name = "create_meetup"),
                path('edit_meetup/?P<meetup_id>[0-9]+/', views.edit_meetup, name = 'edit_meetup'),
                ]
