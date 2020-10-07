import re
import socket

'''
This script was written as part of Hernan Razo's application to the open
software engineer position at Sav.com on 10/6/20. Email hernanrazo@gmail.com for any
other inquiries about this script or Hernan's application.


Challenge:
Without using any prebuilt APIs, Packages, SDKs or examples found on Stack
Overflow, how can you get a domain name's expiration date using Python?
'''

#get socket connection and return domain information
def get_domain_info(domain_name):

    server = 'whois.internic.net'
    chunks = []

    #establish connection to server
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((server, 43))

    except OSError:
        print('Error connecting to server')

    #send domain to server
    conn.send(str.encode(domain_name))

    #return information as binary object
    chunk = conn.recv(1024)
    chunks.append(chunk)

    return b''.join(chunks)


def main():

    #ask user to type the domain in question onto terminal
    domain_input = input('Type in domain in question:\n')

    #dissect the given domain by removing protocol and www.
    domain_input = domain_input.replace('http://', '')
    domain_input = domain_input.replace('www.', '')
    domain_input = domain_input + '\r\n'

    #call function to grab data for given domain
    data = get_domain_info(domain_input).decode('utf-8')

    #filter out only the expiration date
    expiry_date = re.search(r'Registry Expiry Date: (.*?)\r\n', data).group(1)
    
    #print result onto terminal
    print('Registry Expiry Date: ', expiry_date)


if __name__ == "__main__":
    main()
