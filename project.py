def main():
    author = Author()
    hospital = Hospital()
    ailments_set = set()
    specializations_dict = {}

    # Author Login
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if not author.login(username, password):
        print("Invalid credentials. Access denied.")
        return

  
      