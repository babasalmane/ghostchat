# 💬 GHOST CHAT 💀

A minimal, real-time anonymous chat server with a spooky retro aesthetic, built using **Flask** and **Socket.IO**.

---

## 🚀 Features

- Real-time chat using WebSockets (via Flask-SocketIO)
- Terminal-style UI (green-on-black, Courier font)
- HTML-stripped input (sanitized with `bleach`)
- Lightweight, in-memory message buffer (up to 20 messages)
- Auto-syncs all connected users with latest chat history
- "Nuclear wipe" auto-clears messages on server shutdown

---

## 🛠 Requirements

Install the required Python packages using pip:

```bash
pip install flask flask_socketio eventlet bleach
```

##🧪 How to Run (Locally)
###1_Save the server.py file.

###2_Run the server:

```bash
python server.py
```
###3_Open your browser and go to:
http://localhost:5000

##🌐 Access from Other Devices (Local Network)
If you're running this on a computer and want to connect from your phone or another device on the same Wi-Fi network, do the following:

###1_Find your computer's local IP address:

On macOS/Linux:
```bash
ip addr | grep inet
```
On Windows:

```cmd
ipconfig
```

Look for something like 192.168.x.x or 10.x.x.x.

On the other device, open a browser and visit:
```bash
http://YOUR_LOCAL_IP:5000
```
