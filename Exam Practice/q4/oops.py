class ServerManagement:
    def __init__(self, file_name='os_records.txt'):
        self.file_name = file_name

    def add_os_details(self, os_type, user_name, issued_date):
        os_type = os_type.lower()
      
        if os_type in ["ubuntu", "centos"]:
            try:
                # use "a" for append instead of "w" for overwrite
                with open(self.file_name, "a") as file:  
                    record = f"OS Type: {os_type}\nUser Name: {user_name}\nIssued Date: {issued_date}\n\n"
                    file.write(record)
            except IOError as e:
                print(f"Error writing to file: {e}")
        else:
            print("Please contact the IT team for Ubuntu/CentOS installation.")

    def read_server_entries(self):
        try:
            with open(self.file_name, "r") as file:
                print(file.read())
        except IOError as e:
            print(f"Error reading file: {e}")


def main():
    os_type = input("Please enter OS Type (Ubuntu/CentOS): ")
    user_name = input("Enter user name: ")
    issued_date = input("Enter your issued date: ")

    sm = ServerManagement()
    sm.add_os_details(os_type, user_name, issued_date)
    sm.read_server_entries()


if __name__ == "__main__":
    main()