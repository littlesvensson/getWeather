# getWeather
Simple python weather reporting program bundled with Ansible playbook configured for installing docker. 

docker build --rm -t "getweather:dev" .

docker run --name weatherreporting --env OWM_API_KEY="410949e79c084c1ae243676a2614325f" --env OWM_CITY="Bratislava" getweather:dev
