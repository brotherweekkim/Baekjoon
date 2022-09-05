def solution(price, money, count):
    charge = 0
    for i in range(1, count + 1):
        charge += price * i
    
    if charge > money:
        return charge - money
    else:
        return 0