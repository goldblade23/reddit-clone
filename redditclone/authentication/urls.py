from django.urls import path


from redditclone.authentication.views import index, login_view, logout_view, signup

urlpatterns = [
    path('', index, name="homepage"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view),
    path("signup/", signup),
    ]
