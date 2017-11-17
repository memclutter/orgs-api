# Organizations API

API repository for organizations project.

## Up and running

1. Create PostgreSQL user and database. Copy file `.env.dist` to `.env` and edit database connection.
2. Setup virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
``` 

3. Apply migrations `./manage.py migrate`
4. Check unit tests is work `./manage.py test -k`
5. Run development server `./manage.py runserver`, test your live api `http://localhost:8000/v1/`.
6. Read API documentations on `http://localhost:8000/v1/docs`.

