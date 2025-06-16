from flask import Flask, request, jsonify
import model
import notify

app = Flask(__name__)

@app.route('/')
def home():
    return "🍽️ Welcome to FoodieNotify - Personalized Food Recommendation Engine!"

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    user_id = data.get('user_id')
    food = data.get('food')

    if not user_id or not food:
        return jsonify({"error": "user_id and food are required"}), 400

    model.save_order(user_id, food)
    suggestion = model.recommend(user_id)
    notify.send_push(user_id, suggestion)

    return jsonify({
        "message": f"Order for {food} placed successfully!",
        "suggestion": f"Based on your taste, try: {suggestion}"
    })

if __name__ == '__main__':
    app.run(debug=True)