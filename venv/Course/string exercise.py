
msg = 'Welcome to Python 101: Strings'
new = msg[8]+msg[12]+msg[2]+msg[1]+msg[-5]
msg1 = msg[-5:-1]
msg2 = msg[8:10]
print(len(msg))
print(msg[18], msg[:7], msg1.title(), msg2.title(), new.title())
txt = '1 Welcome Ring To Tyler' [::-1]
print(txt)

print(msg.replace('Python','MATLAB'))
msg3 = msg.replace('Python','MATLAB')
print(msg3)
print('MATLAB' in msg3)

# new task
name = 'TERRY'
colour = 'RED'

txt1 = '[' + name.title() + '] loves the colour ' + colour.lower() + '!'
txt2 = f'[{name.title()}] loves the colour {colour.lower()}!'
print(txt1)
print(txt2)



