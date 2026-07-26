num=int(input('Enter Number:'))

if(num>=0):
    if(num>50):
        if(num>100):
            if(num>150):
                if(num>200):
                    if(num>250):
                        print('Number is Greater than 250.')
                    else:
                        print('Number is between 200-250.')           
                else:
                    print('Number is between 150-200.')
            else:
                print('Number is between 100-150.')
        else:
            print('Number is between 50-100.')
    else:
        print('Number is between 0-50.')
else:
    print('Number is less than 0 or equals to 0')