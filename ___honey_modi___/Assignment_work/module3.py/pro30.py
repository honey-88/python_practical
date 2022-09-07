#How Do You Check The Presence Of A Key In A Dictionary?
fruits_dict = dict(apple= 1, mango= 3, banana= 4)
key = 'orange'

if key in fruits_dict:
    print('Key Found')
else:
    print('Key not found')

#output : key not found.