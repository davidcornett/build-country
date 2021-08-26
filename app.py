from flask import Flask
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    return "map test!"

# Listener

if __name__ == "__main__":
    # bind to PORT if defined, otherwise use default
    port = int(os.environ.get('PORT', 6205))
    app.run(port=port) 
