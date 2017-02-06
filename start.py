#!/usr/bin//python

import os
from subprocess import Popen, PIPE, check_call

#start up tempo2 service
check_call(["docker-compose","up","-d"])
p = Popen(["docker","ps","-aq"],stdout=PIPE,stderr=PIPE)
p.wait()

#copy public keys into root and psr user directories
container = "presto"
print("docker cp ~/.ssh/id_rsa.pub %s:/root/.ssh/authorized_keys"%container)
os.system("docker cp ~/.ssh/id_rsa.pub %s:/root/.ssh/authorized_keys"%container)
print("docker cp ~/.ssh/id_rsa.pub %s:/home/psr/.ssh/authorized_keys"%container)
os.system("docker cp ~/.ssh/id_rsa.pub %s:/home/psr/.ssh/authorized_keys"%container)
