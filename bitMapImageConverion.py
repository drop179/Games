v = False
while v == False:
  time = input("Enter the time in the format hr:mn  ")
  if ":" not in time:
    v = False
  elif int(time.split(":")[0]) > 23 or int(time.split(":")[1]) > 59 or int(time.split(":")[0]) < 0 or int(time.split(":")[1]) < 0:
    v = False
  else:
    v = True

  if v == False:
    time = input("Incorrect format.\nEnter the time in the format hr:mn  ")


time = [*time]
time = " ".join(time)
three = ["01110","10001","00010","10001","01110"]
four = ["10001","10001","11111","00001","00001"]
five = ["01111","10000","01111","00001","11110"]
six = ["00110","01000","11110","10001","01110"]
seven = """11111
00010
00100
01000
10000"""
eight = """01110
10001
01110
10001
01110"""
nine = """
01110
10001
01010
00100
01000"""
colon = """1
1
0
1
1"""
space = """0
0
0
0
0"""

zeroes = ["111", "101", "101", "101", "111"]
nums = {"0": zeroes, "1": one, "2": two, "3": three, "4": four, "5": five, "6": six, "7": seven, "8": eight, "9": nine, " ": space, ":": colon}

bitTime = []
for i in time:
  bitTime.append(nums[i])
