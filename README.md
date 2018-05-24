# k8s-python-api
Simple Python API with Containers support for K8s tests

For build container :
```powershell
docker build -t k8s-python-api .
```
For run after successful build:
```powershell
 docker run -p 4000:80 k8s-python-api
```
To check open [localhost:4000](http://localhost:4000)

![alt text](https://github.com/bbenetskyy/k8s-python-api/blob/master/localhost_4000.png)


To Shutdown API - just make **POST** request onto http://localhost:4000/shutdown 