import subprocess


def get_users():
    users = []
    output = str(subprocess.check_output("net user")).split("\\r\\n")[4:-3:]
    for i in output:
        users.extend(i.split("  "))
        # users.append(user.strip() for user in splitup)
    return [x for x in users if x.strip() != ""]

def main():
    return get_users()

if __name__ == "__main__":
    print(get_users())
