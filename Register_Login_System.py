# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:37:02 2022

@author: Sheryl Sharon G

Title: Registration and Login system using Python, file handling
"""
import sys
#validate the password
def validatePassword(passwd):
    if len(passwd)>5 and len(passwd)<16:
        digit, l_case, u_case = 0,0,0
        for ch in passwd:
            if ch.isdigit():
                digit+=1
            if ch.islower():
                l_case+=1
            if ch.isupper():
                u_case+=1
        if digit>=1 and l_case>=1 and u_case>=1:
            return True
        else:
            return False
    else:
        return False

#validate the email address
def validateEmail(email):
    #validating case 1, 2, 3
    if(email.index('@')<email.index('.') and email.index('@')>0 and email.index('@')!=email.index('.')+1):
        #validate case 4
        if(email[0].isalpha()):
            return True
    return False

#get email and process for validation
def register():
    print("Email: ")
    em=input()
    ret = validateEmail(em)
    if ret is False:
        sys.exit('Invalid email Id\nExiting..')
    print("Password: ")
    passwd=input()
    ret = validatePassword(passwd)
    if ret is False:
        sys.exit('Invalid password\nExiting..')
    f1=open('User_Credentials.txt','a+')
    em+=' '
    f1.write(em)
    passwd+='\n'
    f1.write(passwd)
    f1.close()
    return
'''
#get password and process for validation
def password():
    print("Password: ")
    passwd=input()
    ret = validatePassword(passwd)
    if ret is False:
        sys.exit('Invalid password\nExiting..')
    f1=open('User_Credentials.txt','a+')
    passwd+='\n'
    f1.write(passwd)
    f1.close()'''

#fetch password from file
def retrievePasswd(email):
    f1=open('User_Credentials.txt','r')
    for line in f1:
        u_name, pwd = line.split(" ")
        if email == u_name:
            f1.close()
            return pwd
    f1.close()
    return "False"

#recreate password
def newPassword(oldPasswd):
    print("Password: ")
    passwd=input()
    ret = validatePassword(passwd)
    while(ret == False):
        print('Weak Password!\n')
        print("Password: ")
        passwd=input()
        ret = validatePassword(passwd)
    passwd+='\n'
    with open('User_Credentials.txt', 'r') as f1:
        text = f1.read()
    f1.close()
    with open('User_Credentials.txt','w') as f1:
        new_text = text.replace(oldPasswd,passwd)
        f1.write(new_text)
    f1.close()
    
#login
def login():
    print("Email: ")
    em=input()
    print("Password: ")
    passwd=input()
    f1=open('User_Credentials.txt','r')
    flag = False
    for line in f1:
        u_name, pwd = line.replace("\n","").split(' ')
        
        if em == u_name and passwd == pwd:
            print('Login Successful!\n')
            f1.close()
            flag = True
            break
    if flag is False:
        print('Login Unsuccessful\n')
        print('New User? Enter 1, to register')
        print('Existing User? Enter 2, to retrieve password\nEnter your choice: ')
        choice=int(input())
        #New user? register 
        if choice == 1:
            print("=========================REGISTER========================")
            register()
            print('Registration Successful!')
        #Existing User? retrieve password - forgot password
        elif choice == 2:
            ret = retrievePasswd(em)
            #username does not exist in the database
            if ret == "False":
                print('Invalid Username!\nRegister to Login!\n')
                register()
                print('Registration Successful!')
            #username exists, change (or) show password
            else:
                print('Enter 1 to show password\nEnter 2 to enter new password\nEnter your choice: ')
                choice=int(input())
                #show password
                if choice == 1:
                    print('Retrieved Passsword: ',ret,'\nLogin again!\n')
                    print("==========================LOGIN==========================")
                    login()
                #recreate new password
                elif choice == 2:
                    newPassword(ret)
                    print('Password recreated successfully!')
                #invalid choice
                else:
                    print('Invalid Choice\nExiting...\n')
        else:
            print('Invalid Choice\nExiting...\n')
                    
#Driver Code                   
print("================REGISTER AND LOGIN SYSTEM================")
print("To Register, enter 1\nTo Login, enter 2\nEnter your choice: ")
choice = int(input())
#register
if choice == 1:
    print("=========================REGISTER========================")
    register()
    print('Registration Successful!')
#login
elif choice == 2:
    print("==========================LOGIN==========================")
    login()
#invalid choice
else:
    print('Invalid Choice\nExiting...\n')
    
#End of code