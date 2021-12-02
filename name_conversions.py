import os
 
os.chdir(r'C:\Users\Viny Vyas\Dropbox\PC\Downloads\DS')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
