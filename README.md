# 💬 GHOST CHAT 💀

Anonymous TempChat

A secure, real-time chat application where messages:

---

## 🚀 Features

🚀 Auto-send on Enter key

🧹 Max 20 messages (oldest deleted first)

🌌 No accounts, logs, or persistence

🔥 Host anywhere (Heroku, Render, Raspberry Pi)

🛡️ Bleach-sanitized inputs against XSS

---

## 🛠 Requirements

Install the required Python packages using pip:

```bash
pip install flask flask_socketio eventlet bleach
```
On linux (ubuntu) I'm using:
```bash
apt install python3-flask python3-flask-socketio python3-eventlet python3-bleach
```

## 🧪 How to Run (Locally)
### Save the server.py file.

### Run the server:

```bash
python server.py
```
### Open your browser and go to:
http://localhost:5000

## 🌐 Access from Other Devices (Local Network)
If you're running this on a computer and want to connect from your phone or another device on the same Wi-Fi network, do the following:

### Find your computer's local IP address:

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

```cpp
http://YOUR_LOCAL_IP:5000
```
Example:

```cpp
http://192.168.1.12:5000
```
✅ Make sure your firewall allows incoming connections on port 5000.

# For more fun 🤡

## 🧅 Hosting on the Tor Network (Onion Address)
To make Ghost Chat accessible over Tor, follow these steps:

### 📦 1. Install Tor (if not already installed)
```bash
sudo apt install tor
```
### ⚙️ 2. Configure the hidden service
```bash
echo "HiddenServiceDir /var/lib/tor/voidchat\nHiddenServicePort 80 127.0.0.1:5000" | sudo tee -a /etc/tor/torrc > /dev/null
```

### 🔄 3. Restart Tor
```bash
sudo systemctl restart tor
```
### 🌐 4. Get your onion address
```bash
sudo cat /var/lib/tor/voidchat/hostname
```
You'll see something like:
```bash
abc123def456ghi789.onion
```

Now anyone using Tor Browser can visit:
```bash
http://abc123def456ghi789.onion
```

🧠 Make sure your Flask server is still running and listening on 127.0.0.1:5000.

You can change the port and maximum number of messages from the first lines of code.
