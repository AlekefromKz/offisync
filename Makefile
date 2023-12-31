# Makefile

.PHONY: createsuperuser populate_cities setup docker logs load_initial_data env

createsuperuser:
	@echo "Creating a django superuser..."
	@docker-compose run --rm django python manage.py createsuperuser

populate_cities:
	@echo "Populating cities using django cities light..."
	@docker-compose run --rm django python manage.py cities_light

setup: env
	@echo -e "$(CYAN)Creating Docker images$(COFF)"
	@docker-compose build

	@echo -e "SETUP SUCCEEDED"
	@echo -e "Run 'make docker' to start Django development server..."

docker:
	@docker-compose down
	@docker-compose build
	@docker-compose up -d
	@echo -e "Project is up and running. Run 'make logs' to see logs..."

logs:
	@docker-compose logs -f

load_initial_data:
	@echo -e "Loading data for Office, Employee, and WorkHistory models..."
	@docker-compose run --rm django ./manage.py loaddata employees/fixtures/initial.json

env:
	@cp .env.sample .env
	@echo "Created .env file from .env.sample"