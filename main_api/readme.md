# Video API

This README provides instructions on how to run the `api.py` file for the Video API.

## Prerequisites

Before running the API, make sure you have the following installed:

- Python (3.7 or later)
- pip (Python package installer)

## Installation

1. Clone this repository or download the `api.py` file.

2. Install the required dependencies: ```pip install -r api_requirements.txt```

Note: You may need to install additional dependencies depending on the contents of your `api.py` file.

## Running the API

To run the API, use the following command:
```uvicorn api:app --reload --host 0.0.0.0 --port 8000```

This command does the following:

- `uvicorn`: The ASGI server we're using to run our FastAPI application.
- `video_api:app`: This tells uvicorn to look for the `app` variable in the `video_api.py` file. Make sure your file is named `video_api.py` and that it contains a FastAPI application instance named `app`.
- `--reload`: This flag enables auto-reloading, so the server will restart when you make changes to the code.
- `--host 0.0.0.0`: This makes the server accessible from any IP address.
- `--port 8000`: This sets the port number to 8000.

After running this command, your API should be accessible at `http://localhost:8000`.


## Stopping the API

To stop the API, press `CTRL+C` in the terminal where it's running.

## Troubleshooting

If you encounter any issues, please check the following:

1. Ensure all dependencies are correctly installed.
2. Verify that the `api.py` file exists and contains a FastAPI application instance named `app`.
3. Check if the port 8000 is already in use by another application.