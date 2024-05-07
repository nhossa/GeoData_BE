# lightning-fast ASGI server implementation, often used for running asynchronous web applications in Python.
import uvicorn

# checks if the script is being run directly as the main program, When a Python script is executed, the special variable __name__ is set to "__main__"
if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)