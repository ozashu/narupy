if __name__ == "__main__":
    passwd = open("/etc/passwd")
    print(passwd.fileno())
    passwd.close()
    print(passwd.fileno())
