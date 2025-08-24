# API Documentation Generator

This project is a full-stack web application designed to automatically generate API documentation from Python source code. It is a powerful tool that helps developers streamline the documentation process by extracting function and class information directly from docstrings.

<p align="center">
  <img src="path/to/your/screenshot.png" alt="A screenshot of the API Documentation Generator" width="600">
</p>

## Features

- **Code Parsing**: The backend, built with **Python** and **Flask**, uses the built-in `ast` module to analyze Python files, intelligently identifying functions, classes, and their respective docstrings.
- **Structured Data**: The extracted information, including function names, parameters, and docstring text, is organized into a clean **JSON object** for easy transmission between the backend and frontend.
- **User Interface**: The frontend, developed with **Vue.js** and **Vite**, provides a simple and intuitive interface where users can upload a zipped folder of Python files, and the application dynamically renders the JSON data into a clean, readable documentation page.

## Technologies Used

### Backend
* **Python**: The core language for the backend logic.
* **Flask**: A lightweight web framework used to create the API.
* **ast**: Python's built-in module for parsing abstract syntax trees.

### Frontend
* **Vue.js**: A progressive JavaScript framework for building user interfaces.
* **Vite**: A build tool that provides a fast development environment.
* **Axios**: A promise-based HTTP client for making API requests.

## How to Run Locally

### Prerequisites
Make sure you have **Python 3.x** and **Node.js** installed on your system.

### Backend Setup
1.  Navigate to the `backend` folder in your terminal.
    ```bash
    cd backend
    ```
2.  Create and activate a virtual environment.
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```
3.  Install the required Python packages.
    ```bash
    pip install Flask Flask-CORS
    ```
4.  Run the Flask development server.
    ```bash
    python app.py
    ```
    The backend will run on `http://127.0.0.1:5000`.

### Frontend Setup
1.  Open a new terminal and navigate to the `api-docs-frontend` folder.
    ```bash
    cd ../api-docs-frontend
    ```
2.  Install the Node.js packages.
    ```bash
    npm install
    ```
3.  Run the development server.
    ```bash
    npm run dev
    ```
    The frontend will run on `http://localhost:5173`.

### Usage
-   With both servers running, open your web browser and navigate to `http://localhost:5173`.
-   Upload a `.zip` file containing Python code with functions and docstrings.
-   The generated documentation will be displayed on the page.