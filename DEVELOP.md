# Recuperar y Configurar un Clúster Kind


## Configuración del Clúster

Archivo `kind-config.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
```

---

## Comprobar Conflictos de Puertos

Antes de crear el clúster, verificar si alguien utiliza los puertos 80 y 443:

```bash
docker ps
```

En este caso, GitLab está usando:

```text
0.0.0.0:80->80/tcp
0.0.0.0:443->443/tcp
```

### Opción 1: Parar GitLab

```bash
docker stop gitlab
```

### Opción 2: Cambiar los Puertos de Kind

Modificar `kind-config.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 8080
    protocol: TCP
  - containerPort: 443
    hostPort: 8443
    protocol: TCP
```

---

## Crear el Clúster

```bash
kind create cluster --name kind --config kind-config.yaml
```

---

## Verificar el Estado

Comprobar que el nodo está funcionando:

```bash
docker ps
```

Debería aparecer:

```text
kind-control-plane
```

Comprobar Kubernetes:

```bash
kubectl get nodes
```

Resultado esperado:

```text
NAME                 STATUS   ROLES           AGE
kind-control-plane   Ready    control-plane   1m
```

Listar namespaces:

```bash
kubectl get namespaces
```

---

# Instalar NGINX Ingress Controller

Instalar el controlador:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

Esperar a que esté listo:

```bash
kubectl wait \
  --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=300s
```

Verificar:

```bash
kubectl get pods -n ingress-nginx
```

---

# Desplegar una Aplicación de Prueba

Crear deployment:

```bash
kubectl create deployment hello \
  --image=nginxdemos/hello
```

Crear service:

```bash
kubectl expose deployment hello \
  --port=80 \
  --target-