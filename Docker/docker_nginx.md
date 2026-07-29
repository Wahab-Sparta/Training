# Create own version of NGINX

1. First pull nginx using:
```
docker pull nginx
```
2. Run the container using:
```
docker run -d -p 80:80 nginx
```
* `-d` will run it in the background and -p publishes the ports to run, the first is our local machine and the second is in the container.

3. Next we need to go into the container and change the html:
```
docker exec -it <container_name> OR <container_ID> sh
```
* `docker exec` runs a command in the container
* `-it` allocates a terminal you can interact with and `sh` is the type (shell)

4. Now inside the container go to the index.html file in NGINX:
```
cd /usr/share/nginx/html
nano index.html
```
5. Change anything in index.html and see the changes on `localhost`

To make your own image from this:

1. While the container is running, use the command:
```
docker commit <container_name> <username/image_name>
```
* This naming convention of <username/image_name> allows Docker Hub to recognise where the repository will be stored.
* If you dont name the image with your username and image, you can use `docker tag <image_name> <username/image_name>`, which tags the image. 
* It technically just creates a new name for the image, on Docker Desktop you'll see both images still existing, but they point to a single image ID. You can remove the prior image.
2. Next push the new image to Docker Hub with the command:
```
docker push <image_name>
```

# Automate creating docker image using Dockerfile

We will automate the above, where you can use your own index.html instead of the default nginx webpage.

1. First, create a folder and put your index.html inside.   
2. Next, create a dockerfile.

Inside the dockerfile enter the commands:
```
FROM nginx
WORKDIR /usr/share/nginx/html

COPY index.html ./
```
* `FROM nginx` Pulls the nginx image from the docker registry
* `WORKDIR` Changes the directory inside the container for specific commands like `COPY`
* `COPY` Copies the source file from the current directory (unless directory is specified) and delivers it to the specified directory in the container.
  * In this case `./` is actually `/usr/share/nginx/html` since we specified `WORKDIR`

3. In your terminal cd into the current directory and use the command:
```
docker build -t <username/image_name>:<version> .
```
   * `-t` allows you to tag the image with a name and version.
   * The `.` at the end tells docker to build everything in the current directory

Your new image is now created.

To test your new image works run the command:
```
docker run -d -p 90:80 <image_name>
# We're running it on port 90 in case port 80 is already taken
```
