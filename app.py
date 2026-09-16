from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

DAIRY = {
    "name": "Puja Dairy Udhyog",
    "address": "Dhangadhi, Sudurpaschim, Nepal",
    "phone": "9766100969",
    "email": "tekraj618@gmail.com",
    "hours": "5:30 AM – 10:30 PM",
    "trust": "5+ Years of Trusted Dairy Service"
}

PRODUCTS = [
    {"id": 1, "name": "Fresh Milk", "image": "https://images.unsplash.com/photo-1563636619-e9143da7973b?auto=format&fit=crop&w=800&q=85", "description": "Fresh, wholesome milk for your family's everyday needs."},
    {"id": 2, "name": "Curd (Dahi)", "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=800&q=85", "description": "Thick, creamy dahi with a naturally delicious taste."},
    {"id": 3, "name": "Buttermilk (Mahi)", "image": "https://images.unsplash.com/photo-1628088062854-d1870b4553da?auto=format&fit=crop&w=800&q=85", "description": "A light, refreshing traditional drink for any time of day."},
    {"id": 4, "name": "Ghee", "image": "https://images.unsplash.com/photo-1639109426354-5f6c7c9d1e22?auto=format&fit=crop&w=800&q=85", "description": "Rich, golden ghee with a comforting homemade aroma."},
    {"id": 5, "name": "Butter", "image": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=800&q=85", "description": "Smooth, fresh butter for breakfast, cooking and baking."},
    {"id": 6, "name": "Cake", "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=85", "description": "Freshly prepared cakes for celebrations and sweet moments."},
    {"id": 7, "name": "Paneer", "image": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=800&q=85", "description": "Soft, fresh paneer ready for your favourite family dishes."},
    {"id": 8, "name": "Other Dairy Products", "image": "https://images.unsplash.com/photo-1628088062854-d1870b4553da?auto=format&fit=crop&w=800&q=85", "description": "Ask us about our other fresh dairy selections."}
]

messages = []

@app.route("/")
def home():
    return render_template("index.html", dairy=DAIRY, products=PRODUCTS)

@app.route("/api/products")
def products():
    return jsonify(PRODUCTS)

@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or request.form

    name = str(data.get("name", "")).strip()
    phone = str(data.get("phone", "")).strip()
    product = str(data.get("product", "")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not phone or not message:
        return jsonify({"success": False, "message": "Please fill in your name, phone number and message."}), 400

    inquiry = {
        "name": name,
        "phone": phone,
        "product": product,
        "message": message,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    messages.append(inquiry)

    print("\n--- NEW INQUIRY ---")
    print(inquiry)

    return jsonify({"success": True, "message": "Thank you! Your inquiry has been received."})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
