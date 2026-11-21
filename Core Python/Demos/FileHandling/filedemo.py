# f=open("abc.txt",'r')
# # d=f.read()
# # d=f.readline()
# d=f.readlines()
# print(d)

# f=open("abc.txt","w")
# # f.write("MI wons the 5 IPL Trophies.")
# # f.write("\nCSK banned for 2 Years")
# li=["MI wons the 5 IPL Trophies",
#     "\nCSK wons the 5 IPL Trophies",
#     "\nRCB wons the 2 IPL Trophies"]
# f.writelines(li)

# f=open("abc.txt","a")
# f.write("\nGT won te 1 cup")

# with open("abc.txt","a") as f:
#     f.write("\nSRH won the 1 cup")
#     f.close()

with open("abc.txt","r+")as f:
    # d=f.read()
    # print(d)
    # f.write("KKR won the 3 IPL Trophies")
    f.seek(11)
    f.write("DC won the 0 IPL Trophies")