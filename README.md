
# Celery demonstration

Project: SSH credentials bruteforcing: scanning the whole Internet with a username/password pair.

Coded as a demonstration during a talk about queues and workers at Epitech.

## Requirements
- docker
- docker-compose
- browser

## Start
- run the app: $> fig up -d
- start a scan: $> google-chrome-stable http://localhost:8000
- queue monitoring: $> google-chrome-stable http://localhost:5555
- cpu monitoring: $> htop
- queue progress: $> watch 'cat celery1.log | tail'
- valid credentials found: $> google-chrome-stable http://localhost:8000

## Utils
Most used SSH credentials: https://peguta.com/articles/common-used-passwords
