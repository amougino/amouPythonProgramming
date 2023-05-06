import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', 9999))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client = data
        print(from_client)
#        test1 = str(from_client).split('_')
#        print(len(test1))
#        if len(test1) > 1:
#            if test1[2] == 'coord1y':
#                message_tobesent = '1_'+test1[1]+'_'+test1[3]+'_'
#                conn.send(message_tobesent.encode('utf-8'))
#            if test1[2] == 'coord2y':
#                message_tobesent = '2_'+test1[1]+'_'+test1[3]+'_'
#                conn.send(message_tobesent.encode('utf-8'))
    conn.close()
    print('client disconnected')
