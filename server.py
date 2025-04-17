from flask import Flask, render_template_string  
from flask_socketio import SocketIO, emit  
import time  
import bleach  
import hashlib  
import signal  
import os  

app = Flask(__name__)  
app.config['SECRET_KEY'] = os.urandom(24).hex()  
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")  

messages = [] 
max_messages = 20
Port=5000

def nuclear_wipe(signum, frame):  
    global messages  
    messages.clear()  
    print("☢️ MESSAGES PURGED ☢️")  
    os._exit(0)  

signal.signal(signal.SIGINT, nuclear_wipe)  
signal.signal(signal.SIGTERM, nuclear_wipe)  

@app.route('/')  
def void_gate():  
    return render_template_string('''  
    <!DOCTYPE html>  
    <html>  
    <head>  
        <meta charset="UTF-8">  
        <title>GHOST CHAT</title>  
        <style>  
            body {
                background: black;
                color: #0f0;
                font-family: 'Courier New';
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            #messages {
                border: 1px solid #0f0;
                height: 400px;
                margin: 20px 0;
                padding: 10px;
                overflow-y: scroll; /* Enable vertical scrolling */
            }
            input {
                background: #000;
                color: #0f0;
                height: 30px;
                border: 1px solid #0f0;
                width: 100%;
            }
            .timestamp { color: #888; }  
        </style>  
    </head>  
    <body>  
        <h1>💬 GHOST CHAT CLOUD 💀</h1>  
        <div id="messages"></div>  
        <input type="text" id="msgInput" placeholder="Type + Enter to send">  

        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.2/socket.io.min.js"></script>  
        <script>  
            const socket = io()  
            const input = document.getElementById('msgInput')  
            const messagesDiv = document.getElementById('messages')  

            // Auto-focus and Enter handler  
            input.focus()  
            input.addEventListener('keypress', (e) => {  
                if (e.key === 'Enter') {  
                    e.preventDefault()  
                    if (input.value.trim()) {  
                        socket.emit('speak', input.value)  
                        input.value = ''  
                    }  
                }  
            })  

            // Full sync handler  
            socket.on('full_sync', (allMessages) => {  
                messagesDiv.innerHTML = ''  
                allMessages.forEach(msg => {  
                    const div = document.createElement('div')  
                    div.innerHTML = `<pre><span style="color: white;">[${msg.time}]</span> ${msg.text}</pre><hr>`  
                    messagesDiv.appendChild(div)  
                })  
                messagesDiv.scrollTop = messagesDiv.scrollHeight  
            })  
        </script>  
    </body>  
    </html>  
    ''')  

@socketio.on('speak')  
def handle(raw):  
    clean = bleach.clean(raw, tags=[], attributes={}, strip=True)[:256]  
    msg = {  
        'text': clean,  
        'time': time.strftime("%H:%M:%S"),  
        'id': hashlib.sha3_256(f"{time.time()}{os.urandom(8)}".encode()).hexdigest()[:12]  
    }  

    # Atomic message rotation  
    global messages  
    messages.append(msg)  
    if len(messages) > max_messages:  
        messages.pop(0)  
    
    # Force global sync  
    emit('full_sync', messages, broadcast=True)  

@socketio.on('connect')  
def sync():  
    emit('full_sync', messages[-max_messages:])  

if __name__ == '__main__':  
    socketio.run(app, host='0.0.0.0', port= Port)
