# Machine Learning in Production


### H2 Infrastructure setup


Run sh file to build and push the docker image ```opetliak/ml_image:latest``` to docker hub : 
``` 
sh run.sh
```
Run next commands to setup cluster:

```bash
minikube start # create a minikube cluster
kubectl apply -f kubernetes/deployments/deployment.yaml
kubectl get pods # it should show you 3 pods as requested in the yaml
kubectl expose deployment ml-deployment --type=LoadBalancer --port=8080
kubectl port-forward service/ml-deployment 7080:8080 #or minikube service ml-deployment
```

Clean up
```
kubectl delete service ml-deployment
kubectl delete deployment ml-deployment
minikube stop
minikube delete
```
