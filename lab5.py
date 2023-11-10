#Lab5
import socket

def serversideGetPlaySocket():
    ssocket = socket.socket()
    ssocket.bind(('localhost',55555))
    ssocket.listen(3)
    print ("waiting for client to connect")


def clientsideGetPlaySocket(host):


def gameRules(player, opponent):
    if player == opponent:
        return "draw"
    if player == "rock" and opponent == "scissor":
        return "win"
    if player == "paper" and opponent == "rock":
        return "win"
    if player == "scissor" and opponent == "paper":
        return "win"
    else:
        return "lose"