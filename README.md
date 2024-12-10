### 3155 Final Project Team
* Ed C.
* Mauricio M. 

### Enter venv
* Create a venv in the root folder for yourself
* `.\.venv\Scripts\activate`

### Installing necessary packages
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
* `pip install pydantic[email]`

### For MySQL Workbench
* Set config in api/dependencies/config.py
* By Default uses a schema called 3155_final

### Run the server:
* `uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### User stories and Product Backlog
[https://docs.google.com/spreadsheets/d/1rJIA9EKUSKb20ZAuNn8S3p-3-UhjlFRUdrbDqw6Rtwg/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1rJIA9EKUSKb20ZAuNn8S3p-3-UhjlFRUdrbDqw6Rtwg/edit?usp=sharing)

### Demo Video
[https://www.youtube.com/watch?v=py-WTQrRKZE](https://www.youtube.com/watch?v=py-WTQrRKZE)