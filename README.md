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
