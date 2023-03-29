
<img align="left" alt="PNG" src="https://github.com/madalin-dogaru/madalin-dogaru/blob/master/profiler_logo.png?raw=true" width="350" height="488" />

# Profiler   
Yes, I know, someone somewhere created a tool that does this. I just want to create my own and there's nothing you can do to stop me :) 
This will be a target profiling tool used in red teaming exercises. Currently still prototyping and testing various features so this is the moment when new ideas have the most impact on development.   

In the prototyping phase I will leave some hardcoded API authorization tokens in the code(for the lazy ones:)). These are empty test accounts that will be deleted.  

Install
---
##### 1.Clone it:   
`git clone https://github.com/madalin-dogaru/profiler.git` 

##### 2.Install requirements:   
`pip install -r requirements.txt`   

Examples
---

#### -url : 
Scan all the files inside a folder for URLs and print them in the terminal. Or add -o and give it a file to the write the info in.    
`python3 main.py -url ~/path/to/folder`

#### -egen :
Read firstname/lastname from a file(1 pair per line) and the email domain and output all common emails in a file.     
`python3 main.py -egen names -edom microsoft.com -o test`

#### -daddy :
Supply a domain and get other available suffixes on goddady.com (requires API token).   
`python3 main.py -daddy microsoft.com`

#### -domphish :
Supply a domain and get similarly looking domains for that domain and suffix that are available on godaddy.com. (requires API token)   
`main.py -domphish microsoft.com`

#### -iplist :
Take a list of IP's, get their Country/City/Area and write it in a file(including the IPs).    
`python3 main.py -iplist file_containing_ips -o output_file_name`

#### -ip :
Specify a single IP and print in the terminal the IP/Country/City/Area.   
`python3 main.py -ip zf.ro`

#### -dlist :
Take a list of domains, get their IPs/Country/City/Area and write it in a file.   
`python3 main.py -dlist file_containing_domains -o output_file_name`

#### -d :
Specify a single domain and print in the terminal the IP/Country/City/Area.   
`python3 main.py -d zf.ro`

#### The not so beautiful help menu.    
`python3 main.py -h`
