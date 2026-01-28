print("student passsed or failed ")

sub1 = int(input ("enter the mmaths marks"))
sub2 = int (input ("enter the chem marks"))
sub3 = int (input ("enter the physics marks"))
marks = [sub1, sub2, sub3]
percent = sum(marks)/3
print(percent)

if (percent>33):
    print("paaaaaasssssseeeeddd!!!!!")
else:
    print("failed!!!!!")
