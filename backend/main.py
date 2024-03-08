from flask import request, jsonify
from config import app, db
from models import Contact
# CRUD app

@app.route("/contacts", methods=["GET"])
def get_contacts():
    # getting all the contacts
    contacts = Contact.query.all()
    # convert them into json
    # x = contacts
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

# CREATE
@app.route("/create", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name and email"}, 400,)
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    # checking if everything is passing and if there are any errors
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

# UPDATE
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
# this is specifying which contact we want to update specifically 
# /update_contact/1 for example
def update_contact(user_id):
    contact = Contact.query.get(user_id) # finding the user with the specific user_id

    if not contact:
        return jsonify({"message": "USer not found"}), 404
    
    data = request.json
    # the line below is saying that we will modify the firstName to be = json(firstName) otherwise leave it as it was
    # basically if we change only one it changes and the rest stay the same 
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated"}), 200

# DELETE
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id) # finding the user with the specific user_id

    if not contact:
        return jsonify({"message": "USer not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    # when we start the app we get the contexts and create all the models created in our db
    with app.app_context():
        db.create_all()
    app.run(debug=True)