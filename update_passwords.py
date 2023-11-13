import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmanage.settings')
django.setup()

from django.contrib.auth.models import User

def update_passwords():
    users_to_update = {
        'admin': 'admin',
        'manager': 'admin'
    }

    for username, new_password in users_to_update.items():
        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            print(f'Successfully updated password for user "{username}"')
        except User.DoesNotExist:
            print(f'User "{username}" does not exist')

if __name__ == '__main__':
    update_passwords()
