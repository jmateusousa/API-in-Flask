# API-in-Flask:
Simple API in Flask

#Run in terminal:

python api.py

# To run in the background in linux:

python api.py & or nohup python api.py

Acesse http://localhost:5000/

# Consuming the API with Curl -> Available methods:

-- GET example:

curl http://localhost:5000/1

-- POST example:

curl http://localhost:5000/ -d "data=test" -X POST 

-- PUT example:

curl http://localhost:5000/1 -d "data=test" -X PUT

-- DELETE example

curl http://localhost:5000/1  -X DELETE

doubts? contato.matthewd@gmail.com
