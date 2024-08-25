import socket
import sys
args = sys.argv
import base64
import threading
Name = input("WELCOME IM XCAGO TOOL CAN I KMOW YOUR NAME ??")

# Main keys
encoded_pass1 = "Sk9JTiBGT1IgT1RIRVIgVE9PTFMgLS0gQFhfQ0FHTw=="
encoded_pass2 = "TUFERSBCWSAtLSBAQTZfTlM="
encoded_pass3 = "Q1JJRFRTIC0tIEBYX0NBR08="

# decode the key
def decode_password(encoded_password):
    return base64.b64decode(encoded_password).decode()

# reback the key from base64
decoded_pass1 = decode_password(encoded_pass1)
decoded_pass2 = decode_password(encoded_pass2)  # login system by @a6_ns  using base 64 to convert keys to hard type
decoded_pass3 = decode_password(encoded_pass3)

# Cheack the input and keys
login = input("ENTER THE FIRST PASSWORD: ")
Pass2 = input("ENTER THE 2st PASSWORD: ")
Pass3 = input("ENTER THE 3st PASSWORD:")
# ---
if login == decoded_pass1 and Pass2 == decoded_pass2 and Pass3 == decoded_pass3:  # if all keys right == do anything:)   اسف بس الانجليزي بتاعي مش احسن حاجه
    print("DAM IT UR IN WELCOM", Name)
while login != decoded_pass1:
        print(Name, "THE 1st PASSWORD WRONG ! PLS DM @A6_NS") 
        login = input("ENTER THE FIRST PASSWORD: ")
while Pass2 != decoded_pass2:
        print(Name, "THE 2st PASSWORD WRONG ! PLS DM @A6_NS")
        Pass2 = input("ENTER THE 2st PASSWORD: ")
while Pass3 != decoded_pass3:
            print(Name, "THE 3st PASSWORD WRONG ! PLS DM @A6_NS")
            Pass3 = input("ENTER THE 3st PASSWORD:")

def ddos_tool():
    target_host = input("IP OR LINK: ")
    target_port = int(input("ENTER THE PORT TO ATTACK FROM IT: "))

    ip_address = socket.gethostbyname(target_host)

    # صنع الـ SOCKET من AF الاصدار الرابع TO V6 = AF_INET6
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # توصيل الـ CLIENT
        client.connect((ip_address, target_port))

        # إرسال 
        request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
        client.send(request.encode())

        # استلام 
        response = client.recv(4096)

        print("DONE CONNECT:")
        print(response.decode())
    except Exception as e:
        print(f"SORRY I CANT CONNECT WITH THIS LINK :( : {e}")

def port_scanner():
    Prt1 = input("FROM PORT: ")
    Prt2 = input("TO PORT: ")
    WebSite = input("LINK: ")

    for port in range(int(Prt1), int(Prt2)):
        try:
        #FROM SOCK IMPORT SOCKET  
        #AF_INET = V4   #AF_INET6 = V6
    #TCP PORT = socket.SOCK_STREAM
        # {}socket.getservbyport(port) to get the type of port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((WebSite, port))
            print(f"{port} [OPEN] {socket.getservbyport(port)}")
        except:
            print(f"{port} [CLOSE]")

def main():
    print(Name, "CHOOSE A TOOL :--BY @X_CAGO--:")
    choice = input("1- DDOS ATTACK\n2- PORT SCANNER\n")

    if choice == '1':
        ddos_tool()
    elif choice == '2':
        port_scanner()
    else:
        print("WTF", Name, "THERE IS NO CHOICE LIKE THIS")

if __name__ == "__main__":
    main()
















#