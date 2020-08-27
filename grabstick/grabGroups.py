import subprocess

def get_members_of_group(group):
    #returns list of members of specified group
    result = str(subprocess.check_output(f'net localgroup "{group}"'))
    section = result[result.find("Members\\r\\n") + 7:result.find("The command completed successfully."):].split("\\r\\n")
    members = section[3:-1:]
    return [member.strip() for member in members]

def get_groups():
    groups = str(subprocess.check_output("net localgroup")).split("\\r\\n")[4:-3:]
    groups_formatted = [group[1::] for group in groups]
    groupdict = {}
    for group in groups_formatted:
        groupdict[group] = get_members_of_group(group)
    return groupdict


def main():
    return get_groups()
