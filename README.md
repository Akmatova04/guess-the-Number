🎯 Django "Guess the Number" Game
This is a simple web-based Guess the Number game built with the Django framework. The player tries to guess a randomly generated number between 1 and 100.

🎯 Purpose
This project is designed to demonstrate core Django concepts such as:

Views 🧩

Templates 🖼️

URLs 🌐

Sessions 🧠

Forms 📝

Perfect for beginners who want hands-on experience with Django basics!

🛠️ Technologies Used
🐍 Python 3

🌐 Django 5.x

⚙️ Setup Instructions
1️⃣ Create & Activate a Virtual Environment:
bash
Копировать
Редактировать
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
# venv\Scripts\activate  # For Windows
2️⃣ Install Django:
bash
Копировать
Редактировать
pip install django
3️⃣ Apply Migrations:
bash
Копировать
Редактировать
python3 manage.py migrate
4️⃣ Run the Development Server:
bash
Копировать
Редактировать
python3 manage.py runserver
5️⃣ Open in Your Browser:
Navigate to 👉 http://127.0.0.1:8000/game/play/

🧠 Game Logic
The server randomly picks a number between 1 and 100 🎲

The user submits their guess using a form ✍️

The server responds with:

“Too High” 🔼

“Too Low” 🔽

or “Correct!” ✅

The number of attempts is tracked 📊

Once the number is guessed correctly, the app displays how many tries it took and offers a chance to play again 🔁

🚀 Future Improvements
📦 Add a requirements.txt file

🎨 Improve the design with CSS/styling

⛔ Limit the number of attempts

🏆 Add a leaderboard using a database
![IMAGE 2025-05-16 10:12:43](https://github.com/user-attachments/assets/873f102d-6b7c-49a2-b509-48740a60d5c7)
![IMAGE 2025-05-16 10:12:50](https://github.com/user-attachments/assets/0b23534f-271e-48a2-9a07-d4ab2f6898da)
