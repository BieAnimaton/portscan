import socket
import sys

argumento = sys.argv
try:
    endereco = argumento[1]
except:
    print("\033[1;31mFaltam argumentos no comando\033[0;0m")
    sys.exit(1)

portas = [21, 23, 80, 443, 8080]

for portas in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    codigo = cliente.connect_ex((endereco, portas))

    if codigo == 0:
        print portas, " -- \033[1;32mOPENED\033[0;0m"
    else:
        print portas, "-- \033[1;31mCLOSED\033[0;0m"
