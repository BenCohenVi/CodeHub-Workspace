-`0
+`0`from socket import *
-`1
+`1`import thread
-`2
+`2`import threading
-`3
+`3`import time
-`4
+`4`import sys
-`5
+`5`
-`6
+`6`
-`7
+`7`def get_open_port():
-`8
+`8`    #a function that finds an open port and writes it in a file
-`9
+`9`    global password
-`10
+`10`    s = socket(AF_INET, SOCK_STREAM)
-`11
+`11`    s.bind(("", 0))
-`12
+`12`    s.listen(1)
-`13
+`13`    port = s.getsockname() [1]
-`14
+`14`    s.close()
-`15
+`15`    save_port = open("Details.txt", "w")
-`16
+`16`    save_port.write(str(port)+","+password)
-`17
+`17`    save_port.close()
-`18
+`18`    return port
-`19
+`19`
-`20
+`20`
-`21
+`21`def read_file():
-`22
+`22`    #a function that reads the requested file
-`23
+`23`    clientsock.send("Please enter the file you want to open (With path): ")
-`24
+`24`    data = clientsock.recv(BUFSIZ)
-`25
+`25`    try:
-`26
+`26`        reader = open(data)    #opens the file 
-`27
+`27`        return "The File Contains: " + reader.read()   #reading the whole file and returning it
-`28
+`28`    except:
-`29
+`29`        return "Can't open the file, going back for the echo function"
-`30
+`30`
-`31
+`31`
-`32
+`32`def set_timer():
-`33
+`33`    #a function that sets a timer according to the client request
-`34
+`34`    clientsock.send("How much time in seconds? ")
-`35
+`35`    data = clientsock.recv(BUFSIZ)
-`36
+`36`    try:
-`37
+`37`        time.sleep(int(data))    #makes the program waiting for "data" seconds
-`38
+`38`        return "Timer Done"
-`39
+`39`    except:
-`40
+`40`        return "Invalid Input, Going back to the echo function"
-`41
+`41`
-`42
+`42`
-`43
+`43`def Change_Password(clientsock, addr, f):
-`44
+`44`    #a function that changes the server's password
-`45
+`45`    clientsock.send("Which new password do you want?")
-`46
+`46`    password = clientsock.recv(BUFSIZ)
-`47
+`47`    f.seek(0)    #changing the cursor to the start
-`48
+`48`    f.truncate()    #erasing everything
-`49
+`49`    f.write(str(PORT)+","+password)
+`50`    f.close()
+`51`    f = open("Details.txt", "a+")
+`52`    password = f.read().split(",")[1]
+`53`    return "password changed", password
+`54`
+`55`
+`56`def stop_run():
+`57`    #a function that creates a fake client connection to close the server
+`58`    try:
+`59`        HOST = '127.0.0.1'
+`60`        PORT = int(open("Details.txt", "r").read().split(",")[0])     #getting the port from the file
+`61`        ADDR = (HOST, PORT)
+`62`        tcpCliSock = socket(AF_INET, SOCK_STREAM)    #(fake)creating a connection for the serve
+`63`        tcpCliSock.connect(ADDR)    #(fake) connecting into the server
+`64`        print "server closed"
+`65`    except:
+`66`        print "cant fake connection"
+`67`
+`68`
+`69`def handler(clientsock, serversock, addr, f):
+`70`    #the main function that handles the clients
+`71`    global is_open
+`72`    global password
+`73`    try:
+`74`        with clients_lock:
+`75`            clients.add(clientsock)
+`76`        while is_open == True:
+`77`            data = clientsock.recv(BUFSIZ)    #gets information from the clients
+`78`            print data
+`79`            if data[:4]=="read":
+`80`                data = read_file()
+`81`            if data == "Set a Timer":
+`82`                data = set_timer()
+`83`            if data == "Change Password":
+`84`                data, password = Change_Password(clientsock, addr, f)
+`85`            if data == "exit":
+`86`                break
+`87`            if data == password:
+`88`                print "Server is Closing"
+`89`                with clients_lock:
+`90`                    for c in clients:
+`91`                        c.sendall("The Server is Closing")
+`92`                clientsock.close()
+`93`                is_open = False
+`94`                serversock.close()
+`95`                stop_run()
+`96`                thread.exit()
+`97`                raise SystemExit    #killing all threads
+`98`            clientsock.send(data)    #sends the information for the client
+`99`        print password
+`100`        print "ending communication with",addr
+`101`        clientsock.send("Thank you for using my Program!")
+`102`        clientsock.close()
+`103`    except:
+`104`        clientsock.close()
+`105`        thread.exit()
+`106`
+`107`
+`108`is_open = Truet
+`109`password = open("Details.txt", "r").read().split(",")[1]    #getting the password out of the file
+`110`BUFSIZ = 1024
+`111`HOST = "127.0.0.1"
+`112`PORT = get_open_port()
+`113`ADDR = (HOST, PORT)    #creates an address for the server
+`114`serversock = socket(AF_INET, SOCK_STREAM)    #creates a socket for the server
+`115`serversock.bind(ADDR)    #connecting the server into his adress
+`116`serversock.listen(2)    
+`117`f = open("Details.txt", "r+")
+`118`print "Type This into the Client's PORT = "+str(PORT)
+`119`clients = set()
+`120`clients_lock = threading.Lock()
+`121`
+`122`
+`123`while 1:
+`124`    try:
+`125`        print 'waiting for connection...'
+`126`        clientsock, addr = serversock.accept()
+`127`        print '...connected from:', addr
+`128`        if is_open == True:
+`129`            thread.start_new_thread(handler, (clientsock, serversock, addr, f))    #creates a new thread to handle to client
+`130`    except:
+`131`        break1
+`132`
