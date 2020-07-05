from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from root.Constant import *

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['MONGO_DBNAME'] = dbOnline
app.config["MONGO_URI"] = urlOnline
# (breakpoint())
con = PyMongo(app)
db = con.db.students

@app.route('/')
def index():
    return 'Home'


@app.route('/get')
def get():
    return 'get'

@app.route('/signin', methods=['POST'])
def signin():
    getId = request.args.get("stu_id", "", str)
    getPass = request.args.get("stu_password", "", str)

    # getId = request.form.get("stu_id", "", str)
    # getPass = request.form.get("stu_password", "", str)

    data = db.find_one({"stu_id": getId, "stu_password": getPass}, {"_id": 0})
    if data == None:
        return jsonify({"status": "unsuccessful"})
    elif data["actavition"] == False:
        return jsonify({"status": "An Active Account"})
    else:
        data["status"] = "successful"
        return jsonify(data)
# @app.route('/active', methods=['GET'])
# def acive():
#     getID = request.args.get("stu_id", "", str)
#     # getPass = request.args.get("stu_password", "", str)
#     # getEmail = request.args.get("email", "", str)
#
#     data = db.find_one({"stu_id": getID}, {"_id": 0})
#     if data == None:
#         return jsonify({"status": "Unsuccessful ID"})
#
#     elif data["actavition"] == True:
#         return jsonify({"status": "already activied"})
#
#     else:
#         db.update_one({"stu_id":getID})
#         return data
#     # else:
#     #     db.update_one({{"stu_id": getID,
#     #                     "$set":
#     #                         {
#     #                             "stu_password": getPass,
#     #                             "email": getEmail,
#     #                             "actavition": True}}})
#     #     return jsonify("ok")


if __name__ == '__main__':
    app.run()