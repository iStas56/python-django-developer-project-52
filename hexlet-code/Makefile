MANAGE := poetry run python manage.py

.PHONY: test
test:
	@poetry run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	@poetry install

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	@$(MANAGE) makemigrations

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: runserver
runserver:
	@$(MANAGE) runserver

.PHONY: makemessages
makemessages:
	@$(MANAGE) makemessages -l ru

.PHONY: compilemessages
compilemessages:
	@$(MANAGE) compilemessages
