Para rodar o projeto 

Copie a .env.example para env e adicione as keys

depois inicie o ambiente virtual

python3 -m venv venv  

depois ative ele

source venv/bin/activate

depois baixe as dependencias do requirementes.txt

pip install -r requirements.txt

execute as migrations

python3 manage.py migrate

e depois para rodar o app

python3 manage.py runserver