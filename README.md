# Machine Learning in Production


### H2 Infrastructure setup


Run sh file to build and push docker images ```opetliak/ml_image:latest and opetliak/web_image:latest``` to docker hub : 
``` 
sh run.sh
```

Start minikube cluster

```
minikube start
```

To create the Pod, run the following command:
```
kubectl apply -f kubernetes/pods/pod.yaml
```

It will sleep forever so we can access it using:

```
kubectl exec -it ml-pod -- bash
```

To create the Job, run the following command:

```
kubectl apply -f kubernetes/jobs/job.yaml
```

If we look at ```kubectl get pod``` we will see that ml-job status is Completed because of ```restartPolicy: Never```


To create the Deployment and Service, run the following command:

```
kubectl apply -f kubernetes/deployments/deployment.yaml
kubectl apply -f kubernetes/services/service.yaml
kubectl get pods # it should show you 3 pods as requested in the yaml
```

To get access outside of the cluster:

```
kubectl port-forward service/ml-service 7080:8080 #or minikube service ml-deployment
```

Go to ```http://localhost:7080/```


Clean up
```
kubectl delete service ml-service
kubectl delete deployment ml-deployment
minikube stop
minikube delete
```
