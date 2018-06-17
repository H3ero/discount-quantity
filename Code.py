WeedP = {1:'Amnesia', 2:'Kush',3:'Chronic'}
W_price = {1:20,2:25,3:35}

print(' Menu\n 1-Amnesia $20\n 2-Kush $25\n',
'3-Chronic $35\n 0-Quit\n')

W_order = input('Select the number of your stream please  \n')

while True:
    if W_order == '0':
        quit
    else:
        try:
            if int(W_order) in WeedP:
                W_qtt = float(input('How many grams sir? \n'))
                try:
                    W_total = W_price[int(W_order)]*W_qtt
                    if 0< W_qtt <28:
                        print('\nNo discount \n')
                        print('$',W_price[int(W_order)],'x',"%.2f"%W_qtt,'g \n\nTotal $',W_total)
                        print(15*'=')
                        print('\n',WeedP[int(W_order )],"%.2f"%W_qtt)
                    elif 28<= W_qtt <56:
                        print('\n$',W_price[int(W_order)],'x',"%.2f"%W_qtt,'g\n\nSubTotal $',W_total)
                        print('\nDiscount of 5% $',"%.2f"%(W_total*0.05),'\n\nTotal $',"%.2f"%(W_total*0.95))
                        print(15*'=')
                        print('\n',WeedP[int(W_order)],"%.2f"%W_qtt)
                    elif 56<= W_qtt <100:
                        print('\n$',W_price[int(W_order)],'x',"%.2f"%W_qtt,'g\n\nSubTotal $',W_total)
                        print('\nDiscount of 10% $',"%.2f"%(W_total*0.10),'\n\nTotal $',"%.2f"%(W_total*0.90))
                        print(15*'=')
                        print('\n',WeedP[int(W_order)],"%.2f"%W_qtt,)
                    elif 100<= W_qtt:
                        print('\n$',W_price[int(W_order)],'x',"%.2f"%W_qtt,'g\n \nSubTotal $',W_total)
                        print('\nDiscount of 15% $',"%.2f"%(W_total*0.15),'\n\nTotal $',"%.2f"%(W_total*0.85))
                        print(15*'=')
                        print('\n',WeedP[int(W_order)],"%.2f"%W_qtt,'g')
                    else:
                        continue
                    break 
         
                except ValueError:
                    print(' Try again ')
            else:
                print(' Try again ')
        except:
            print('\n Try again ')
