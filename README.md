# FastAPI Application with MongoDB

## Project Structure

- `src/` - Contains the application source code.
- `src/configuration/` - Contains db/settings configuration files.
- `src/tests/` - Contains test cases for the API endpoints.
- `Dockerfile` - Dockerfile for building the application image.
- `docker-compose.yml` - Docker Compose configuration file.

## Getting Started

### Setting Up the Environment

1. **Clone the Repository**

   ```bash
   git clone  https://github.com/ajay776/FastApi_With_Mongo.git
   cd FastApi_With_Mongo
   ```

2. **Build and Start Containers**
   Use Docker Compose to build and start the containers

```bash
docker-compose up --build
```

3. **Running the Application**
   After the containers are up and running, you can access the FastAPI application at below endpoint and can check the swagger docs.

```bash
http://localhost:8000/docs
```

### Running Tests

1. **Run Tests in a Docker Container**

To run testcases inside docker container you have to first get the container id and then you can run iterative mode on that id
eg.

```bash
docker exec -it <conainer_id> sh
```

once you enter the interactive mode you can simply navigate inside _`tests`_ directory and run `pytest` it will run all testcases.
