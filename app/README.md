# christmas

## Run Locally without Docker

Install Python 3

Clone the project

```
git clone https://github.com/anaislet/christmas
```

Start a virtual ENV

```
source ENV/bin/activate
```

Install depedencies (Django...)

```
pip install -r requirements.txt
```

Run server

```
python3 manage.py runserver
```

## Run Locally with Docker and Docker-compose

sudo docker-compose up --build (avec affichage des logs)

sudo docker-compose up --build -d (sans affichage des logs)

sudo docker-compose down (pour stopper les containers et les supprimer)

## Build de l'image

sudo docker build . -t christmas:latest

## Lancer un conteneur

sudo docker run -p 3100:8000 christmas

## Consulter le site depuis le navigateur

http://localhost:3100/

## Commandes utiles

sudo docker container ls : Afficher la liste des conteneurs actifs

sudo docker container ls -a : Afficher la liste des conteneurs

sudo docker image ls : Afficher la liste des images

sudo docker image rm id_de_l'image : Supprimer une image (possibilité d'utiliser -f pour forcer)

sudo docker container prune : Supprimer les containers arrêtés

sudo docker image prune : Supprimer les images n'ayant pas de containers actifs