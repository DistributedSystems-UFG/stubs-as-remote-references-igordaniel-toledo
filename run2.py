from client import *
from dbclient import *
from constRPC import *
import pickle

def main():
    c2 = Client(HOSTC2, PORTC2)

    print("Aguardando referência...")
    data = c2.recvAny()

    dbC2 = pickle.loads(data)

    dbC2.appendData('Client 2')
    print("Valor final da lista:")
    print(dbC2.getValue())

    c2.sendTo(HOSTS, PORTS, [STOP])

if __name__ == "__main__":
    main()