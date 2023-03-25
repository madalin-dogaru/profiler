# profiler
Target profiling for red teaming exercises.
---

Usage
---
```
profiler.py [-h] [-npath NAMES_FILE] [-dpath EMAIL_DOMAIN] [-pgen VALUES_FILE] [-cprofile PROFILE_NAME]

Create email addresses from a file with names and surnames, generate combinations of specified values, and create a profile file.

options:
  -h, --help            show this help message and exit
  -npath NAMES_FILE, --names-file NAMES_FILE
                        Path to the file containing names and surnames.
  -dpath EMAIL_DOMAIN, --email-domain EMAIL_DOMAIN
                        Email domain, e.g., @microsoft.com
  -pgen VALUES_FILE, --values-file VALUES_FILE
                        Path to the file containing values for combinations.
  -cprofile PROFILE_NAME, --profile-name PROFILE_NAME
                        Profile name to create a new profile file.
```