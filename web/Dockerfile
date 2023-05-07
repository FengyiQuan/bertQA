FROM python:3.7.9
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD .. /code/
# ENTRYPOINT ["python3"] 
# CMD ["manage.py", "runserver", "0.0.0.0:8080"]
#CMD ["gunicorn", "web.wsgi"]
CMD ["gunicorn", "web.wsgi", "-b", "0.0.0.0:8080"]
EXPOSE 8080