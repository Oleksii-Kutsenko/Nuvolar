Firstly, set-up environment
```
export FASTAPI_ENV=development
export FASTAPI_ENV=production
```
Secondly, install proper dependencies
```
pip install -r requirements/prod.txt
pip install -r requirements/test.txt
pip install -r requirements/dev.txt
```
Thirdly, run docker, apply migrations and start application
```
./manage.py compose up -d
alembic upgrade head

./manage.py start
```