# Deploying TTT App and MongoDB with Kubernetes

We want to make two deployments, one for the app and one for the database.

The app deployment should have 3 replicas and the database deployment should only have one.

## TTT App Deployment
1. First we need to create the deployment yaml file for the app.
2. Inside the deployment file we need to specify:
   * The kind of service to create (Deployment)
   * The name of the deployment
   * A label to reference the app
   * The replica set
   * The image we need to use
   * The environment variable we need to connect to the database
   * The container port we need published
  
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ttt-deployment
spec:
  selector:
    matchLabels:
      app: ttt
  replicas: 3
  template:
    metadata:
      labels:
        app: ttt

    spec:
      containers:
      - name: ttt
        image: wahabsparta/tech610-tttapp:1.2.0
        env:
        - name: MONGODB_URI
          value: "mongodb://mongodb-svc:27017/tictactoe"
        ports:
        - containerPort: 3000
```
* The value given in the environment variable does not use an IP, instead it uses the name of the MongoDB service we will create.

## MongoDB Database Deployment

1. First we need to create the deployment yaml file for the database.
2. Inside the deployment file we need to specify:
   * The kind of service to create (Deployment)
   * The name of the deployment
   * A label to reference the database
   * The image we need to use
   * The container port we need published

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb-deployment
spec:
  selector:
    matchLabels:
      db: mongodb 
  template:
    metadata:
      labels:
        db: mongodb
      
    spec:
      containers:
      - name: mongodb
        image: mongo:8.2.5
        
        ports:
        - containerPort: 27017
```
* Notice how we didn't need to specify a replica, since we only need one pod.

## Services

Lastly we'll need to create a service for each deployment, so the app pods can communicate with the database pod.

For both services we will need to specify:

*  The kind of object (Service)
*  The name of the service
*  The namespace
*  The selector to reference a deployment

In the App service we need to specify:

* The type of service
  * We will use NodePort as we need to connect from external sources
* The target port of the container (3000)
* The port of the service
* The Node Port (How our local machine will connect to the container)

In the Database service we need to specify:
* The type of service
  * We will use ClusterIP, since we only need the database to communicate with the app pods
  * The port of the container (27017)
  * The port of the service


```yaml
---
#APP SERVICE
apiVersion: v1
kind: Service
metadata:
  name: ttt-svc
  namespace: default
spec:
  ports:
  - nodePort: 30001 # range is 30000-32768
    port: 80
    targetPort: 3000
  selector:
    app: ttt  # this label connect this service to the deployment
  type: NodePort  # also use LoadBalancer - for local use cluster IP

---
#DATABASE SERVICE
apiVersion: v1
kind: Service
metadata:
  name: mongodb-svc
  namespace: default
spec:
  ports:
  - name: database
    port: 80
    targetPort: 27017
  selector:
    db: mongodb
  type: ClusterIP 
```