orders = {}

def save_order(user_id, food):
    if user_id not in orders:
        orders[user_id] = []
    orders[user_id].append(food)

def recommend(user_id):
    if user_id not in orders:
        return "Paneer Butter Masala"
    last = orders[user_id][-1].lower()
    if "biryani" in last:
        return "Chicken Tikka"
    if "paneer" in last:
        return "Shahi Kofta"
    return "Butter Naan"