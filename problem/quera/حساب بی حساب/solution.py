n = int(input())
transactions = [input().split() for i in range(n)]
# مرتب سازی تراکنش ها برحسب زمان
transactions.sort(key= lambda t: t[2])

def calculated_deposit():
    least_deposit = 0
    # مقدار مجودی حال حاضر
    max_deposit = 2000000
    # حداکثر موجودی
    base_deposit = 0
    # حداقل مقدار موجودی 
    for transaction in transactions:
        amount  = int(transaction[1])
        if transaction[0] == 'DEP':
            least_deposit += amount
            max_deposit += amount
        else:
            if transaction[3] == "OK":
                if amount > least_deposit:
                    base_deposit += amount - least_deposit
                    least_deposit = 0
                else:
                    least_deposit -= amount
                
                max_deposit -= amount
                if max_deposit < 0:
                    return -1
            else:
                max_deposit = min(max_deposit, amount-1)
                if amount < least_deposit:
                    return -1
    return base_deposit
                
base_deposit = calculated_deposit()
if base_deposit == -1:
    print("DOROGHE")
else:
    print(base_deposit)