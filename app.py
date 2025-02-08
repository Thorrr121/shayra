from flask import Flask, render_template

app = Flask(__name__)

birthday_quotes = [
    "Happy Birthday, my dear! May your day be as beautiful and special as you are! ❤️",
    "Wishing you a day filled with love, laughter, and all the happiness in the world! 🎂💕",
    "Happy Birthday to the one who makes my heart skip a beat! Hope your day is magical! 💖",
    "On your special day, I just want to remind you how amazing you are. Have a wonderful birthday! 😘🎉"
]

background_images = [
    "her_background1.jpg", "her_background2.jpg", "her_background3.jpg",
    "her_background4.jpg", "her_background5.jpg", "her_background6.jpg",
    "her_background7.jpg", "her_background8.jpg"
]

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Birthday Quotes</title>
        <style>
            body { 
                font-family: 'Poppins', sans-serif;
                text-align: center;
                background-size: cover;
                color: white;
                padding: 20px;
            }
            .container {
                width: 80%;
                max-width: 600px;
                margin: auto;
                background: rgba(0, 0, 0, 0.5);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.5);
                margin-top: 50px;
            }
            h1 {
                font-size: 24px;
                margin-bottom: 15px;
            }
            .quote {
                font-size: 18px;
                margin: 10px 0;
                padding: 10px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 10px;
            }
        </style>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                var images = ["her_background1.jpg", "her_background2.jpg", "her_background3.jpg",
                              "her_background4.jpg", "her_background5.jpg", "her_background6.jpg",
                              "her_background7.jpg", "her_background8.jpg"];
                var randomImage = images[Math.floor(Math.random() * images.length)];
                document.body.style.background = "url('/static/" + randomImage + "') no-repeat center center fixed";
            });
        </script>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Birthday Quotes 🎂</h1>
            ''' + ''.join(f'<div class="quote">{quote}</div>' for quote in birthday_quotes) + '''
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True, port=5001)
