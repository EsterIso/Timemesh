set -x  # Enable debugging output
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput
echo "Contents of staticfiles directory:"
ls -R staticfiles