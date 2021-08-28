"""
CP1404/CP5632 Practical
emails program
"""


def main():
    emails = []
    names = []
    email = input("email: ")
    while email != "":
        emails.append(email)
        full_name = get_possible_name_from_email(email)
        names = confirm_name(full_name, names)
        email = input("email: ")
    print()
    combine_and_print_emails_with_names(emails, names)


def get_possible_name_from_email(email):
    full_name = ""
    email_split_by_at = email.split("@")
    name = email_split_by_at[0]
    split_name = name.split(".")
    for name in split_name:
        name = str(name).title()
        full_name += f"{name} "
    return full_name


def confirm_name(full_name, names):
    choice = input(f"Is your name {full_name}(Y/n)").lower()
    while choice != "y" and choice != "" and choice != "n":
        print("invalid choice")
        choice = input(f"Is your name {full_name}(Y/n)").lower()
    if choice == "y" or choice == "":
        names.append(full_name)
    else:
        name = input("Name: ")
        names.append(name)
    return names


def combine_and_print_emails_with_names(emails, names):
    email_name_dict = dict(zip(emails, names))
    for email in email_name_dict:
        print(f"{email_name_dict[email]}({email})")


main()
