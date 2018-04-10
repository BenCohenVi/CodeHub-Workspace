9-data = input_entry.get()
10-input_entry.delete(0, END)
11-listbox.insert(END, ">" + data)
12-print "works"
13-if not data or data == "exit":
15-tcpCliSock.send(data)
16-output = tcpCliSock.recv(BUFSIZ)
17-listbox.insert(END, output)
18-listbox.see(END)
21-server_ip = raw_input("Please enter the IP address of the server: ")
24-HOST = str(server_ip)
25-PORT = int(free_port)
26-BUFSIZ = 1024
27-ADDR = (HOST, PORT)
28-tcpCliSock = socket(AF_INET, SOCK_STREAM)
29-tcpCliSock.connect(ADDR)
30-print "connected"
34-root.geometry("500x350")
36-frame = Frame(root)
38-scrollbar.pack(in_=frame, side=RIGHT, fill=Y)
39-listbox = Listbox(root, yscrollcommand=scrollbar.set)
40-listbox.pack(in_=frame)
41-scrollbar.config(command=listbox.yview)
42-frame.grid(row=3, column=0, sticky=W)
43-input_entry = Entry(root)
45-send_data_btn = Button(root, text="SEND DATA", command=print_input)
46-send_data_btn.grid(row=0, column=1)
5+#a function that closes the GUI and stop running
10+try:
11+data = input_entry.get()
12+input_entry.delete(0, END)    #clears the entry box
13+input_output_list.insert(END, ">" + data)    #adding the input into the listbox
14+input_output_list.itemconfig(END, bg='#4382b3')
15+tcpCliSock.send(data)
16+output = tcpCliSock.recv(BUFSIZ)
17+if output[:19] == "The File Contains: ":
18+reading_listbox.insert(END,output[19:])    #adding the recived information into a diffrent listbox
19+reading_listbox.itemconfig(END, bg='#4382b3')
20+output = "File added to the Read List"
21+input_output_list.insert(END, output)
22+input_output_list.itemconfig(END, bg='#ffd94a')
23+input_output_list.see(END)    #allways seeing the end of the list
24+if data == "exit":
25+print output
26+close_program()
27+if output == "The Server is Closing":
28+print output
29+close_program()
30+except:
31+print "Server is closed"
37+connected = False
38+while not connected:
39+try:
40+HOST = '127.0.0.1'
41+PORT = int(free_port)
42+BUFSIZ = 1024
43+ADDR = (HOST, PORT)
44+tcpCliSock = socket(AF_INET, SOCK_STREAM)    #creating a socket for the client
45+tcpCliSock.connect(ADDR)    #connecting into the server
46+print "connected"
47+connected = True
48+except:
49+print "Can't connect to server, please try again"
50+free_port = raw_input("Please aenter the Port of the server: ")
53+root.configure(background = '#22496a')
55+root.geometry("1150x500")
58+reading_input_output_frame = Frame(root)
59+scrollbar1 = Scrollbar(root, orient=VERTICAL)
60+scrollbar1.pack(in_=reading_input_output_frame, side=RIGHT, fill=Y)
61+reading_listbox = Listbox(root, width=40, height = 15,font='Ariel 14' ,bg='#1e2933',yscrollcommand=scrollbar1.set)
62+reading_listbox.pack(in_=reading_input_output_frame)
63+scrollbar1.config(command=reading_listbox.yview)
64+reading_input_output_frame.grid(row=3, column=1, sticky=E, padx=20)
66+input_output_frame = Frame(root)
68+scrollbar.pack(in_=input_output_frame, side=RIGHT, fill=Y)
69+input_output_list = Listbox(root, width=50, height=15, font='Ariel 16' ,bg='#1e2933',yscrollcommand=scrollbar.set)
70+input_output_list.pack(in_=input_output_frame)
71+scrollbar.config(command=input_output_list.yview)
72+input_output_frame.grid(row=3, column=0, sticky=W)
74+input_entry = Entry(root, font='Ariel 18', fg='#129e13', bg='#1e2933', width = 30)
76+send_data_btn = Button(root, text="SEND DATA", font='Ariel 12', bg='#3776ab', width=12, command=print_input)
77+send_data_btn.grid(row=0, column=1, pady=15, padx=5)
78+reading_listbox.select_set(0)
