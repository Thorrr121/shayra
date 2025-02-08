from flask import Flask, render_template, request

app = Flask(__name__)

birthday_messages = [
    "Happy Birthday! May your day be filled with love and laughter!",
    "Wishing you a day filled with happiness and a year filled with joy!",
    "Happy Birthday! Hope you have a fantastic celebration!",
    "May this year bring you endless happiness and success. Happy Birthday!",
]

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Birthday Wishes</title>
        <style>
            body { 
                font-family: Arial, sans-serif;
                text-align: center;
                background: url('/static/birthday_bg.jpg') no-repeat center center fixed;
                background-size: cover;
                color: white;
            }
            .container {
                width: 50%;
                margin: auto;
                background: rgba(0, 0, 0, 0.7);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
                margin-top: 50px;
            }
            img { width: 100%; max-width: 300px; border-radius: 10px; margin-top: 20px; }
            input, textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            button {
                padding: 10px 20px;
                background: #28a745;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover { background: #218838; }

            /* Text Animation */
            .animated-text {
                animation: bounce 1.5s infinite;
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="animated-text">🎉 Send a Birthday Wish! 🎂</h1>
            <img src="/static/birthday_cake.png" alt="Birthday Cake">
            <form action="/wish" method="post">
                <label for="name">Recipient's Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="message">Your Message (optional):</label>
                <textarea id="message" name="message"></textarea>

                <button type="submit">Send Wish</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route("/wish", methods=["POST"])
def wish():
    import random
    name = request.form.get("name")
    message = request.form.get("message") or random.choice(birthday_messages)

    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Birthday Wish</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background: url('/static/birthday_bg.jpg') no-repeat center center fixed;
                background-size: cover;
                color: white;
            }}
            .container {{
                width: 50%;
                margin: auto;
                background: rgba(0, 0, 0, 0.7);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
                margin-top: 50px;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{ background: #0056b3; }}

            /* Confetti Animation */
            @keyframes confetti {{
                0% {{ transform: translateY(0) rotate(0); opacity: 1; }}
                100% {{ transform: translateY(100vh) rotate(720deg); opacity: 0; }}
            }}
            .confetti {{
                position: absolute;
                width: 10px;
                height: 10px;
                background: #FFD700;
                animation: confetti 3s linear infinite;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Happy Birthday, {name}! 🎂</h1>
            <p>{message}</p>
            <a href="/">Send Another Wish</a>
        </div>
        <script>
            function createConfetti() {{
                for (let i = 0; i < 100; i++) {{
                    let confetti = document.createElement("div");
                    confetti.classList.add("confetti");
                    confetti.style.left = Math.random() * 100 + "vw";
                    confetti.style.animationDuration = Math.random() * 3 + 2 + "s";
                    document.body.appendChild(confetti);
                    setTimeout(() => confetti.remove(), 5000);
                }}
            }}
            createConfetti();
        </script>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)