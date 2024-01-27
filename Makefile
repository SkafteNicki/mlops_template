

# Create a new test project
create_test_project:
	mkdir TEST-PROJECT && cd TEST-PROJECT 
	cookiecutter https://github.com/LukasLeindals/repo_template
	cd ..


# Clean up the project

clean:
	rm -rf TEST-PROJECT