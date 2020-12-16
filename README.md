# Deepface Analyze ML models using Flask + Gunicorn + Nginx inside Docker

## Running the solution

In order to run this solution, you just have to install Docker, Docker compose, then clone this repository, and then:
```
bash run_docker.sh
```

For Docker installation instructions follow:

— [Docker installation](https://docs.docker.com/engine/install/ubuntu/)

— [Make Docker run without root](https://docs.docker.com/engine/install/linux-postinstall/)

— [Docker Compose installation](https://docs.docker.com/compose/install/)

## Understanding the solution

— The fast way: the project is structured as follows: Flask app and WSGI entry point are localed in flask_app directory. Nginx and project configuration files are located in nginx directory. Both directories contain Docker files that are connected using docker_compose.yml file in the main directory. 
  
   For simplicity, I also added run_docker.sh file for an even easier setting-up and running this solution. 
```
.
├── flask_app 
|   ├── src
|   |   ├── commons
|   |   |   ├── distance.py
|   |   |   ├── functions.py
|   |   |   └── realtime.py
|   |   ├── weights
|   |   |   ├── age_model_weights.h5
|   |   |   ├── race_model_single_batch.h5
|   |   |   └── facial_expression_model_weights.h5
|   |   ├── Age.py
|   |   ├── Emotion.py
|   |   └── Race.py
│   ├── api.py          
│   ├── wsgi.py
│   ├── Dockerfile
|   ├── requirements.txt
|   └── environment.yml
├── nginx
│   ├── nginx.conf          
│   ├── project.conf
│   └── Dockerfile
├── docker-compose.yml
└── run_docker.sh
```
