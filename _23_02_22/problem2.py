#remove the preceeding 0's to make the ip address vaalid

ip="00000127.001.001/24"
newip=""
for i in ip.split("."):
    newip=newip+i.lstrip("0")+"."
print(newip)
for j in newip.split("/"):
    mask = j
    newip=newip.rstrip(mask)

print("ip=",newip)
print("mask",mask)