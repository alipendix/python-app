# Python App

Servicio REST desarrollado con Flask que expone información básica de la aplicación y un endpoint de salud.

## Endpoints

### GET /api/v1/info

Devuelve información de la instancia en ejecución.

#### Respuesta

```json
{
  "time": "2026-09-01 10:30:12",
  "hostname": "python-app-abc123",
  "message": "Version dinamica v10!!!",
  "deployed_on": "kubernetes"
}
```

### GET /api/v1/healthz

Comprueba el estado del servicio.

#### Respuesta

```json
{
  "status": "up"
}
```

## Tecnologías

- Python 3
- Flask
- Kubernetes

## Ejemplo de uso

```bash
curl http://localhost:5000/api/v1/info
curl http://localhost:5000/api/v1/healthz
```
