from subprocess import call #importing call from subprocess otherwise we have use subprocess.call
call(["touch","-a","-m","-t","201512180130.09","file.txt"]) #calling unix touch command to modify timestamp #this is how we can call unix command from python command arguments
