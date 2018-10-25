Create an environment with k8s
==============================

# Build the Docker image

```
USER_ID=[YOUR USER ID ON MN-1 CLUSTER]

docker build --rm \
--build-arg USER_ID=${USER_ID} \
--build-arg USER_NAME=${USER} \
-t harbor.pfn.io/user-${USER}/medical-ai .

docker push harbor.pfn.io/user-${USER}/medical-ai
```

# Create a pod

```
kubectl port-forward medical-ai :8080
kubectl apply -f pod.yml
```

# Launch Jupyter notebook

```
kubectl exec -ti mecial-ai zsh
jupyter notebook --no-browser --ip 0.0.0.0 --port 8080 --NotebookApp.token=''
```

