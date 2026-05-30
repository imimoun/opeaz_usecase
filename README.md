![Python](https://img.shields.io/badge/python-3.14.5-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-6.0.5-%23092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-18.4-%234169E1?style=for-the-badge&logo=postgresql&logoColor=white)

# Opeaz Usecase
Opeaz Usecase: Implement a tree-structured document management system, across multiple entities, using Django and Django REST Framework.

## Getting Started
```bash
# Clone the repository and navigate to the directory
git clone https://github.com/imimoun/opeaz_usecase.git
cd opeaz_usecase

# Build and run the docker containers
export USER_ID=$(id -u);export GROUP_ID=$(id -g);docker compose -f environments/dev/docker-compose.yml up --build
# Open http://127.0.0.1:8000/

# Set up database
docker exec -it dev-web-1 python manage.py migrate
docker exec -it dev-web-1 python manage.py createsuperuser
docker exec -it dev-web-1 python manage.py loaddata ./fixtures_dev/usecase_example.json
```
