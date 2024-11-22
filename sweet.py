''' 4. A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over.'''
sweet=int(input("how many sweet ? "))
pupil=int(input("how many pupils? "))
remaining=sweet%pupil
per=sweet//pupil
if remaining==1:
    print(f"There will be {per} sweets per pupil with {remaining} sweet left ")
elif remaining<1:
    print(f"There will be {per} sweets per pupil with no sweet left over ")
else:
    print(f"There will be {per} sweets per pupil with {remaining} sweets left over ")
    
