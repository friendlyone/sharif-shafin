'''
def malware():
    x = 1
    while x == 1:
        print("malware found ")
malware()
'''
import datetime
print("Hello Friend ")

person = input("what's your name ? ");
print('Hello', person);

day = input('how was your day ? ');
if day == "good":
    print("good for you ", person);
elif day == "great":
    print("that's great");
else:
    print('oh what happened ', person);
print("well it can only get get better am i right or what lol");
print("would you like to know today's date ? answer with Y or N ")
date = input();
if date == "Y":
    currentDate = datetime.date.today();
    print(currentDate);
elif date == 'y':
    currentDate = datetime.date.today();
    print(currentDate);
else:
    print('oh ok then ')
persons_age = input("what's your age ?  ");
print("nice so your ", persons_age, "years old");
print("nice when is your birthday ? ");

bday = input('');
print('nice well i was created, i cant tell you when i was created because its not even in my syntex');
print("how many girlfriends do you have ? lol ");

gf = input("well ?" );

if gf == 'yes':
    print("wow nice");
elif gf == "yea":
    print("god damn your doing good no your doing great");
else:
    print("oh why ", person);
'''
def malware():
    x = 1
    while x == 1:
        print("malware found ")
malware()
'''
'''
# This sets the condition of x for later use
x=0
# This is the main part of the program
def numtest():
    print ("I am the multiplication machine")
    print ("I can do amazing things!")
    c = input ("Give me a number, a really big number!")
    c=float(c)
    print ("The number", int(c), "multiplied by itself equals",(int(c*c)))
    print("I am Python 3. I am really cool at maths!")
    if (c*c)>10000:
        print ("Wow, you really did give me a big number!")
    else:
         print ("The number you gave me was a bit small though. I like bigger stuff than that!")

# This is the part of the program that causes it to run over and over again.
while x==0:
    numtest()
    again=input("Run again? y/n >>>")
    if x=="y":
        print("")
        numtest()
    else:
        print("Goodbye");
'''
print('hello man');
print('If your trying to get a girl to like you then this i for you ');
print('or ')
print('If you ever had a girl friend that your trying to get back then this is just the thing for you !!! ');
her_name = input('what was her first name ? ');
hair_color = input('what was her hair color ? ');
eye_color = input('what was her eye color ? ');
place_frst_seen = input('where did you first see her ? ');
met = input('how did you guys meet each other ? ');
frst_one_date = input('where was your first date ? ');
frst_two_date = input('when was your first date ? ');
print('dont worry all of this has a purpose, you will see when all the questions are finished ');
frst_thought_of_her = input('what was your first thought when you saw her for the first time ? ');
ur_number = input('wats ur phone number ? ' "don't leave this blank this a very important ");

for i in range(1000):
    print('process is running please wait, the may take a few minutes ');

get_back = input('so are you trying to get back with a ex-girlfriend ? Y/N');
if get_back == 'Y':
    print('Hi ', her_name,
      ' How are you doing. I have really been think about you lately and was thinking if you wanted to meet up ',
      frst_one_date,
      ' I know your probably still mad at me but i really wanted another chance ', her_name,
      ' just give me on more chance and i '
      ' I promise you wont be mad, sad, or upset ever again. ', her_name, ' I remember the first time i saw you in ',
      place_frst_seen,
      ' I remember how beautiful your ', eye_color, ' eyes and ', hair_color,
      ' hair look. And even up to today your still '
      ' the same ', her_name, ' . I remember from ', met,
      ' Thats the first time we met you remember our first date ? it was in ',
      frst_one_date, ' I remember that our first date happened on ', frst_two_date,
      ' that day i will never forget because i love you ',
      her_name,
      '. And all I really want in life right now is another chance with you . ' ' If you want to talk or text well then my '
      ' number is ', ur_number, '. Thanks for taking time out of your day to read this ', her_name);
#finish the else statment
else:
    print('');