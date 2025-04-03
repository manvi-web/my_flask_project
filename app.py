from flask import Flask, render_template, request
import os

app = Flask(__name__)

field_map = {
    "Student Registration": [
        ["Name", "Text Input"],
        ["Email", "Email Input"],
        ["Date of Birth", "Date Picker"],
        ["Gender", "Radio Button"],
        ["Class", "Dropdown"],
        ["Address", "Text Area"],
        ["Phone Number", "Number Input"],
        ["Profile Picture", "File Upload"]
    ],
    "Job Application": [
        ["Name", "Text Input"],
        ["Resume", "File Upload"],
        ["Experience", "Text Area"]
    ],
    "Contact Form": [
        ["Name", "Text Input"],
        ["Email", "Email Input"],
        ["Message", "Text Area"]
    ]
}

@app.route('/')
def home():
    return render_template('my_subfolder/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    formname = request.form.get('formname', '').strip()  # Remove leading/trailing spaces
    print("Received Form Name:", formname)  # Debugging

    # Ensure we match keys exactly (case-sensitive)
    predicted_fields = field_map.get(formname, [["No predictions available", ""]])

    print("Predicted Fields:", predicted_fields)  # Debugging

    return render_template('my_subfolder/index.html', fields=predicted_fields, formname=formname)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses environment variable PORT
    print(f"Starting Flask API on port {port}...")
    app.run(host="0.0.0.0", port=port)
