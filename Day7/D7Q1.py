#
#Question 1 :
#Use the dictionary,
 #port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"},
#and make a new dictionary in which keys become values and values become keys,
# as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23,"http": 80}
#

port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print(port1)

port1 = {value:key for key, value in port1.items()}
print(port1)