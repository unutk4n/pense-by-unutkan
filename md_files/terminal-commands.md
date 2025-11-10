NOTE: This sheet may become sporadic since I will add this commands only if I need or find them.

# Terminal Commands

## File Permissions.

In UNIX and Linux EVERYTHING is a file. 
Devices are usually referred to as a node; however, they are still files. All of the files  on a system have permissions that allow or prevent others from viewing, modifying or  executing. 
To change or edit files that are owned by root, sudo must be used 

| read >| (view) | r or 4|  
|--------|-------|---------| 
| write >| (edit) | w or 2| 
| execute >| (execute) | x or 1|  


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


unzip >>> unzip filename.zip





# BASH DOCUMENTS AND NOTES


## What is BASH?

Bash is the shell for the GNU operating system. 
The name is an acronym for the ‘Bourne-Again SHell 
While the GNU operating system provides other shells, including a version of csh, Bash is the default shell. Like other GNU software, Bash is quite portable. It currently runs on nearly every version of Unix and a few other operating systems 

## What is Shell?
At its base, a shell is simply a macro processor that executes commands. The term macro processor means functionality where text and symbols are expanded to create larger expressions.  

<b> IMPORTANT </b>

A Unix shell is both a command interpreter and a programming language. As a command interpreter, the shell provides the user interface to the rich set of GNU utilities. The programming language features allow these utilities to be combined. Files containing commands can be created, and become commands themselves. These new commands have the same status as system commands in directories such as /bin, allowing users or groups to establish custom environments to automate their common tasks.  

There is two types of shells. Interactively and non-interactively. The non part doesn't take command as input. Instead it reads it from a file and the other type allows inputs.

A shell allows execution of GNU commands, both synchronously and asynchronously. The shell waits for synchronous commands to complete before accepting more input; asynchronous commands continue to execute in parallel with the shell while it reads and executes additional commands.  The <b>redirection </b>  constructs permit fine-grained control of the input and output of those commands. Moreover, the shell allows control over the contents of commands’ environments.  

<b> IMPORTANT </b>
Shells also provide a small set of built-in commands (builtins) implementing functionality impossible or inconvenient to obtain via separate utilities. For example, cd, break, continue, and exec cannot be implemented outside of the shell because they directly manipulate the shell itself. 


buraya kadar olan kismi biraz kisisellesirebiliriz aslinda.


## Definitions

- Posix = A standart furthermore the bash is concerned with the posix 1003.1 standart.
- blank = space or tab character
- build-in = a command that can be used by default because it's already downloaded with the app or software itself.
- control operator = A <b> token </b> that performs a control function. It is a <b> newline </b> or one ofthe following ‘||’, ‘&&’, ‘&’, ‘;’, ‘;;’, ‘;&’, ‘;;&’, ‘|’, ‘|&’, ‘(’, or ‘)’. 
- exit status = The value which is returned by the command to the user. The value is restricted to eight bits so it can be 255 maximum.
- field = A unit of text of the shell. as the command name and arguments. 
- job control = a mechanism user can stop resart or resume.
- metacharacter = A character that seperates words. space, tab, newline or the following characters; ‘|’, ‘&’, ‘;’, ‘(’, ‘)’, ‘<’, or ‘>’. 
- name = word consisting solely of letters, numbers and underscores. can't begin with number. names are used as shell variable and function names. referred as identifier.
- operator = A <b> control operator </b> or a <b> redirection operator</b>. Operators contain at least on unquoted metacharacter.
- process group = A collection of related processes each having the same process group ID. 
- process group ID = A unique identifier that represents a <b> process group</b> during its lifetime. 
- reserved word = words that has a special meaning to the shell. like "for" and "while"
- return status = A synonim for <b> exit status </b>. 
-  signal = A mechanism that kernel sends to say that an event is occuring.
- special build-in = a shell build-in that is assigned as special by the posix standart.
- token = A sequence of characters considered as a single unit by the shell. It's either a word or a operator.
- word = A sequence of characters treated as a unit by the shell. Words may not include unquoted metacharacters. 









glmark2 -b build:duration=1





























