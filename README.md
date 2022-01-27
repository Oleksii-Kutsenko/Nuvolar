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

## Implementation Notes
The subsequent introduction of exception handling will allow the application to respond to exceptional conditions at 
runtime.  For more correct work, it is worth improving the validation of incoming parameters, such as JSON and query 
parameters, which will affect the quality of data processing.  Also, the ability to increase test coverage will help 
evaluate the testing of more scenarios, requirements, and characteristics of particular functionality.  There is an 
option to completely containerize the application by adding services and docker files for Fastapi and Nginx.  For more 
security, in the future, you can add JWT authentication.  You can also set up throttling and API quotas to protect 
applications from too many requests. CORS integration can give web servers the ability to control cross-domain requests 
and securely exchange data between different domains.