# Create TTT App and Database containers using Docker Compose

We  want to create the Tic Tac Toe app container and Database container using Docker Compose to run both simultaneously.

## Manual
First I manually created both the app and database containers to see what was needed to connect the two.  
From doing this I learnt that we need to change the bindip in MongoDB since we are connecting through 127.0.0.1.  
All we need need to do is set the App environment variable to the database IP


## Automatic - Using Compose file

1. Create a file called compose.yaml in a new directory.
2. We need to add both the database and an app as a container.
Database code: 
```
services:
  db:
    image: mongo:8.2.5
    ports: 
    - "27017:27017"
    container_name: "mongodb"
```
* Creates a service called "db" using the MongoDB 8.2.5 image
* Opens ports 27017 on host machine and container
* Sets container name as "mongodb"

App code:
```
  app:
    image: wahabsparta/tech610-tttapp:1.2.0
    ports:
      - "3000:3000"
    environment:
      - MONGODB_URI=mongodb://db:27017/tictactoe
    container_name: "ttt"
    depends_on: 
      - db
```
* Creates a service "app" using my own TicTacToe image
* Opens port 3000 on both machine and container
* Adds an environment variable to the container so the app can connect to the db
  * In the env var, you can see I've used "db" instead of an IP, this will connect it straight to the MongoDB container. 
  * This will change depending on what you have named your service. (E.g. My service was called "db")
* The app service depends on the database service to complete running before running.
  * You can do health checks to make sure that everything on the container is actually running before you start running the app container.

Now you can run `docker compose up -d` (-d means detached) to run the file. (Make sure you're in the folder before running). You can run `docker compose down` to delete the containers.

# Seeding
To seed the MongoDB database we can run seed.js in the app container located at /app/seeds which will upload data from seedData.js into our database. 

In that case we can run a command `node /app/seeds/seed.js" to run the file which will seed the database.
```
command: sh -c "node /app/seeds/seed.js && node /app/index.js"
```
If we put this in the yaml file in our app service, it will run the command once everything has finished running, seeding the database.

# Volumes

Since containers are ephemeral (meaning nothing will persist if the containers are deleted) we need volumes to make data/storage persist. 

However, with the way our yaml file works right now, there would be no point using volumes. 

Currently, our seed.js file will run everytime we run `docker compose up` and when the file runs it deletes everything in the database, and seeds it with the data in seedData.js. Because of this, there's no point using volumes since everything will be deleted on startup. 

To use a volume we must find a way to ONLY run seed.js if the database is empty. This way we can `docker compose up` and seed the database for the first time, then every next time we run `docker compose up` it shouldn't run seed.js, so we don't lose our data.

I haven't implemented this function yet.
