# BrasilAPI Explorer

BrasilAPI Explorer é uma aplicação web que permite consultar diversos endpoints da [BrasilAPI](https://brasilapi.com.br/), como CEP, CNPJ, Câmbio, Corretoras, entre outros. A aplicação foi construída com Flask (backend) e Bootstrap/JavaScript (frontend), e está configurada para rodar em um ambiente Docker.

## Pré-requisitos

- **Docker**: Certifique-se de que o Docker está instalado no seu sistema. Você pode baixá-lo em [docker.com](https://www.docker.com/get-started).
- **Docker Compose** (opcional): Necessário se você optar por usar o `docker-compose.yml`.

Verifique se o Docker está funcionando:
```bash
docker --version