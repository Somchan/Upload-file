To install the required dependencies, use the following command:


pip install -r Pip_Install.txt

Configuration
Make the following configurations before running the application:

Update the JavaScript files in the "JS" directory to replace http://localhost:8000 with the IP address of your machine. This ensures proper communication between the frontend and the FastAPI server.
javascript

// Example: Change from
const response = await fetch("http://localhost:8000/get");
// to
const response = await fetch("http://192.168.100.63:8000/get");

