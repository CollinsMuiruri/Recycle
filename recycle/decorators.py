from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def company_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks if the user is a compnay and redirects to login page if they are not
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_company,
        login_url = login_url,
        redirect_field_name = redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator