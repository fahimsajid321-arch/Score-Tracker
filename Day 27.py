Questions = [["What is the capital of Pakistan","Islamabad","Lahore","Karachi","Rawalpindi", 1],
              ["WHo is PM","Shebaz", "Asim Munir", "Asif Ali","Rawalpindi", 1], 
              ["Who is COAS", "Shebaz", "Asim Munir", "Asif Ali","Rawalpindi", 2], 
              ["Who deserve to be in Prison", "Shebaz", "Asim Munir", "Imran Khan","Rawalpindi", 3], 
              ["What is the capital of Pakistan","Islamabad","Lahore","Karachi","Rawalpindi", 1], 
              ["WHo is PM","Shebaz", "Asim Munir", "Asif Ali","Rawalpindi", 1], 
              ["Who is COAS", "Shebaz", "Asim Munir", "Asif Ali","Rawalpindi", 2], 
              ["Who deserve to be in Prison", "Shebaz", "Asim Munir", "Imran Khan","Rawalpindi", 3], 
              ["What is the capital of Pakistan","Islamabad","Lahore","Karachi","Rawalpindi", 1], 
              ["WHo is PM","Shebaz", "Asim Munir", "Asif Ali","Rawalpindi", 1], 
              ["Who is COAS", "Shebaz", "Asim Munir", "Asif Ali","Rawalpindi", 2], 
              ["Who deserve to be in Prison", "Shebaz", "Asim Munir", "Imran Khan","Rawalpindi", 3]]

levels = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000]
money = 0
for i in range(0,len(Questions)):
    Question = Questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"{Question[0]}")
    print(f"a. {Question[1]}        b. {Question[2]}")
    print(f"c. {Question[3]}        d. {Question[4]}")
    reply = int(input("Enter your answer(1 - 4) or Press 0 to quit : "))
    if(reply==0):
        money = levels[i-1]
        break
    if (reply == Question[-1]):
        print(f"correct answer, you won {levels[i]} \n")
        if (i == 3):
            money = 400000
        elif (i == 6):
            money = 700000
        elif (i == 11):
            money = 120000
    else:
        print("Wrong Answer")
        break
print(f"Your take home money is {money}")

