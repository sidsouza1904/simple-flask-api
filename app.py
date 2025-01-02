from flask import Flask, request
from data import students


app = Flask(__name__)


@app.route('/students', methods=['GET'])
def get():
    return students

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    return students.get(
        student_id,
        {'error': 'Student not found'}
    )

@app.route('/students', methods=['POST'])
def create():
    id = sorted(students.keys())[-1] + 1
    new_student = {
        'name': request.json['name'],
        'email': request.json['email'],
        'room': request.json['room'],
    }
    students[id] = new_student
    return new_student

@app.route('/students/<int:student_id>', methods=['PUT'])
def update(student_id):
    if student_id in students.keys():
        update_student = {
            'name': request.json['name'],
            'email': request.json['email'],
            'room': request.json['room'],
        }
        students[student_id] = update_student
        return update_student
    else:
        return {'error': 'Student not found'}

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete(student_id):
    if student_id in students.keys():
        del students[student_id]
        return {'data': 'Student deleted successfully.'}
    else:
        return {'error': 'Student not found'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5152, debug=True)