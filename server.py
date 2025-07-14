from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# List of fake unicorn stories
unicorn_stories = [
    "Once upon a time, a sleepy unicorn floated on a cloud made of marshmallows and dreamed of rainbows.",
    "A purple unicorn danced in the moonlight while the stars giggled above.",
    "The unicorn tiptoed through the stardust fields to wish the moon a good night.",
    "A baby unicorn curled up in a petal-soft nest and snored glittery dreams.",
    "Every night, the unicorn sprinkled dream-dust over the forest to keep the animals happy.",
    "A magical unicorn sailed across the sky on a jellybean boat, spreading bedtime hugs.",
    "One gentle unicorn whispered lullabies to help clouds fall asleep.",
]

@app.route("/story")
def generate_story():
    story = random.choice(unicorn_stories)  # Pick a random story
    return jsonify({"story": story})

if __name__ == "__main__":
    app.run(debug=True)
