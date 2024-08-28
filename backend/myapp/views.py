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
        call_command('createsuperuser', interactive=False)
        return HttpResponse("Superuser created successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
