harhacker
=========

### Setup Development

    # Install virtualenv (if not already installed)
    sudo pip install virtualenv

    # Build and install dependencies
    virtualenv deps

    # Active virtualenv
    source deps/bin/activate

    # Install requirements
    pip install -Ur harhacker/requirements/project.txt

### Run Development

    # Active virtualenv
    source deps/bin/activate

    # Start server
    python harhacker/manage.py runserver
