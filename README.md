
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

For -url, 
1. Scan all the files inside a folder for URLs and print them in the terminal. Or add -o and give it a file to the write the info in.    
`python3 main.py -url ~/path/to/folder`   

2. Read firstname/lastname from a file(1 pair per line) and the email domain and output all possible emails in a file.     
`python3 main.py -egen names -edom microsoft.com -o test`   

3. Supply a domain and get other available suffixes on goddady.com (requires API token).   
`python3 main.py -daddy microsoft.com`   

4. Supply a domain and get similarly looking domains for that domain and suffix that are available on godaddy.com. (requires API token)   
`main.py -domphish microsoft.com`

3. Take a list of IP's, get their Country/City/Area and write it in a file(including the IPs).    
`python3 main.py -iplist file_containing_ips -o output_file_name`   

4. Take a list of domains, get their IPs/Country/City/Area and write it in a file.   
`python3 main.py -dlist file_containing_domains -o output_file_name`   

5. Specify a single domain and print in the terminal the IP/Country/City/Area.   
`python3 main.py -d zf.ro`   

6. Specify a single IP and print in the terminal the IP/Country/City/Area.     
`python3 main.py -ip zf.ro`   

7. The not so beautiful help menu.    
`python3 main.py -h`   
