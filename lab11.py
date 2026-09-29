bus=[["A","A","A"],
      ["A","A","A"],
      ["A","A","A"]]


for i in range(3):
    print(bus[i])

    print("select your seat")

    row= int(input("Enter your row Number:"))
    seat= int(input("Enter your seat Number:"))

if bus [row-1][seat-1]=="A":
   bus [row-1][seat-1]="R"

   print("your seat is Reserved")   

else:
    print("your seat is already Reserve")

for i in range(3):
    print(bus[i])