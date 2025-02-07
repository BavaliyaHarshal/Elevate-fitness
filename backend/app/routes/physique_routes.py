from flask import Blueprint, request, jsonify
from app.utils.database import get_db_connection
import google.generativeai as genai
import os

physique_routes = Blueprint("physique_routes", __name__)

# Load API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

@physique_routes.route("/physique", methods=["POST"])
def generate_physique():
    data = request.json
    user_id = data.get("user_id")
    height = data.get("height")
    weight = data.get("weight")
    age = data.get("age")
    gender = data.get("gender")
    diseases = data.get("diseases", "")

    if not all([user_id, height, weight, age, gender]):
        return jsonify({"error": "Missing required fields"}), 400

    # Structured prompt for short, clear output
    ai_prompt = f"""
    Create a SHORT & well-structured fitness plan for a {age}-year-old {gender} 
    with height {height} cm, weight {weight} kg, and diseases: {diseases}.

    **FORMAT:**
    Diet Plan:
    - Breakfast: (1-2 items)
    - Lunch: (1-2 items)
    - Dinner: (1-2 items)
    - Snacks: (1-2 items)

    Exercise Plan:
    - Cardio: (Duration & type)
    - Strength: (Exercise names)
    - Flexibility: (Exercise names)
    
    Keep it concise and easy to follow.
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(ai_prompt)
        plan = response.text.strip()  # Extract clean text

        # Store in database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO physique (user_id, height, weight, age, gender, diseases, diet_plan, exercise_plan, schedule)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
        """, (user_id, height, weight, age, gender, diseases, plan, plan))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Plan generated successfully!", "plan": plan}), 201
    
    except Exception as e:
        return jsonify({"error": f"Gemini AI error: {str(e)}"}), 500
