import pexpect
import sys
m = pexpect.spawn('python add_num.py')
m.logfile_read = sys.stdout
m.expect("inter number")
m.sendline(10)
m.expect("inter number:")
m.sendline(20)
m.expect("enter arithmatic operator:")
m.sendline("*")

m.close()
