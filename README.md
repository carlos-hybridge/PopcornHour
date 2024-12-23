# PopcornHour
## Portal web para recomendar, calificar y discutir sobre películas y series. 

Existirán dos tipos de usuarios: moderador y estándar. 
Los usuarios de tipo “moderador” contarán con la posibilidad para subir películas que los usuarios de tipo estándar
puedan calificar, comentar y discutir

    Dependencias listadas en Pipfile.lock, pero se usa Django y SQLlite3

Para correr el proyecto se necesita instalar pipenv, y después correr:

```bash
pipenv install
```

Una vez instaladas las dependencias se puede ingresar al entorno virutal de la carpeta .venv con: 

```bash
.\.venv\Scripts\activate
```

Una vez levantado el ambiente se corren las migraciones con

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```
El último comando es para checar que se hayan corrído las migraciones y finalmente se levanta el servidor con:


```bash
python manage.py runserver
```

Las vistas de moderador estan listadas en /movies/moderator_urls.py y las de usuario estandar estan listadas en /movies/urls.py,
pero la navegación se puede iniciar desde 

    http://127.0.0.1:8000/moderator/login/

si tienes una cuenta si no en el mismo login se puede navegar al registro y para un usario normal en la url base

    http://127.0.0.1:8000

todo dependiendo de en que puerto levantes el servicio.
