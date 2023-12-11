# econokey-backend
Econokey is a prototype for a password vault and generator, that differentiates from others by having the capabilities for cryptocurrency cold wallet generation. 
## Instalation

1. Install Python >3.10 https://www.python.org/downloads/
2. Install Poetry as dependency solver https://python-poetry.org/docs/#installation

## Running the app

### Standalone (Must install python and poetry)
1. Clone this repo
2. Open CMD/Terminal
3. Navigate to the folder where the repo was cloned
4. Install dependencies with Poetry```poetry update && poetry install```
5. Run the app with the following command ```python3 -m flask run```
6. Use configure postman url collection variable to your ip (localhost shoud work)
7. Have fun

### Docker
1. Pull the image from the registry ```docker pull econokey/backend:latest```
2. Run the container using ```docker run -p 5000:5000 econokey/backend:latest```
3. Use configure postman url collection variable to the container ip (localhost shoud work)
4. Have fun
