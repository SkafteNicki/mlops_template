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

# Define the target for copying and renaming Python files, excluding __init__.py files
create_test_files: SOURCE_DIR = "{{ cookiecutter.repo_name }}/{{ cookiecutter.project_name }}"
create_test_files: DEST_DIR = "\{\{\ cookiecutter.repo_name\ \}\}/tests"
create_test_files:
	# Create the destination directory
	@mkdir -p $(DEST_DIR)

	# Find directories in the source directory and prepend "test_" to their names
	@find $(SOURCE_DIR) -type d ! -wholename $(SOURCE_DIR) -exec sh -c 'new_dir="$${0#$(SOURCE_DIR)/}"; mkdir -p "$(DEST_DIR)/test_$$new_dir"; echo "Created $(DEST_DIR)/test_$$new_dir"' {} \;
	
	# Add __init__.py files to the newly created directories
	@find $(SOURCE_DIR) -type d ! -wholename $(SOURCE_DIR) -exec sh -c 'new_dir="$${0#$(SOURCE_DIR)/}"; touch "$(DEST_DIR)/test_$$new_dir/__init__.py"; echo "Created $(DEST_DIR)/test_$$new_dir/__init__.py"' {} \;
	
	# Find Python files in the source directory, prepend "test_" to their names,
	# and create necessary directory structure in the destination directory
	@find $(SOURCE_DIR) -type f -name "*.py" ! -name "__init__.py" -exec sh -c ' \
		new_file="$${0#$(SOURCE_DIR)/}"; \
		filename="$$(basename "$$new_file")"; \
		dir_path="$$(dirname "$$new_file")"; \
		new_dir_path="$$dir_path"; \
		if [ "$$new_dir_path" != "." ]; then \
			new_dir_path="$$new_dir_path/"; \
		fi; \
		mkdir -p "$(DEST_DIR)/test_$$new_dir_path"; \
		touch "$(DEST_DIR)/test_$$new_dir_path/test_$$filename"; \
		echo "Created $(DEST_DIR)/test_$$new_dir_path/test_$$filename"' {} \;

# Clean test files
clean_test_files:
	rm -rf "{{ cookiecutter.repo_name }}/tests"

# Clean up the project
clean:
	rm -rf TEST-PROJECT