import django_authopenid
from django_authopenid.views import not_authenticated


@not_authenticated
def register(request):
    result = django_authopenid.views.register(request, send_email=False)

    if (request.POST and request.user is not None and not request.user.is_superuser):
        # We need active user by admin.
        request.user.is_active = False
        request.user.save()

    return result
