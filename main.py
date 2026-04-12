import os
import socket
from flask import Flask, render_template

app = Flask(__name__)

# --- THE CHECKER (Finds out why it's failing) ---
def pre_flight_check():
    print("\n--- TEAM AVOSITY SYSTEM CHECK ---")
    
    # 1. Check Port
    port = 10649
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
        print(f"❌ ERROR: Port {port} is ALREADY in use. Stop the server and start again.")
    else:
        print(f"✅ Port {port} is free and ready.")
    sock.close()

    # 2. Check Folders
    if not os.path.exists('templates'):
        print("❌ ERROR: 'templates' folder is missing! Create it in File Manager.")
    elif not os.path.exists('templates/index.html'):
        print("❌ ERROR: 'index.html' is NOT inside the templates folder.")
    else:
        print("✅ HTML Templates found.")

    # 3. Check Images
    if not os.path.exists('static/logo.png'):
        print("⚠️ WARNING: logo.png not found in /static. Site will look broken.")
    
    print("---------------------------------\n")

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"System Error: {str(e)}"

if __name__ == "__main__":
    # Render assigns a port automatically, this code finds it
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)