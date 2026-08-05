# MindX DevOps Lab

MindX DevOps Lab is an incremental backend and DevOps learning repository. It builds a production-oriented FastAPI service step by step, starting with application structure and containerization and progressing through database infrastructure and backend foundations.

## Project Overview

The repository is organized by learning module. Each module captures a specific stage of the system’s evolution while preserving a clear path toward a scalable backend.

The current reference application is located in `module-05-Backend-Architect`. It contains the architecture established in Module 05 and the PostgreSQL integration completed in Module 06.

## Features

- Modular FastAPI application structure.
- Environment-based application configuration.
- API routing with a health endpoint.
- Automatic Swagger UI and OpenAPI documentation.
- Dockerized FastAPI application.
- PostgreSQL service managed through Docker Compose.
- Persistent PostgreSQL Docker volume.
- SQLAlchemy 2.x engine and declarative base.
- SQLAlchemy session factory and FastAPI database dependency.
- Database connectivity verification without application models or migrations.

## Project Architecture

The current backend follows a layered structure:

- `app/api/`: HTTP routers and endpoint definitions.
- `app/core/`: Shared application configuration.
- `app/db/`: SQLAlchemy engine, session factory, declarative base, and database dependency.
- `app/models/`: Reserved boundary for future SQLAlchemy models.
- `app/schemas/`: Reserved boundary for future request and response schemas.
- `app/services/`: Reserved boundary for future business services.
- `app/middleware/`: Reserved boundary for future middleware.
- `app/exceptions/`: Reserved boundary for future application exceptions.
- `app/utils/`: Reserved boundary for shared utilities.
- `app/main.py`: FastAPI application entry point and router composition root.

## Technology Stack

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic Settings
- SQLAlchemy 2.x
- Psycopg 3
- PostgreSQL 16
- Docker
- Docker Compose

## Completed Modules

### Module 03 — FastAPI Fundamentals

Introduced the initial FastAPI application and development dependencies.

### Module 04 — Docker Compose

Introduced containerization and Docker Compose-based application execution.

### Module 05 — Backend Architecture

Established the scalable application layout, configuration layer, API routing layer, application entry point, health endpoint, Dockerfile, and Compose foundation.

### Module 06 — PostgreSQL Integration

Added PostgreSQL to Docker Compose, persistent storage, SQLAlchemy initialization, session management, environment-based database configuration, and database connectivity verification.

## Upcoming Modules

Future modules will extend the existing architecture incrementally with domain-specific backend capabilities, while keeping each concern isolated in its appropriate application layer.

## Folder Structure

```text
MindX-DevOps-Lab/
├── .gitignore
├── LICENSE
├── README.md
├── module-03-fastapi/
├── module-04-docker-compose/
├── module-05-Backend-Architect/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── exceptions/
│   │   ├── middleware/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── .dockerignore
│   ├── .env
│   ├── compose.yaml
│   ├── Dockerfile
│   ├── README.md
│   └── requirements.txt
└── module-05-postgresql/
```

## Getting Started

The current reference application is run from `module-05-Backend-Architect`.

### Prerequisites

- Git
- Docker Desktop with Docker Compose
- PowerShell, Bash, or another terminal
- At least 2 GB of available Docker memory

### Installation

After cloning the repository from its GitHub repository page, enter the current application directory:

```powershell
cd MindX-DevOps-Lab\module-05-Backend-Architect
```

Create or update the local `.env` file with the application and PostgreSQL settings required by the Compose configuration. Never commit real credentials.

### Docker Commands

Build and start the application and PostgreSQL services:

```powershell
docker compose up --build -d
```

List service status:

```powershell
docker compose ps
```

View service logs:

```powershell
docker compose logs -f
```

Stop the services while preserving the PostgreSQL volume:

```powershell
docker compose stop
```

Stop and remove the containers and network:

```powershell
docker compose down
```

The named PostgreSQL volume is preserved by `docker compose down` unless volumes are explicitly removed.

### Running the Application

After the services are healthy, the API is available at:

```text
http://localhost:8000
```

Check the health endpoint:

```powershell
Invoke-WebRequest http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "MindX DevOps Lab",
  "environment": "development"
}
```

### API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

OpenAPI JSON:

```text
http://localhost:8000/openapi.json
```

## Development Workflow

1. Work inside the module currently being developed.
2. Keep configuration in environment files and avoid committing secrets.
3. Make one focused architectural change at a time.
4. Rebuild the Docker image after dependency or container changes.
5. Verify Compose configuration before starting services.
6. Check service health, application logs, `/health`, and Swagger after changes.
7. Review `git status` before committing.
8. Commit changes with a concise, descriptive message.

## Future Roadmap

- Extend the database layer with domain-specific persistence capabilities.
- Add validated request and response contracts.
- Introduce business services behind the API layer.
- Add secure application concerns as their dedicated modules are reached.
- Improve operational visibility and deployment workflows incrementally.

## Contributing

1. Create a focused branch for your change.
2. Keep changes limited to the relevant module or repository concern.
3. Do not commit secrets, local environment files, generated artifacts, or IDE metadata.
4. Verify the affected services locally with Docker Compose.
5. Review the final diff and Git status before opening a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
