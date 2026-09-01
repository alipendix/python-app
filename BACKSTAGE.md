Arracanr contenedor en caliente para instalación de backsage:

docker run --rm -p 3000:3000 -ti -v /home/alleraro/backstage-app:/app -w /app node:22-bookworm-slim bash

Ahora necesitamos 2 puertos back y front

docker run --rm -p 3000:3000  -ti -p 7007:7007 -v /home/alleraro/backstage-app:/app -w /app node:22-bookworm-slim bash


Configurar seguridad con github

docker run --rm -e AUTH_GITHUB_CLIENT_ID=72819833 -e AUTH_GITHUB_CLIENT_SECRET=f5c1f4ab3d268b1958523445e6ef3a95f05dd628 -p 3000:3000  -ti -p 7007:7007 -v /home/alleraro/backstage-app:/app -w /app node:22-bookworm-slim bash

ClientID: 72819833
ClientSecret:f5c1f4ab3d268b1958523445e6ef3a95f05dd628