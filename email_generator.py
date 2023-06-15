"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: MIT
Description: A Red Teaming tool focused on profiling the target.
"""

class EmailGenerator:
    def __init__(self, firstname_lastname_list, domain):
        self.firstname_lastname_list = firstname_lastname_list
        self.domain = domain

    # Generate a list of possible email formats for each user
    def generate_emails(self, users):
        emails = []
        for firstname, lastname in users:
            emails.append(f'{firstname}.{lastname}@{self.domain}')
            emails.append(f'{lastname}.{firstname}@{self.domain}')
            emails.append(f'{firstname}_{lastname}@{self.domain}')
            emails.append(f'{lastname}_{firstname}@{self.domain}')
            emails.append(f'{firstname}-{lastname}@{self.domain}')
            emails.append(f'{lastname}-{firstname}@{self.domain}')
            emails.append(f'{firstname}{lastname}@{self.domain}')
            emails.append(f'{lastname}{firstname}@{self.domain}')
            emails.append(f'{firstname[0]}{lastname}@{self.domain}')
            emails.append(f'{lastname[0]}{firstname}@{self.domain}')
            emails.append(f'{firstname}@{self.domain}')
            emails.append(f'{lastname}@{self.domain}')
        return emails
    

    def process_name_list(self, output_handle):
        users = []
        with open(self.firstname_lastname_list, "r") as name_file:
            for line in name_file:
                firstname, lastname = line.strip().split()
                users.append((firstname, lastname))

        emails = self.generate_emails(users)
        for email in emails:
            if output_handle:
                output_handle.write(email + "\n")
                output_handle.flush()
