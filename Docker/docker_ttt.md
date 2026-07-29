# Create a container running the TTT app

1. Create a new directory
2. Put your app folder inside the new directory
3. Create a new dockerfile

Inside the dockerfile:
```dockerfile
FROM node:20-alpine
WORKDIR /app/

COPY /app/package.json /app/package-lock.json .
COPY /app/seeds ./seeds
RUN npm ci

COPY /app/ .

USER node

EXPOSE 3000

CMD ["node", "index.js"]
```
* `FROM node:20-alpine` Pulls the image for node version 20, alpine is a small version of it.
* `WORKDIR /app/` Sets the path in the container to /app/
* `COPY` The copy commands copy over the necessary dependencies to run a clean install
* `RUN npm CI` Executes a clean install 
* `COPY /app/ .` Copies over everything inside our app folder into the container app folder (Remember how workdir = /app/, so now all we need to do is .)
* `USER node` Specifies the user in the container as node
* `EXPOSE 3000` Publishes port 3000, doesn't really do much other than let the user know to use port 3000
* `CMD ["node", "index.js"]` Starts the app by running "node index.js"

4. Build the docker image by running the command:
```
docker build -t <image_name>:<version> .
```
* `-t` allows you to tag the image with a name and version.
* The `.` at the end tells docker to build everything in the current directory  
* Remember to use the format "name/image_name:version" so it can be uploaded to Docker Hub.

