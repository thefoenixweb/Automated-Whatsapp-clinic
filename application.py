from datetime import datetime

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://john:Father@cluster0.b1lrdrw.mongodb.net/?retryWrites=true&w=majority")
db = cluster["medix"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    res = MessagingResponse()
    user = users.find_one({"number": number})
    if bool(user) == False:
       msg = res.message(
            "Hi, thank you for contacting *Medix*.\nChoose from the options below: \n\n*Type*\n\n 1️⃣ To *contact* us \n 2️⃣ To *order* medicine \n 3️⃣ To know our *operating hours* \n 4️⃣ To get our *address*")
     
       users.insert_one({"number": number, "status": "main", "messages": []})

    elif user["status"] == "main":


        try:
            option = int(text)
        except:
            res.message("Please enter a valid response")
            return str(res)

        if option == 1:
            res.message(
                "You can contact us through phone or e-mail.\n\n*Phone*: 0731234537 \n*E-mail* : contact@medix.co.za")


        elif option == 2:
            res.message("You have entered *ordering mode*.")
            users.update_one({"number": number}, {"$set": {"status": "ordering"}})
            res.message(
                "You can select from the following list of medicines to order: \n\n 1️⃣ ZIAGEN \n2️⃣ TRIZIVIR \n 3️⃣ EPZICOM \n 4️⃣ TRIUMEQ \n 5️⃣ TYMLOS \n 6️⃣XEGLYZE \n 7️⃣ KIVEXA \n 8️⃣ Lamivudine \n 0️⃣ BACK")


        elif option == 3:
            res.message("We operate from *9 AM to 6 PM*")

        elif option == 4:
            res.message("Our store is at *29 SwallowTail, Little Falls*")

        else:

            res.message("Please enter a valid response")

    elif user["status"] == "ordering":

        try:

            option = int(text)

        except:

            res.message("Please enter a valid response")

            return str(res)

        if option == 0:

            users.update_one(

                {"number": number}, {"$set": {"status": "main"}})

            res.message("You can choose from one of the options below: "

                        "\n\n*Type*\n\n 1️⃣ To *contact* us \n 2️⃣ To *order* medicine \n 3️⃣ To know our *working hours* \n 4️⃣ "

                        "To get our *address*")

        elif 1 <= option <= 8:

            medicines = ["ZIAGEN", "TRIZIVIR", "EPZICOM",

                     "TRIUMEQ", "TYMLOS", "XEGLYZE", "KIVEXA", "Lamivudine"]

            selected = medicines[option - 1]

            users.update_one(

                {"number": number}, {"$set": {"status": "address"}})

            users.update_one(

                {"number": number}, {"$set": {"item": selected}})

            res.message("Excellent choice 😉")

            res.message("Please enter your address to confirm the order")

        else:

            res.message("Please enter a valid response")

    elif user["status"] == "address":

        selected = user["item"]

        res.message("Thanks for shopping with us 😊")

        res.message(f"Your order for *{selected}* has been received and will be delivered within an hour")

        orders.insert_one({"number": number, "item": selected, "address": text, "order_time": datetime.now()})

        users.update_one(

            {"number": number}, {"$set": {"status": "ordered"}})

    elif user["status"] == "ordered":

        res.message("Hi, thanks for contacting again.\nYou can choose from one of the options below: "

                    "\n\n*Type*\n\n 1️⃣ To *contact* us \n 2️⃣ To *order* medicine \n 3️⃣ To know our *working hours* \n 4️⃣ "

                    "To get our *address*")

        users.update_one(

            {"number": number}, {"$set": {"status": "main"}})

    users.update_one({"number": number}, {"$push": {"messages": {"text": text, "date": datetime.now()}}})

    return str(res)


if __name__ == "__main__":
    app.run()
