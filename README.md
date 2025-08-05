# Elevate Fitness

**Elevate Fitness** is a Python-based fitness and wellness web application designed to provide users with customized exercise schedules, diet plans tailored to their body types, and expert guidance.

GitHub Repository: [https://github.com/BavaliyaHarshal/Elevate-fitness](https://github.com/BavaliyaHarshal/Elevate-fitness)

---

## 🚀 Features

- 💪 Personalized exercise routines  
- 🥗 Custom diet plans based on user profile  
- 👩‍⚕️ Expert consultation and fitness tracking  
- 📝 Contact form with email confirmation  
- 📬 Admin panel to view form submissions  
- 🖼️ Posts with comments and real-time replies  
- 🔐 User authentication and session management  

---

## 🛠️ Tech Stack

**Frontend:**

- HTML5, CSS3, Bootstrap
- EJS (Embedded JavaScript Templates)

**Backend:**

- Python (Flask or Django – confirm if needed)
- MongoDB (via PyMongo or ORM)
- Socket.io (if using Node bridge or similar for real-time)

**Other Tools:**

- Git & GitHub
- Email sending (e.g., via SMTP or Flask-Mail)
- Python-dotenv for config management

---

## 📦 Installation

1. **Clone the repository**  

   ```bash
   git clone https://github.com/BavaliyaHarshal/Elevate-fitness
   cd Elevate-fitness

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv

3. **Activate the Virtual Environment**

    On Windows
    ```bash
        venv\Scripts\activate
    ```
    
    On macOS/Linux
    ```bash
        source venv/bin/activate
    ```

5. **Install Project Dependencies**
  ```bash
    pip install -r requirements.txt
  ```

5. **Set Up Environment Variables**

Create a .env file in the root folder of the project with the following keys:
  ```bash
    MONGODB_URI=your_mongodb_connection_string
    EMAIL_USER=your_email
    EMAIL_PASS=your_email_password_or_app_password
    SECRET_KEY=your_secret_key_for_sessions
  ```

6. **Run the Application**
   ```bash
    python run.py
