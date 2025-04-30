from bottle import get, post, run, request, response
import uuid

# Global list of persons
persons = [
    {"name": "Emma", "id": 2, "uuid": str(uuid.uuid4())},
    {"name": "Lena", "id": 3, "uuid": str(uuid.uuid4())}
]

# Logic function to create a person
def create_person(data):
    data["uuid"] = str(uuid.uuid4())
    persons.append(data)
    return data

# HTTP POST handler
@post('/person')
def create_person_handler():
    data = request.json
    new_person = create_person(data)
    response.status = 201
    return new_person

# HTTP GET handler
@get('/person')
def list_persons():
    response.status = 200
    return {"persons": persons}

# Run server only if run directly
if __name__ == '__main__':
    run(host="0.0.0.0", port=8080, debug=True, reload=True)
