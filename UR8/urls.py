from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^sign-up/$', views.signup_view, name="sign_up"),
    url(r'^sign-in/$', views.signin_view, name="sign_in"),
    url(r'^sign-out/$', views.signout_view, name="sign_out"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^edit_avatar/$', views.edit_avatar, name="edit_avatar"),
    url(r'^reset-pwd/$', views.reset_pwd, name="reset_pwd"),
]
