import requests

url = "http://127.0.0.1:8000/api/workers/projects/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMTcwMDUzLCJpYXQiOjE3MzIxNDAwNTMsImp0aSI6ImI5OTVlZGVhNDc4YjQzYWE4YTE5YjMxM2JjNTQ2OGI1IiwidXNlcl9pZCI6MX0.PRrw5ZGES74FVtxc_deswzi0bjQom5uEELmaaJ4o2UI"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Список проектов:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)
