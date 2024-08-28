from django.http import HttpResponse
from django.core.management import call_command

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

        # Using Django’s built-in create_superuser method to avoid interactive prompts
        call_command('createsuperuser', 
                     interactive=False, 
                     username=username, 
                     email=email, 
                     password=password)
        
        return HttpResponse("Superuser created successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")