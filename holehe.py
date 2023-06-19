"""
Title: profiler
Author: Mădălin Dogaru
Discord: techblade.
Date: 25-03-2023
Version: v0.1
License: GPLv3
Description: A Red Teaming tool focused on profiling the target.
#################################
A Holehe wrapper filtering only the valid responses and with added automation so you can use a list of emails from a file.
Full props go to Palenath for an awesome tool: https://github.com/megadose/holehe
"""

import subprocess
import csv
#import time

class EmailProfiler:
    def __init__(self, filename):
        self.filename = filename

    def profile(self):
        # Open file and read lines
        with open(self.filename, 'r') as file:
            emails = file.readlines()

        # For each email in the list
        for email in emails:
            email = email.strip()  # remove leading/trailing whitespace and newlines

            print(f"Results for {email}:")  # Print email before running holehe

            # Run the command and pipe its output to grep
            process1 = subprocess.Popen(['holehe', email], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process2 = subprocess.Popen(['grep', '-F', '[+]'], stdin=process1.stdout, stdout=subprocess.PIPE)
            process1.stdout.close()  # Allow process1 to receive a SIGPIPE if process2 exits

            # Decode the output, split it into lines and filter out lines starting with '100%'
            output = process2.communicate()[0].decode('utf-8')
            lines = output.split('\n')          

            # Define the line to exclude
            exclude_line = "[+] Email used, [-] Email not used, [x] Rate limit, [!] Error"

            # Filter out the excluded line
            lines = [line for line in lines if not line.startswith('100%') and line != exclude_line]

            # Print the remaining lines
            print('\n'.join(lines))

            #time.sleep(5)  # Wait for 5 seconds

class EmailProfilerCSV:
    def __init__(self, filename, csvname):
        self.filename = filename
        self.csvname = csvname

    def profileCSV(self):
        # Open file and read lines
        with open(self.filename, 'r') as file:
            emails = file.readlines()

        # For each email in the list
        results = {}

        for email in emails:
            
            email = email.strip()  # remove leading/trailing whitespace and newlines

            print(f"Results for {email}:")  # Print email before running holehe

            # Run the command and pipe its output to grep
            process1 = subprocess.Popen(['holehe', email], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process2 = subprocess.Popen(['grep', '-F', '[+]'], stdin=process1.stdout, stdout=subprocess.PIPE)
            process1.stdout.close()  # Allow process1 to receive a SIGPIPE if process2 exits

            # Decode the output, split it into lines and filter out lines starting with '100%'
            output = process2.communicate()[0].decode('utf-8')
            lines = output.split('\n')
 

            # Define the line to exclude
            exclude_line = "[+] Email used, [-] Email not used, [x] Rate limit, [!] Error"

            # Filter out the excluded line
            lines = [line for line in lines if not line.startswith('100%') and line != exclude_line]
            domains = []
            for line in lines:
                domain = line.split()
                try:
                    domains.append(domain[1])
                except:
                    continue
            # Print the remaining lines
            print('\n'.join(lines))

            # add email and domains to results dictionary
            results[email] = domains
            #time.sleep(5)  # Wait for 5 seconds

        header = ['email'] + sorted(set(domain for domains in results.values() for domain in domains))
        rows = []
        # create rows and colums for found domains and emails
        for email, domains in results.items():
            row = [email]
            for domain in header[1:]:
                if domain in domains:
                    row.append('x')
                else:
                    row.append('')
            rows.append(row)

        #Write to a csv file
        with open(self.csvname, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(rows)

        print(f'CSV file created: {self.csvname}')
