import socket
from getpass import getpass

from actions.ClientFileController import ClientFileController


class ClientThread:
    SERVER = "127.0.0.1"
    PORT = 8080

    def __init__(self):
        self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_connection.connect((ClientThread.SERVER, ClientThread.PORT))
        self.client_data = ClientFileController()

    def run_connection(self):
        while True:
            print("From Server :", self.get_message_from_server())

            respond_to_server = input("I choose (option number):")
            self.send_message_to_server(respond_to_server)
            if respond_to_server == '1':
                print("From Server :", self.get_message_from_server())
                user_login = input("Login: ")
                user_password = input("Password: ")
                self.send_message_to_server(user_login)
                self.send_message_to_server(user_password)
                requested_auth = self.get_message_from_server()
                if requested_auth == '2':
                    break
                else:
                    print(requested_auth)
                    # available options
                    print(self.get_message_from_server())
                    selected_option = input('Select option nr.:')
                    self.send_message_to_server(selected_option)
                    while True:
                        if selected_option == '5':
                            self.closing_connection()
                            break
                        if selected_option == '1':
                            # account balance
                            print(self.get_message_from_server())
                        if selected_option == '2':
                            # ask about money to deposit & show account balance
                            print(self.get_message_from_server())
                            print(self.get_message_from_server())
                            deposit_money = input('Put money: ')
                            # respond
                            self.send_message_to_server(deposit_money)
                            # show account balance
                            print(self.get_message_from_server())
                        if selected_option == '3':
                            # ask about money to withdraw & show account balance
                            print(self.get_message_from_server())
                            print(self.get_message_from_server())
                            withdraw_money = input('Withdraw money: ')
                            # respond to server
                            self.send_message_to_server(withdraw_money)
                        if selected_option == '4':
                            # ask about money to transfer & show account balance
                            print(self.get_message_from_server())
                            print(self.get_message_from_server())
                            transfer_money = -1.00
                            while transfer_money < 0.00:
                                transfer_money = float(input('transfer money (can\'t be nagative): '))
                            # respond to server
                            self.send_message_to_server(transfer_money)
                            # ask about account nr
                            print(self.get_message_from_server())
                            account_number = input('Account number: ')
                            self.send_message_to_server(account_number)
                            print(self.get_message_from_server())

                        self.send_message_to_server('2')
                        self.closing_connection()
            if respond_to_server == '2':
                self.closing_connection()
            else:
                message_from_server = self.get_message_from_server()

    def send_message_to_server(self, message):
        self.server_connection.sendall(bytes(message, 'UTF-8'))

    def get_message_from_server(self):
        received_from_server = self.server_connection.recv(1024)
        return received_from_server.decode()

    def closing_connection(self):
        print('Closing client connection')
        self.server_connection.close()
        exit(0)
