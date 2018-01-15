if __name__ == "__main__":
    with open("/etc/passwd") as passwd:
        print(passwd.fileno())
    passwd.closed
    try:
        print(passwd.fileno())
    except ValueError:
        print("The file already has closed")
    
