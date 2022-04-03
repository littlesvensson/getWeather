FROM python:3.10.4
COPY getweather.py ./
RUN pip install pyowm
CMD ["python","./getweather.py"]