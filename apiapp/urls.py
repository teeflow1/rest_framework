from apiapp.views import Postlist, PostDetails
from django.urls import path

urlpatterns = [
    path('api/posts/', Postlist.as_view()),
    path('api/posts/<int:pk/', PostDetails.as_view())
]
