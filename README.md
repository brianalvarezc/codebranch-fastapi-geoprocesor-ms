# codebranch-fastapi-geoprocesor-ms

## Introduction
This microservice performs coordinate geoprocessing using FastAPI. It calculates the centroid and geographic bounds of a list of points, and is designed to be consumed by other services via HTTP.


## Installation and Deployment
1. Clone the repository.
2. (Recommended) Create and activate a Python virtual environment:
    ```bash
	# Create venv (Windows)
	python -m venv venv
	# Activate venv (Windows)
	venv\Scripts\activate

	# Create venv (Linux/Mac)
	python3 -m venv venv
	# Activate venv (Linux/Mac)
	source venv/bin/activate
	```
	To deactivate the virtual environment:
	```bash
	deactivate
	```

3. Install dependencies inside the virtual environment:
	```bash
	pip install -r requirements.txt
	```
4. Configure the required environment variables (see `.env.example`).
5. Run the service:
	```bash
	uvicorn src.app:app --reload --port {API_PORT}
	```
    If you want the service to be accessible from your local network or other devices, use the following flags:
    ```bash
    uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
    ```
    The `--port` flag should always be used because the port may change according to your `.env` file or environment variable configuration (e.g., `API_PORT`). Adjust the value as needed to match your setup.

**(Alternative) Local deployment using Docker or Podman:**
1. Build the image:
    ```bash
    docker build -t geoprocessor-ms --build-arg PORT=8000 .
    # or with Podman
    podman build -t geoprocessor-ms --build-arg PORT=8000 .
    ```
2. Run the container:
    ```bash
    docker run -d -p 8000:8000 --env PORT=8000 --env-file .env geoprocessor-ms
    # or with Podman
    podman run -d -p 8000:8000 --env PORT=8000 --env-file .env geoprocessor-ms
    ```
    It can be changed the exposed port by modifying the `PORT` build arg and environment variable. Example for port 8080:
    ```bash
    docker build -t geoprocessor-ms --build-arg PORT=8080 .
    docker run -d -p 8080:8080 --env PORT=8080 --env-file .env geoprocessor-ms
    ```
    This works even without changing anything in the .env file or system environment variables—the value is set directly via the build argument and container environment.

    **Security Note:**
    For security, the Dockerfile creates a non-root user with limited permissions, sufficient only for running the application in `/app`. This reduces the risk of privilege escalation or lateral movement attacks inside the container.
	

## Authentication (Optional, deactivated in endpoints)
The microservice uses JWT authentication. To obtain a token, make a request to the login endpoint with your credentials configured in the `.env` file.

**Login example:**
```bash
curl -X POST "http://localhost:8000/auth/login" \
    -H "Content-Type: multipart/form-data" \
    -F "username=<username>" \
    -F "password=<password>"
```
Include the token in the `Authorization` header in your requests:
```
Authorization: Bearer <token>
```

## API Usage

### Process Coordinates
- **Endpoint:** `POST /{API_BASE_PATH}/process`
- **Description:** Receives a list of points and returns the centroid and geographic bounds.
- **Note:** All endpoints are prefixed with `API_BASE_PATH`, which is configured via your `.env` file or environment variables. For example, if `API_BASE_PATH=/api/v1`, the full endpoint will be `POST /api/v1/process`.
- **Request Body:**
    ```json
		{
			"points": [
				{ "lat": 40.712776, "lng": -74.005974 },    // New York, USA
				{ "lat": -33.868820, "lng": 151.209296 },   // Sydney, Australia
				{ "lat": 35.689487, "lng": 139.691711 },    // Tokyo, Japan
				{ "lat": 55.755825, "lng": 37.617298 },     // Moscow, Russia
				{ "lat": -23.550520, "lng": -46.633308 }    // São Paulo, Brazil
			]
		}

- **Response:**
    ```json
    {
        "centroid": {
                "lat": 14.9477496,
                "lng": 41.5758046
        },
        "bounds": {
                "north": 55.755825,
                "south": -33.86882,
                "east": 151.209296,
                "west": -74.005974
        }
    }
    ```

- **Common Errors:**
	- `400 Bad Request`: Invalid body or malformed points.
	- `401 Unauthorized`: Missing or invalid token.

## Models and Validation
- **Point:**
	- `lat` (float): Latitude of the point.
	- `lng` (float): Longitude of the point.
- **ProcessedCoordinatesOut:**
	- `centroid`: Object with latitude and longitude of the centroid.
	- `bounds`: Object with north, south, east, and west values.

## Practical Examples

**Successful request:**
```bash
curl -X POST "http://localhost:8000/process" \
	-H "Authorization: Bearer <token>" \
	-H "Content-Type: application/json" \
	-d '{
    "points": [
        { "lat": 40.712776, "lng": -74.005974 },
        { "lat": -33.868820, "lng": 151.209296 },
        { "lat": 35.689487, "lng": 139.691711 },
        { "lat": 55.755825, "lng": 37.617298 },
        { "lat": -23.550520, "lng": -46.633308 }
    ]
    }'
```


**Error response:**
```json
{
    "detail": "The 'points' field must be present, be a list, and not be empty."
}

{
    "detail": "Not authenticated"
}
```

**Validation error example (incomplete Point):**
```json
{
	"detail": [
		{
			"type": "missing",
			"loc": ["body", "points", 4, "lng"],
			"msg": "Field required",
			"input": {"lat": -23.55052}
		}
	]
}
```
*This is an example; the values and list length may vary.*

**Empty points list error:**
```json
{
	"detail": "Point list cannot be empty."
}
```


