print("Qualification?")
qualification = input()
print("Work done?")
work_done = input()
if(int(qualification) >= 4) and (work_done == 'yes'):
    final = "pass"
else:
    final = "not pass"
print(final)