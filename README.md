Para correr el proyecto se necesitan setear un .env en la raiz del proyecto
Estos son datos de ejemplo
    user = postgres
    host = localhost
    port = 5433
    bd_name = prueba_finva
    password = root
    API_KEY = "tu api_key"
    BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

necesitas instalar tambien poetry : pip install poetry 
despues usar el comando poetry shell
para iniciar uvicorn main:app --reload
y el comando de alembic upgrade head para la migracion de todas las tablas en la base datos
para acceder al swagger por defecto es http://127.0.0.1:8000/docs