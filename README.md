
<img align="center" alt="PNG" src="https://github.com/madalin-dogaru/madalin-dogaru/blob/master/profilerlogo.png?raw=true" width="900" height="150" />

# Profiler   
Yes, I know, someone somewhere created a tool that does this. I just want to create my own and there's nothing you can do to stop me :) 
This will be a target profiling tool used in red teaming exercises. Currently still prototyping and testing various features, so if you have any ideas, this is the moment when they will have the most impact on development.   

Install
---
##### 1.Clone it:   
`git clone https://github.com/madalin-dogaru/profiler.git` 

##### 2.Install requirements:   
  - `pip install -r requirements.txt`   
  - Install [Holehe](https://github.com/megadose/holehe/tree/master#%EF%B8%8F-installation) (accessible via global path)
#   
#   
Examples
---
In the prototyping phase I will leave some hardcoded API authorization tokens in the code(for the lazy ones:)). These are empty test accounts that will be deleted. In the future you will need various APIs for take full advantage of Profiler.   

#### -mails   
Use the power of Holehe to check on what websites a user created accounts. I've added functionality so a list of emails can be specified from a file and the results are filtered to show only valid accounts.    
<img align="center" alt="PNG" src="https://github.com/madalin-dogaru/madalin-dogaru/blob/master/account_check.png?raw=true" width="350" height="700" /> 

#### -dork :
Perform powerful Google dorks searches using SerpApi integration: You need to supply a file with google dorks(one per line) and a target domain. You need an SerpAPI API key.    
`python3 profiler.py -dork smartree.com -f workfiles/dorks_list_file_name`   

<img align="center" alt="PNG" src="https://github.com/madalin-dogaru/madalin-dogaru/blob/master/google_dork_example.png?raw=true" width="650" height="430" />   



#### -url : 
Scan all the files inside a folder for URLs and print them in the terminal. Or add -o and give it a file to the write the info in.    
`python3 profiler.py -url ~/path/to/folder`

#### -egen :
Read firstname/lastname from a file(1 pair per line) and the email domain and output all common emails in a file.     
`python3 profiler.py -egen workfiles/names -edom microsoft.com -o results/test`

#### -daddy :
Supply a domain and get other available suffixes on goddady.com (requires API token).   
`python3 profiler.py -daddy microsoft.com`

#### -domphish :
Supply a domain and get similarly looking domains for that domain and suffix that are available on godaddy.com. (requires API token)   
`python3 profiler.py -domphish microsoft.com`

#### -iplist :
Take a list of IP's, get their Country/City/Area and write it in a file(including the IPs).    
`python3 profiler.py -iplist workfiles/file_containing_ips -o results/output_file_name`

#### -ip :
Specify a single IP and print in the terminal the IP/Country/City/Area.   
`python3 profiler.py -ip zf.ro`

#### -dlist :
Take a list of domains, get their IPs/Country/City/Area and write it in a file.   
`python3 profiler.py -dlist workfiles/file_containing_domains -o results/output_file_name`

#### -d :
Specify a single domain and print in the terminal the IP/Country/City/Area.   
`python3 profiler.py -d zf.ro`

#### The not so beautiful help menu.    
`python3 profiler.py -h`
