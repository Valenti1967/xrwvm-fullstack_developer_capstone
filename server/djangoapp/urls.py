from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration
    path('register', views.registration, name='register'),

    # Paths for login/logout
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),

    # Path to get all cars
    path('get_cars', views.get_cars, name='getcars'),

    # Dealer-related views
    path(
        'get_dealers',
        views.get_dealerships,
        name='get_dealers'
    ),
    path(
        'get_dealers/<str:state>',
        views.get_dealerships,
        name='get_dealers_by_state'
    ),
    path(
        'dealer/<int:dealer_id>',
        views.get_dealer_details,
        name='dealer_details'
    ),
    path(
        'reviews/dealer/<int:dealer_id>',
        views.get_dealer_reviews,
        name='dealer_reviews'
    ),

    # Path to add a review
    path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
