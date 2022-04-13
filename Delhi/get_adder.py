import os

for i in range(10):
    command = "git add Delhi_00"+str(i)
    os.system(command)
    command = "Delhi_00"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")


for i in range(10,100):
    command = "git add Delhi_0"+str(i)
    os.system(command)
    command = "Delhi_0"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")
