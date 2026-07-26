#4.else-will execute when loop executed successfully.

# for i in range(1,6):
#     if(i==3):
#         break
#     print(i)
# else:
#     print('For Loop Executed Successfully.')


for i in range(1,6):
    if(i==3):
        print(i)
        continue
    print(i)
else:
    print('For Loop Executed Successfully.')