from django.urls import path
from appsaes.views.decrypt_view import DecryptView
from appsaes.views.encrypt_view import EncryptView

urlpatterns = [
    path(r'encrypt/', EncryptView.as_view(), name='encrypt'),
    path(r'decrypt/', DecryptView.as_view(), name='decrypt'),
]