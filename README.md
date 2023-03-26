![profiler_logo](https://user-images.githubusercontent.com/34633522/227782206-76a478c0-7197-4a6c-8631-4b8bbf44dee3.jpg)
# Profiler   

Target profiling for red teaming exercises.
---

Install
---
##### 1.Clone it:   
`git clone https://github.com/madalin-dogaru/profiler.git` 

##### 2.Install requirements:   
`pip install -r requirements.txt`   


Examples
---
1. Take a list of IP's, get their Country/City/Area and write it in a file(including the IPs).    
`python3 profiler.py -iplist file_containing_ips -o output_file_name`

2. Take a list of domains, get their IPs/Country/City/Area and write it in a file.   
`python3 profiler.py -dlist file_containing_domains -o output_file_name`

3. Specify a single domain and print on the terminal the IP/Country/City/Area.   
`python3 profiler.py -d zf.ro`

4. Specify a single IP and print on the terminal the IP/Country/City/Area.   
`python3 profiler.py -ip zf.ro`

5. The not so beautiful help.    
`python3 profiler.py -h`   
