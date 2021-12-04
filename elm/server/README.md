To run the server:

- create an `input` folder in the same directory as the `elm` directory and files named `01.txt` to `25.txt` containing the inputs

- install FastAPI and Uvicorn
```
pip install fastapi
pip install "uvicorn[standard]"
```

- start the server
```
uvicorn main:app
```
