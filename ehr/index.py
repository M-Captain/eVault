# api/index.py
from ehr.wsgi import application
from vercel_python_wsgi import make_lambda_handler

handler = make_lambda_handler(application)
