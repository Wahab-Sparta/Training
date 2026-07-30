# Kubernetes

## Some of the biggest challenges facing enterprises
  
* Modernise legacy application
* Migrating to the cloud or back to on-prem
* Costs of Cloud & AI use
* Security and Compliance
  * AI assisted hacks
  * Need to protect data (as well as applications & services)
* Understanding how they can make best use of AI
* Containerisation -> Kubernetes

## Intro to Kubernetes

* Why is Kubernetes needed
  * Manage containers, especially scaling

* Benefits of Kubernetes
  * Orchestrate/schedule/manage containers at scale
  * Open-source
  * Can run anywhere
  * Self-healing
  * Auto scaling
  * Load balancing
  * Rolling updating & Rollbacks
  * Declarative
  * For production, designed to have no single point of failure

* Success stories
  * Pokemon GO (2015)
    * Ran on Kubernetes on Google architecture
    * Exceeded the load they expected by 50 times and was still able to handle it

* Kubernetes architecture (include a diagram)

* The cluster setup

  * What is a cluster
    * A cluster is a set of machines called nodes that run your container apps
    * Made up of at least one master node
    * Must have at least one worker node
    * For production, we'd want a multi-node setup (multiple workers)
    * For dev/testing purpose, usually we'd have a single setup (single worker node)
  * How it works with AKS (Azure Kubernetes Service)
    * Master node and worker nodes are kept separate 
    * Azure takes care of running the master node
    * Azure doesn't charge you for the master node
    * What you pay for: One VM per worker node
  * Comparing to AWS & GCP
    * With EKS (Elastic Kubernetes Service) or GKE (Google Kubernetes Engine) you pay for the master node (around 10p/hr)
  * How it works with Minikube
    * Both master & worker nodes can be run on a single VM

  * Pros and cons of using managed service
    * Managed Service (AKS, EKS, GKE)
      * Pros
        * Master node is automatically managed
      * Cons
        * Have to pay for it (EKS, GKE)

  * Control plane vs data plane
    * Control plane
      * Has master node(s)
      * Controller Manager monitors for changes in the cluster, if changes do need to be changed it goes through the API server.
      * API server is the central hub for all communication
      * Scheduler creates worker nodes based on resource availability
      * ETCD is a database that keeps tracks of whats happening in the cluster using key value pairs
    * Data plane has worker node(s)
      * Kubelet connects directly to and receives instructions from the API server on the Control plane
      * kube-proxy controls the network routing
      * Container Engine
      * Pods

* Kubernetes objects
  * Deployments
    * Contains Replica Set and Pods
  * Replica Set
    * Can contain pods
    * Can replicate pods
  * Pods
    * Container is not the same as a pod
    * Smallest component of Kubernetes
    * Pod can contain multiple containers, but usually you'd have one container
      * E.g 2nd container can act like a service like logging
    * Pod doesn't need to be inside a Replica Set but can be if you want a duplicate
    * Pods are ephemeral
  * Service 
    * Used to either expose pods to the outside world or expose pods for communication between other pods
  * Volumes
    * Used for persistent storage

* How to mitigate security concerns with containers
  * Use maintained container images
  * Use automatic vulnerability scanning on container registry
  * Use your own security scanning tool on your container images
  * NEVER run containers with root privileges
  * Monitor and/or log of container activity

* Maintained images
  * A docker image that is regularly updated/manages by a maintainer
  * Usually the maintainer of the image is an organisation, a community, or an individual.
    * Example: Canonical maintain Ubuntu images
  * Pros and cons of using maintained images for your base container images
    * Pros:
      * Better security because they are regularly patched
      * Up to date
      * Better stability and reliability
      * More support and documentation available
      * Usually adhering to best practices/industry standards
      * May be more streamlined and optimised for performance and/or smaller image size
    * Cons:
      * 


## Commands
```
kubectl get all
# Shows everything running
# Can do "deployments", "pods" instead of "all"

kubectl create -f <filename>
# Creates a deployment
# -f means file

kubectl apply -f <filename>
# Updates deployment

kubectl delete -f <filename>
# Removes deployment
```