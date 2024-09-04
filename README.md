## API Endpoints

### Public Endpoints
These endpoints are accessible to anyone:

- **Health check**: Check the health status of the service.
- **Log in**: Authenticate and obtain a token.
- **Get all companies**: Retrieve a list of all companies.
- **Get company by ID**: Retrieve detailed information about a specific company using its ID.
- **Create user**: Register a new user (with or without specifying `company_id`).

### Private Endpoints
These endpoints are accessible only to authenticated users. 

#### Normal User
A normal user has access to their own information and tasks:

- **Get their own user information**: Retrieve information about their own user account.
- **Update their own user information**: Modify their own user details.
- **Delete their own account**: Remove their own user account from the system.
- **Create their own task**: Add a new task associated with their account.
- **Get their own task information by task ID**: Retrieve details of a specific task using its ID.
- **Get all of their own tasks**: Retrieve a list of all tasks associated with their account.
- **Update their own task**: Modify an existing task associated with their account.
- **Delete their own task**: Remove a task associated with their account.

#### Admin
An admin has elevated privileges and can access or modify information for all users and tasks:

- **Get all users' information**: Retrieve a list of all users and their information.
- **Get any user's information**: Retrieve information for any specific user.
- **Update any user's information**: Modify details for any user.
- **Delete any user's account**: Remove any user's account from the system.
- **Get all tasks' information**: Retrieve a list of all tasks and their details.
- **Get any task's information**: Retrieve details of any specific task.
- **Update any task's information**: Modify details of any task.
- **Delete any task**: Remove any task from the system.

# Sample setup
- Create a virtual environment module in your project.
```bash

# Generate virtual environment
# On Windows
python -m venv venv

# On macOS and Linux
python3 -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install depdendency packages
pip install -r requirements.txt
```

- Configure `.env` file by creating a copy from `.env.sample`
```bash
# Example
ASYNC_DB_ENGINE=postgresql+asyncpg
DB_ENGINE=postgresql
DB_NAME=fastapi_db
DB_USERNAME=tuan
DB_PASSWORD=tuan
DB_HOST=localhost
DB_PORT=5433
ADMIN_DEFAULT_PASSWORD=tuan
JWT_SECRET=2f8d64a98ff91836a2a78884573c402a627d4c120eb9c3213e5d51379bfb46c4
JWT_ALGORITHM=HS256

```
- At `app` directory, run `alembic` migration command. Please make sure your postgres DB is ready and accessible.
```bash
# Migrate to latest revison
alembic upgrade head

# Dowgragde to specific revision
alembic downgrade <revision_number>

# Downgrade to base (revert all revisions)
alembic downgrade base

# Create new revision
alembic revision -m <comment>
```

- Run `uvicorn` web server from `app` directory (`reload` mode is for development purposes)
```bash
uvicorn main:app --reload
```

- Access `http://127.0.0.1:8000/docs` to test the APIs on Swagger-UI:
<img width="931" alt="Screenshot 2024-09-04 093411" src="https://github.com/user-attachments/assets/e37e07e8-7bfe-4348-982e-ab650679e9e8">
<img width="887" alt="Screenshot 2024-09-04 093445" src="https://github.com/user-attachments/assets/665945cd-d57b-4581-b2c7-857b507376fe">


