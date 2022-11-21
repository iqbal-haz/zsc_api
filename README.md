# zsc-api

## Installation

1. Clone repository
2. Create virutal environment <br>
Python setup <br>
`python3 -m venv env` <br>
Virtualenv <br>
`virtualenv env`
3. Activate virtual environment <br>
Windows <br>
`env\Scripts\activate` <br>
MacOS / Linux <br>
`source env/bin/activate`
4. Install requirements <br>
`pip install -r requirements.txt`
5. Run the app <br>
`flask run`

## Endpoint(s)

`POST /`

```
curl --location --request POST 'http://127.0.0.1:8000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sequence":"saya suka kamu",
    "candidates": ["positif","negatif"]
}
```