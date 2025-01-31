# Flask API Project

This project is a simple Flask-based API that returns JSON-formatted information, including the developer's email, the current timestamp in ISO format, and a GitHub repository link for the project hosted. This task is related to **HNG 12** [Internship](https://hng.tech/hire/python-developers) task 0 for Backend track: <https://hng.tech/hire/python-developers>.


## Features
- Returns a JSON response containing:
  - Developer email
  - Current date and time in ISO 8601 format
  - GitHub repository URL

## Endpoint

### GET /
**URL:** `http://127.0.0.1:5000/`

#### Request
- Method: `GET`
- No request parameters required

#### Response
```json
{
    "email": "poarnold@outlook.com",
    "current_datetime": "2024-01-31T12:34:56.789123",
    "github_url": "https://github.com/poarnold/hng_task_0"
}
```

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- pip (Python package manager)

For Amazon Linux instances, install dependencies using:
```bash
sudo yum install -y python3 python3-pip
```

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/poarnold/hng_task_0.git
   cd hng_task_0
   ```
2. Install required dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python hng_task_0.py
   ```
4. Access the API at `http://127.0.0.1:5000/`

## Nginx Reverse Proxy Configuration
To configure an Nginx reverse proxy for this Flask application, use the following configuration to replace the default server section (or comment them out) in the /etc/nginx/`nginx.conf` file:

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Prefix /;
    }
}
```

### Testing and Restarting Nginx
After adding the configuration file, test the Nginx configuration with:
```bash
sudo nginx -t
```
If the test is successful, restart Nginx to apply the changes:
```bash
sudo systemctl restart nginx
```

## Notes
- Flask automatically runs on port 5000 by default. If needed, modify `app.run()` in the script to specify a different port.
- Ensure your Python environment is correctly set up to avoid dependency conflicts.

## License
This project is open-source and available under the MIT License.

