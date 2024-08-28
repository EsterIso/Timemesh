from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.management import call_command

User = get_user_model()  # This retrieves the custom user model

def run_migrations(request):
    try:
        call_command('migrate')
        return HttpResponse("Migrations completed successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def create_superuser(request):
    try:
        username = 'Ester'  # Set your desired username
        email = 'esterlinjpaulinp@gmail.com'  # Set your desired email
        password = 'admin-app123'  # Set your desired password

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            return HttpResponse("Superuser already exists.")

        # Create the superuser
        User.objects.create_superuser(email=email, username=username, password=password)
        
        return HttpResponse("Superuser created successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
