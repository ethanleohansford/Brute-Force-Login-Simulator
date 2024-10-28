import time

# Hardcoded credentials for the simulation
TARGET_USERNAME = "admin"
TARGET_PASSWORD = "supersecret"  # Change this to simulate different "correct" passwords

def load_passwords(filename):
    """Load passwords from a file and return them as a list."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def brute_force_login(username, password_list):
    """Simulate a brute-force attack by trying each password in the list."""
    print(f"Attempting brute-force on username '{username}'...")
    for attempt, password in enumerate(password_list, start=1):
        print(f"Attempt {attempt}: Trying password '{password}'")
        time.sleep(0.5)  # Simulate delay for each attempt

        if username == TARGET_USERNAME and password == TARGET_PASSWORD:
            print(f"[SUCCESS] Login successful with password '{password}' after {attempt} attempts!")
            return True

    print("[FAILED] Brute-force attack failed. Password not found.")
    return False

def main():
    # Load passwords from the file
    password_file = "passwords.txt"
    password_list = load_passwords(password_file)
    
    # Attempt brute-force on the username "admin"
    brute_force_login("admin", password_list)

if __name__ == "__main__":
    main()
