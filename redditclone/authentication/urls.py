from django.urls import path

from redditclone.authentication.views import index, LoginView, logout_view, signup, all_communities, handler404, handler500

urlpatterns = [
    path('', index, name="homepage"),
    path('all/', all_communities),
    path("login/", LoginView, name="login"),
    path("logout/", logout_view),
    path("signup/", signup),
] 

handler404 = handler404
handler500 = handler500