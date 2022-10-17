import socket
from threading import Thread

 
clientes = [] #array pra armazenar o nome dos clientes
host = 'localhost' #ip 
port = 50000 #porta 

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # socket do servidor
    try:
        server.bind((host,port)) #abre conexao utilizando o ip e a porta informada
        server.listen() # modo de escuta #metodo blocnante
        print('aguardando conexao\n')
    except:
       return print('nao possivel iniciar servidor')
   
    while True:
        cliente, endereco = server.accept() #aceitar conexao 
        clientes.append(cliente) #adiciona o nome do cliente no array
        print('conectado em',endereco)#imprime endereço do cliente
        
        Thread(target=recv_msg, args=[cliente]).start()# inicia a thread pra RECEBER as mesagens vinda do cliente

def env_dados(conexao): 
    while True:
        conexao.sendall(str.encode(input("mensagem:")))#enviar mensagem do servidor pro cliente
        print("")

def recv_msg(cliente):
    while True:
        try:
            msg = cliente.recv(1024) #recebe a mensagem do cliente
            broadCast(msg,cliente) #envia mensagem para todos os outros cliente menos pra quem enviou 
        except:
            deleteCliente(cliente) #deleta o cliente do array
            break

def broadCast(msg, cliente):
    for client in clientes: #percorrer o array de clientes
        if client != cliente: #se for diferente do cliente que enviou a mensagem e enviado
            try:
                client.send(msg) #envi mensagem
            except:
                deleteCliente(client)#deleta cliente do array

def deleteCliente(cliente):
    clientes.remove(cliente)#deleta cliente do array
    
            


    

main()




