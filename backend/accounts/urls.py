from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views
from django.urls import path
from .views import SignUpView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Define URL patterns for the accounts app.
urlpatterns = [
    path('profile/',views.ProfileView.as_view()),  # URL for the ProfileView that requires authentication.
    path('api/auth/', views.CustomAuthToken.as_view()),  # URL for the CustomAuthToken view that generates auth tokens.
    path('profile/',views.LoginView.as_view()), 
    path('signup/', SignUpView.as_view(), name='signup'),   
    path('api/auth/', views.MyProtectedView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]

# Add support for URL suffixes like '.json' or '.api'.ss
# This allows clients to specify the format of the response data they want to receive.
urlpatterns = format_suffix_patterns(urlpatterns)




# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def check_auth(request):
#     """
#     View to check if user is authenticated and their token is valid.
#     """
#     return Response({'message': 'User is authenticated.'})

# urlpatterns = [
#     path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
#     path('check-auth/', check_auth, name='check_auth'),
# ]






