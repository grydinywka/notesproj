Test app for 'PlasticJam'

Manual about deploying project locally:

git clone https://github.com/grydinywka/sergiy_ignatenko_test_pj

cd sergiy_ignatenko_test_pj

virtualenv -p python3 .env

source .env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

