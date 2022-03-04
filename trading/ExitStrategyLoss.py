import matplotlib.pyplot as plt
n0 = 1
# p0 = 1
l = 0.1
t = 0.35
tt = 0

print()
print("------------start, loss rate = " + str(l) +
         ", takeout = " + str(t) + ", -----------------");
print();

xAxis = [1]
initialA = [1]
takeoutA = [0]
finalAfterTakeoutA = [1]
totalTakeoutA = [0]
totalAmountA = [1]

for i in range(1,11):
    p = 1 - l*i
    initial = n0*p
    takeout = initial*t
    finalAfterTakeout = n0*p*(1 - t)
    n1 = n0*(1 -t)
    tt += takeout
    ta = tt + finalAfterTakeout
    xAxis.append(p)
    initialA.append(initial)
    takeoutA.append(takeout)
    finalAfterTakeoutA.append(finalAfterTakeout)
    totalTakeoutA.append(tt)
    totalAmountA.append(ta)
    print("initial " + str(initial) + ", final " +
        str(finalAfterTakeout) + ", takeout " + str(takeout) + ", total takeout " + str(tt) + 
        ", price " + str(p) + " times, total amt " + str(ta));
    print();
    n0 = n1

print("------------end-----------------")
print()
plt.scatter(xAxis, initialA, label = "initial")
plt.scatter(xAxis, finalAfterTakeoutA, label = "final after takeout")
plt.scatter(xAxis, takeoutA, label = "takeout")
plt.plot(xAxis, totalTakeoutA, label = "total takeout")
plt.plot(xAxis, totalAmountA, label = "total amount")

plt.title("loss rate = " + str(l) + ", takeout rate = " + str(t))
plt.legend()
plt.show()



# At each level you realise loss on the amount you takeout. You then have 3 options: either re-invest the takeout
# amount at an even lower price (lower than the price at which you tookout) thereby increasing the total amount
# of tokens you hold (win from a staking perspective, as you are effectively farming new tokens), or, re-invest at a 
# price higher than where you tookout (some loss realised based on how high from the takeout level you re-invest, ex, 
# takeout at .9, re-invest at .92, loss 2.2% or takeout at .9, re-invest at 1, loss 10%), or, you don't re-invest the
# takeout amount in the same token at all, thereby realising a fixed loss based on your takeout level