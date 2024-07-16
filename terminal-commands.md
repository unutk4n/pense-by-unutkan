NOTE: This sheet may become sporadic since I will add this commands only if I need or find them.

# Terminal Commands

## File Permissions.

In UNIX and Linux EVERYTHING is a file. 
Devices are usually referred to as a node; however, they are still files. All of the files  on a system have permissions that allow or prevent others from viewing, modifying or  executing. 
To change or edit files that are owned by root, sudo must be used 

| read | (view) | r or 4|
|--- - --| ---  - --|--- - ---|
| write | (edit) | w or 2|
|--- --- |--- --- --|- --- ---  |
| execute | (execute) | x or 1| 
|--- --- --|- --- --- |--- --- --- |

chmod a-w file (removes all writing permissions) 
chmod o+x file (sets execute permissions for other (public permissions)) 
chmod u=rx file        (Give the owner rx permissions, not w) 
chmod go-rwx file      (Deny rwx permission for group, others) 
chmod g+w file         (Give write permission to the group) 
chmod a+x file1 file2  (Give execute permission to everybody) 
chmod g+rx,o+x file    (OK to combine like this with a comma) 

u = user that owns the file 
g = group that owns the file 
o = other (everyone else) 
a = all (everybody) 

r = read aces to the file 
w = write access 
x = execute (run) access  
