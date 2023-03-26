
<img align="left" alt="PNG" src="https://raw.githubusercontent.com/madalin-dogaru/madalin-dogaru/master/profiler-logo.png?raw=true" width="370" height="493" />

# Profiler   

Target profiling tool for red teaming exercises. Currently its a simple tool that can be used to gather more information about IPs and domains but more features are on their way with which will focus on creating a profile of individuals or teams.    


Install
---
##### 1.Clone it:   
`git clone https://github.com/madalin-dogaru/profiler.git` 

##### 2.Install requirements:   
`pip install -r requirements.txt`   

#   
#   
#   

Examples
---

0. Scan all the files inside a folder for URLs and print them in the terminal.   
`python3 profiler.py -url ~/path/to/folder`   

1. Scan all the files inside a folder for URLs and print them in a file and in the terminal.   
`python3 profiler.py -url ~/path/to/folder -o output_file_name` 

2. Read firstname/lastname from a file(1 pair per line) and the email domain and output all possible emails in a file.    
`python3 profiler.py -egen names -edom microsoft.com -o test`   

3. Take a list of IP's, get their Country/City/Area and write it in a file(including the IPs).    
`python3 profiler.py -iplist file_containing_ips -o output_file_name`

4. Take a list of domains, get their IPs/Country/City/Area and write it in a file.   
`python3 profiler.py -dlist file_containing_domains -o output_file_name`

5. Specify a single domain and print in the terminal the IP/Country/City/Area.   
`python3 profiler.py -d zf.ro`

6. Specify a single IP and print in the terminal the IP/Country/City/Area.   
`python3 profiler.py -ip zf.ro`

7. The not so beautiful help menu.    
`python3 profiler.py -h`   
