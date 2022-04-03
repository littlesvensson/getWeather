# getWeather

Repository consists of the following parts:
- Ansible playbook handling the Docker service installation
- Weather reporting program for the given city
- Dockerfile enabling to run the Weather reporting in Docker

## How to use
### Requirements
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries by either

```python
$ pip install pyowm
```
or
```
$ pip install -r requirements.txt
```
### Run program locally 
To get the weather reporting, the respective env variables for city(OWM_CITY) and api key(OWM_API_KEY) have to be defined. To export the variables, you can run:
 
```bash
$ source ./.env
```
For the weather reporting, run:

```
$ python getweather.py
```

### Dockerize & run the program 
Getting weather reporting through docker container is easy:

Build the docker image:

```
$ docker build --rm -t "getweather:dev" .
```

Run docker image:
```
$ docker run --rm --name weatherreporting --env OWM_API_KEY="410949e79c084c1ae243676a2614325f" --env OWM_CITY="Bratislava" getweather:dev
```
Without exporting the OWM_CITY variable, you will get weather for lovely city of Trnava :) A valid OWM_API_KEY is mandatory.

### Ansible Playbook
It is possible to install docker service for Ubuntu 18.04 with enabled logging to Docker host´s syslog file. In order to do that, run:
```
$ ansible-playbook -i "localhost," -c local site.yml
```

