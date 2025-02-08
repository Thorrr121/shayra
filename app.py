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
                background: #fad0c4;
                color: white;
                padding: 20px;
                overflow: hidden;
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
                position: relative;
                z-index: 2;
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
            .image-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                overflow: hidden;
                z-index: 1;
            }
            .image-container img {
                position: absolute;
                width: 300px;
                height: 300px;
                object-fit: cover;
                border-radius: 10px;
                opacity: 0.8;
                transition: transform 3s ease-in-out;
            }
        </style>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                var images = ["her_background1.jpg", "her_background2.jpg", "her_background3.jpg",
                              "her_background4.jpg", "her_background5.jpg", "her_background6.jpg",
                              "her_background7.jpg", "her_background8.jpg"];
                var container = document.createElement("div");
                container.classList.add("image-container");
                document.body.appendChild(container);
                
                images.forEach((image, index) => {
                    let img = document.createElement("img");
                    img.src = "/static/" + image;
                    img.style.top = Math.random() * 70 + "vh";
                    img.style.left = Math.random() * 70 + "vw";
                    container.appendChild(img);
                });
                
                function shuffleImages() {
                    document.querySelectorAll(".image-container img").forEach(img => {
                        img.style.transform = `translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px)`;
                    });
                }
                setInterval(shuffleImages, 3000);
            });
        </script>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Happy Birthday Princess 🎂</h1>
            ''' + ''.join(f'<div class="quote">{quote}</div>' for quote in birthday_quotes) + '''
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
