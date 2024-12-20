from .models import UserInfo

def get_users_data():
    users = UserInfo.objects.all()

    return users