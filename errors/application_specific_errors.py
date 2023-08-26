from flask import Flask, jsonify

class AgeException(Exception):
    def __init__(self, code, message = 'Default age is not valid'):
        super().__init__(message)
        self.code = code

app = Flask(__name__)

@app.route('/<int:age>',methods = ['GET','POST'])
def age_validator(age):
    try:
        if age < 18:
            raise AgeException(message= 'Invalid age', code=33) 
    except AgeException as e:
        return jsonify({'message' : e.args[0], 'status code' : 422}),422
    return 'age'


if __name__ == '__main__':
    app.run(debug = True)
