import argparse
import os
import itertools
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create email addresses from a file with names and surnames, generate combinations of specified values, and create a profile file.')
    parser.add_argument('-npath', '--names-file', help='Path to the file containing names and surnames.')
    parser.add_argument('-dpath', '--email-domain', help='Email domain, e.g., @microsoft.com')
    parser.add_argument('-pgen', '--values-file', help='Path to the file containing values for combinations.')
    parser.add_argument('-cprofile', '--profile-name', help='Profile name to create a new profile file.')
    return parser.parse_args()

def read_user_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    users = []
    for line in lines:
        if line.strip():
            firstname, lastname = line.strip().split(' ')
            users.append((firstname, lastname))

    return users

def generate_emails(users, domain):
    emails = []
    for firstname, lastname in users:
        emails.append(f'{firstname}.{lastname}{domain}')
        emails.append(f'{lastname}.{firstname}{domain}')
        emails.append(f'{firstname}_{lastname}{domain}')
        emails.append(f'{lastname}_{firstname}{domain}')
        emails.append(f'{firstname}-{lastname}{domain}')
        emails.append(f'{lastname}-{firstname}{domain}')
        emails.append(f'{firstname}{lastname}{domain}')
        emails.append(f'{lastname}{firstname}{domain}')
        emails.append(f'{firstname[0]}{lastname}{domain}')
        emails.append(f'{lastname[0]}{firstname}{domain}')
        emails.append(f'{firstname}{domain}')
        emails.append(f'{lastname}{domain}')
    return emails

def read_params_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    params = []
    for line in lines:
        if line.strip():
            match = re.search(r"=(\s*)'(.+?)'", line.strip())
            if match:
                value = match.group(2)
                params.append(value)
    return params

def generate_combinations(params):
    combinations = list(itertools.permutations(params))
    with open('combinations.txt', 'w') as file:
        for combination in combinations:
            file.write(''.join(combination) + '\n')

def create_profile_file(profile_name):
    file_name = f"{profile_name}_profile"
    with open(file_name, 'w') as file:
        file.write("############################################################################################\n")
        file.write("# ADD VALUES BETWEEN ' ' ON EACH LINE YOU WANT TO USE. VALUES WITHOUT ' ' WILL BE IGNORED. #\n")
        file.write("############################################################################################\n")
        file.write("birth_year=\n")
        file.write("child_name=\n")
        file.write("wife_name=\n")
        file.write("city_name=\n")
        file.write("favorite_month=\n")
        file.write("favorite_season=\n")
        file.write("favorite_day=\n")
        file.write("favorite_food=\n")
        file.write("sports_team=\n")
        file.write("dog_name=\n")
        file.write("cat_name=\n")
        file.write("company_name=\n")

def main():
    args = parse_arguments()

    if args.names_file and args.email_domain:
        users = read_user_file(args.names_file)
        emails = generate_emails(users, args.email_domain)

        for email in emails:
            print(email)

    if args.values_file:
        params = read_params_file(args.values_file)
        generate_combinations(params)

    if args.profile_name:
        create_profile_file(args.profile_name)

if __name__ == '__main__':
    main()