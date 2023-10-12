from .models import User

# put ur queries here

def get_user(username):
    user = User.objects.get(pk=username)
    return user

def verify_user(username, password):
    pass