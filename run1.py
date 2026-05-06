from client import *
from dbclient import *
from constRPC import *
from time import sleep
import pickle

def main():
    c1 = Client(HOSTC1, PORTC1)
    
    dbC1 = DBClient(HOSTS, PORTS)
    dbC1.create()
    dbC1.appendData('Client 1')

    sleep(3)  # espera client2 subir

    print("Enviando referência para Client 2...")
    c1.sendTo(HOSTC2, PORTC2, dbC1)

if __name__ == "__main__":
    main()