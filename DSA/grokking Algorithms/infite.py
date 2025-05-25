#def countdown(i):
  #  print(i)
 #   countdown(i+1)

#countdown(1)
def countdown(i):
    print(i)
    if i<=0:
        return
    else:
        countdown(i-1)


countdown(10)

