FROM python
RUN mkdir -p /app/bin
COPY ./ /app/bin
RUN pip install -r /app/bin/requirements.txt
EXPOSE 8000
CMD python /app/bin/manage.py runserver 0.0.0.0:8000