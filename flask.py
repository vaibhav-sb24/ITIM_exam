from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to ITIL exam"

@app.route('/module')
def subjects():
    subject_list = [
        "FCN",
        "COSA",
        "ITIM",
        "DEVOPS",
        "PKI",
        "NDC",
        "SC",
        "CA",
        "PYTHON"
    ]
    return jsonify(subjects=subject_list)

@app.route('/me')
def about_me():
    roll_no = "84177"
    name = "Vaibhav"
    phone_number = "+1234567890"
    return jsonify({"Roll No": roll_no, "Name": name, "Phone Number": phone_number})

if __name__ == '__main__':
    app.run(debug=True)
