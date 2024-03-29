# fastapi-backend-boilerplate

This is basic backend service boilerplate of FastAPI with Postgres.

### Requirements

- Python 3.6+
- Postgres
- Redis


### Setup

```shell
# Create a virtual enviroment

python3 -m venv env

source env/bin/activate


# Install dependencies

pip install -r requirements.txt



# also run pre-commit install when contributing to codebase [optional]
pre-commit install

# Done
```


### Run
After all setup is complete. If you wish to run directly to host system

- Copy `.sample.env` -> `.env`
- Run `./run.sh`

If you wish to run from `docker-compose` file
- Copy `.sample.docker.env` -> `.env``
- `docker-compose up -d`

Navigate to http://localhost:8000/redoc

-----------------------
Feel free to create PR or use this boilerplate for reference


### Contact
- Email: rajatgupta310198@gmail.com or rajat310198@outlook.com
