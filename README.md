# py-pass-cracker
A password cracker which uses curl to crack web logins

# Working
It uses curl.exe in windows to send web requests replacing the username or password or both with the variables from the wordlist.

# Features
It has multiple features like
[1] Username enumuration using wordlist

If the website sends response for invalid username then it can be used to find valid users. This option uses a wordlist, which can conatin words or 
numbers or both.

[2] Username enumuration using numbers

Some websites might have a number as a user id in which case it would be better to take this option. For example : A site has user ids starting from
10100 to 10500.

[3] Attack specific account

If you have a username to attack then use this option. You will need to provide a wordlist which contains a list of passwords.

[4] Default login wordlist

Some users might have their username as their password, in this case this option will be useful. You will provide a wordlist and this tool will use each
word in it in place of user and password. That way you might be able to find default logins.

[5] Default login numbers

Same as option 4 but here instead of a wordlist numbers will be used. for example user id and password both might be 10100. Wordlist is not required as 
the numbers will be generated automatically via `for` loop in `range()`.

[6] Complete database harvester

Uses each and every combination of user and password. Both user and password wordlist is required.


As it uses curl the user dont need to do much work and this works for any website which sends data in plain text form. All they have to do is copy the 
request as curl command in their web browser(firefox recommended, didnt work as expected in chromium based browsers) dev tools.

# Flaws
Works very slow, only useful for demonstration of password attacks. Might not be worth using practically.
