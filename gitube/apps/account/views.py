from django.contrib.auth.models import User

import django_authopenid
from django_authopenid.views import not_authenticated


@not_authenticated
def register(request):
    django_authopenid.views.register_account = register_account
    return django_authopenid.views.register(request, send_email=False)

def register_account(form, _openid):
    user = User.objects.create_user(form.cleaned_data['username'], 
                            form.cleaned_data['email'])
    user.is_active = False
    user.save()
    