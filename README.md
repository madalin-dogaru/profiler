
<img align="center" alt="PNG" src="https://github.com/madalin-dogaru/madalin-dogaru/blob/master/profilerlogo.png?raw=true" width="900" height="150" />

# Profiler   
Yes, I know, someone somewhere created a tool that does this. I just want to create my own and there's nothing you can do to stop me :) 
This will be a target profiling tool used in red teaming exercises. Currently still prototyping and testing various features, so if you have any ideas, this is the moment when they will have the most impact on development.   

Install
---
#### Classic Install
##### 1.Clone it:   
`git clone https://github.com/madalin-dogaru/profiler.git` 

##### 2.Install requirements:   
  - `pip install -r requirements.txt`   
  - Install [Holehe](https://github.com/megadose/holehe/tree/master#%EF%B8%8F-installation) (must be accessible via global path)
#   
#### Docker Build   
For now you will have to build your image locally, although I created an official image here: `https://hub.docker.com/r/iot41/profiler`, given you need to add you api keys either I change the profiler to accept API keys via cli parameters or environment variables, not happy with either of them, still searching for more elegant solutions.    
1. `git clone https://github.com/madalin-dogaru/profiler.git`
2. `cd profiler`
3. Add your API keys/secrets in `dorks_search.py` and `godaddy_search.py`
4. Build the docker image:
```
docker build -t profiler:0.1 .
[+] Building 5.8s (10/10) FINISHED                                                                                                                           
 => [internal] load build definition from Dockerfile                                                                                                    0.0s
 => => transferring dockerfile: 722B                                                                                                                    0.0s
 => [internal] load .dockerignore                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.11                                                                                          2.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                           0.0s
 => [1/4] FROM docker.io/library/python:3.11@sha256:2dd2f9000021839e8fba0debd8a2308c7e26f95fdfbc0c728eeb0b5b9a8c6a39                                    0.0s
 => [internal] load build context                                                                                                                       0.0s
 => => transferring context: 303.03kB                                                                                                                   0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                           0.0s
 => [3/4] COPY . /app                                                                                                                                   0.0s
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt                                                                                            3.4s
 => exporting to image                                                                                                                                  0.1s 
 => => exporting layers                                                                                                                                 0.1s 
 => => writing image sha256:1143d5dc1a7445fa8368e9fc95d934149274ad08f6b9ef09f489b1713f7db61f                                                            0.0s 
 => => naming to docker.io/library/profiler:0.1
```
5. When using features that require local files, you need to mount the file and then use it. Example below:   
```
docker run -v /Users/User/tools/dorks_example_file:/app/dorks_example_file profiler:0.1 python profiler.py -dork samsung.com -f /app/dorks_example_file
```



Examples
---  
#### -mails   
Use the power of Holehe to check on what websites a user created accounts. I've added functionality so a list of emails can be specified from a file and the results are filtered to show only valid accounts.    
<img align="center" alt="PNG" src="https://github.com/madalin-dogaru/madalin-dogaru/blob/master/account_check.png?raw=true" width="350" height="700" /> 

Additionally ```-om``` or ```--format-csv``` flag can be provided to output the mails in CSV format.   
`python3 profiler.py -mails ~/tools/emails -om findings.csv`

#### -dork :
Perform powerful Google dorks searches using SerpApi integration: You need to supply a file with google dorks(one per line) and a target domain. You need an SerpAPI API key.    
`python3 profiler.py -dork smartree.com -f workfiles/dorks_list_file_name`   

<img align="center" alt="PNG" src="https://github.com/madalin-dogaru/madalin-dogaru/blob/master/google_dork_example.png?raw=true" width="650" height="430" />   


#### -be : 
Integration with BinaryEdge's API to get data about a target IP (results types/format are still WIP)   
`python3 profiler.py -be 212.93.143.54`


#### -url : 
Scan all the files inside a folder for URLs and print them in the terminal. Or add -o and give it a file to the write the info in.    
`python3 profiler.py -url ~/path/to/folder`

#### -egen :
Read firstname/lastname from a file(1 pair per line) and the email domain and output all common emails in a file.     
`python3 profiler.py -egen workfiles/names -edom microsoft.com -o results/test`

#### -daddy :
Supply a domain and get other available suffixes on goddady.com (requires API token).   
`python3 profiler.py -daddy microsoft.com`

#### -u :
Supply a username and get a list of websites where the username exists
`python3 profiler.py -u USERNAME`

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
