from django.apps import apps
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def run_migrations(request):
    try:
        call_command('makemigrations')
        call_command('migrate')
        return HttpResponse("Migrations completed successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def create_superuser(request):
    try:
        # Use the appropriate user model
        User = get_user_model()
        email = 'esterlinjpaulino@gmail.com'  # Set your desired email
        username = 'Ester'  # Set your desired username
        password = 'admin-app123'  # Set your desired password

        # Check if the superuser already exists
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            return HttpResponse("Superuser already exists.")

        # Create the superuser
        User.objects.create_superuser(email=email, username=username, password=password)
        
        return HttpResponse("Superuser created successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
