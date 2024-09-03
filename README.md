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
