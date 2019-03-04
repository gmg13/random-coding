li = [(1940, 1952), (1940, 1952), (1940, 1952), (1940, 1952),
      (1956, 2017), (1922, 2013), (1964, 1969), (1943, 1988)]

# get them into 2 list birth and death and sort them
# or hopefully in a more optimal fashion
birth = sorted([i[0] for i in li])
death = sorted([i[1] for i in li])

# get the count
n = len(birth)
# counter for most alive
maxalive = 0
# year when max alive
maxyear = 0
# current alive counter
alive = 0
# pointers for birth and death
bp = dp = 0

# main loop
while bp < n:
    print(maxalive, maxyear)
    if birth[bp] <= death[dp]:
        # increase alive
        alive += 1
        maxalive = max(maxalive, alive)
        if maxalive == alive:
            maxyear = birth[bp]
        bp += 1
    else:
        # decrease alive
        alive -= 1
        dp += 1

# print the max alive now
print("FINAL COUNT: ", maxalive, maxyear)
