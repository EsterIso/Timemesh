from django.apps import apps
from django.http import HttpResponse
from django.core.management import call_command

def run_migrations(request):
    try:
        call_command('makemigrations')  # This line was corrected
        call_command('migrate')
        return HttpResponse("Migrations completed successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def create_superuser(request):
    try:
        CustomUser = apps.get_model('users', 'CustomUser')
        email = 'esterlinjpaulinp@gmail.com'  # Set your desired email
        username = 'Ester'  # Set your desired username
        password = 'admin-app123'  # Set your desired password

        # Check if the user already exists
        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse("Superuser already exists.")

        # Create the superuser
        CustomUser.objects.create_superuser(email=email, username=username, password=password)
        
        return HttpResponse("Superuser created successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")