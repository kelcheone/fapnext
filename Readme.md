# JWT AUTH

## Set up

```bash
cd api
touch .env
```

add to .env

```env
DATABASE_HOST=localhost
DATABASE_NAME=fapnext
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_PORT=5432
APP_NAME="JWT WITH FASTAPI"
```

```bash
python3 -m venv env
source /env/bin/activate
pip install -r requirements.txt

uvicorn main:app --reload

alembic upgrade head
```

```bash
cd ../client
npm i or yarn

npm dev or yarn dev
```
