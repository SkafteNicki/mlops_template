.PHONY: *
.DEFAULT_GOAL := hello

# Say hello
hello:
	@echo "This is a cookiecutter template for a Python project. Please use \`make <target>\` to run the commands."

# Install requirements
requirements:
	python -m pip install -r requirements.txt

# Create a new test project
create_test_project: DIR = TEST-PROJECT
create_test_project: clean
	mkdir $(DIR) && cd $(DIR)
	cookiecutter . --no-input --output-dir $(DIR)
	cd ..


# Clean up the project
clean:
	rm -rf TEST-PROJECT