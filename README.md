# Profiler   

Target profiling for red teaming exercises.
---

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
