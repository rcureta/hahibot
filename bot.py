import socket
import config

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "hahibot"

def send_message(message):
    s.send(bytes("PRIVMSG #vahrei :" + message + "\r\n", "UTF-8"))

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + config.PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #vahrei \r\n", "UTF-8"))


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print(username + ": " + message)
        if message:
            send_message("Welcome to my stream, " + username + ". ᕦʕಠᴥಠʔᕤ ")
