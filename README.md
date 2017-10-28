# SysOps

Ok so considering the task, I believe I hacked enough Python code to solve it.
The result is the file check.py from this folder.

Here are the steps I took and the logic I followed:

1. First I did some recon, discovered we're on an Ubuntu machine missing some of the tools. (+1 bonus points at login)
2. Discovered an error in the config file for Apache, removed it, restarted Apache.
3. Installed net-tools, wget, nmap, updated python, removed python3 modules, 
4. Found second bonus point with: "wget localhost" and "cat index.html". It was in the index.html file.
5. Had to install some python modules.
6. Tried to use the local smtp, couln't get around to it and decided to use a public service. The task said nothing about having a working SMTP. :)
7. Built a python script (considering I never programmed in python before today) that I believe does the job.

Here is the logic in the Python check.py:

1. using the subprocess module I see if a process runs for apache2 on port 80. If that is true, variable a1 becomes 2.
2. using the commands module I see if the wget output contains "200 OK". If that is true, variable a2 becomes 4.
3. variable a becomes a1 + a2
4. check to see if a == 6 (line 47)
   if yes
   4.yes - website is up. I initially sent emails with "Website is up" but now I commented out that code.
   if no
   4.no checks if a file called log.txt exists in the same folder (log.txt is used to count how many times the error was encountered) (line 57)
          4.no.yes if file log.txt exists, I read it (line 59) and get the content as integer into the variable contor
                  if contor == 5 (its the 5th time an error is ecountered) - sends email to address2 (line 67)
                  if contor not 5 - sends email to address1 (line 79), increases contor with 1, deletes log.txt, recreates log.txt with new contor (line 85)
          4.no.no if file log.txt doesn't exist .. I create file log.txt with 1 in the first line (line 93)
          
5. I remove index.html created by wget.

          
                  
          
