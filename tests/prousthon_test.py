import prousthon

print("Initializing test! (1/1)")
try:
    print("")
    print(prousthon.get_question())
    print("")
except AttributeError:
    print("Whoops! Executing a exercise() call got an AttributeError!")
    exit(2)
except ValueError:
    print("Whoops! Executing a exercise() call got an ValueError!")
    exit(2)
print("Successful Test! (1/1 COMPLETE)")
print("Terminating!")
exit()
