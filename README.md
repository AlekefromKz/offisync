# Offisync README

## TODOs 

In case I had more resources, I would do the following things:
1. Add a schema generator, probably OpenAPI that would generate a schema on a `/api/schema` endpoint
2. Add UI for that, Swagger UI 
3. Add tests for the open-meteo integration 
4. I would try to find a python package for the open-meteo service and use it instead
5. Improve logging 
6. Add CI-CD 
7. Maybe add internationalization and localization if needed for end users

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

- Docker
- Docker-compose

### Installation

Clone the repository:

```bash
git clone git@github.com:AlekefromKz/offisync.git
cd offisync
```

Run the setup command to build Docker images:

```bash
make setup
```

Start the Docker containers:

```bash
make docker
```

Create a Django superuser:

```bash
make createsuperuser
```

Populate cities data (Note: This process might take some time and may fail due to timeout issues. If it fails, simply
press Ctrl + C and proceed with the next step):

```bash
make populate_cities
```

Load initial data for the models:

```bash
make load_initial_data
```

### Using the API

Before using the API, you need to create an API key in the Django admin panel.

1. Go to the Django admin panel (http://127.0.0.1:8000/admin/) (use the credential that you set for the superuser).
2. Create a new API key.

To use the endpoints make sure to add the created API key to the header as follows:

```bash
curl --location 'http://127.0.0.1:8000/api/employees' \
--header 'Authorization: Api-Key <created-api-key>'
```

Here are the endpoints you can access:

1. Get all offices: http://127.0.0.1:8000/api/offices/
2. Get employees of a specific office (replace 5 with the desired office
   ID): http://127.0.0.1:8000/api/offices/5/employees/
3. Get all employees: http://127.0.0.1:8000/api/employees/
