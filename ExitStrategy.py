import matplotlib.pyplot as plt
p0 = 1;
n0 = 1;
r = 0.5;
t = 0.5;
c = 1 - t;
tt = 0;
print()
print("------------start, return = " + str(r) +
         ", takeout = " + str(t) + ", -----------------");
print();
xlist = [1]
y0list = [1]
y1list = [1]
y2list = [0]
y3list = [0]
y4list = [1]
y5list = [1]
for i in range(1,11):
    p1 = (1 + i*r);
    n1 = (t + c*p1*n0)/p1;
    amt0 = n0*p1;
    amt1 = n1*p1;
    xlist.append(p1)
    y0list.append(amt0)
    y1list.append(amt1)
    y2list.append(amt0 - amt1)
    tt += amt0 - amt1;
    y3list.append(tt)
    y4list.append(amt1 + tt)
    y5list.append(1 + tt)
    print("initial " + str(amt0) + ", final " +
        str(amt1) + ", takeout " + str(amt0 - amt1) + ", total takeout " + str(tt) + 
        ", price " + str(p1) + " times, total amt " + str(amt1 + tt) + ", exit liquidity amountt " + str(1 + tt));
    print();
    p0 = p1;
    n0 = n1;
print("------------end-----------------")
print()
plt.scatter(xlist, y0list, label = "initial")
plt.scatter(xlist, y1list, label = "final after takeout")
plt.scatter(xlist, y2list, label = "takeout")
plt.plot(xlist, y3list, label = "total takeout")
plt.plot(xlist, y4list, label = "total amount")
plt.plot(xlist, y5list, label = "exit liquidity amount")
plt.title("return = " + str(r) + ", takeout = " + str(t))
plt.legend()
plt.show()


# rate of increment 'r' is dependent on the size of project. For large projects the increment step 'r' is small, around 0.5.
# For small projects the increment step 'r' is large, around 1. 
# After a certain number of steps (inflection point, around 5) the 'air starts to get thinner', 'things get too hot'.
# rate of takeout 't' should be such that after the inflection point the 'final after takeout' value starts to decrease.
# for 'r' = 0.5, 't' = 0.25 (price = 3.5 times, 5 steps) | for 'r' = 1, 't' = 0.2/0.3 (price = 6/5 times, 5/4 steps)