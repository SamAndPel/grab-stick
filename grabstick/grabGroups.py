import subprocess


def get_groups():
    groups = str(subprocess.check_output("net localgroup")).split("\\r\\n")[4:-3:]
    return groups


def main():
    return get_groups()

if __name__ == "__main__":
    print(get_groups())
