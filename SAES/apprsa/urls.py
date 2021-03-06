from django.urls import path
from apprsa.views.decrypt_view import DecryptView
from apprsa.views.encrypt_view import EncryptView
from apprsa.views.key_view import KeyView

urlpatterns = [
    path(r'key/', KeyView.as_view(), name='rsa-key'),
    path(r'encrypt/', EncryptView.as_view(), name='rsa-encrypt'),
    path(r'encrypt/<int:first_key>/<int:second_key>/', EncryptView.as_view(), name='rsa-encrypt'),
    path(r'decrypt/', DecryptView.as_view(), name='rsa-decrypt'),
    path(r'decrypt/<int:first_key>/<int:second_key>/', DecryptView.as_view(), name='rsa-decrypt'),
]