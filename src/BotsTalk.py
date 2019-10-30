#This program makes two bots(from cleverbot.com) talk to each other
#The data from one bot is sent to another and vice versa
import bs4,time,re,sys
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
browser_1 = webdriver.Chrome() 
browser_2 = webdriver.Chrome()

#open each bot in separate chrome window
browser_1.get('https://www.cleverbot.com/')
browser_2.get('https://www.cleverbot.com/')


def writemsg(browser,msg):
    #this function writes the message on cleverbot page in the window of browser object
    button = browser.find_element_by_css_selector('#avatarform > input.stimulus')
    button.click();
    button.send_keys(msg)
    button.send_keys(Keys.ENTER);

def readmsg(browser):
    #this function reads the last message of the bot from the chrome window of browser object
    time.sleep(4)
    txt = browser.find_element_by_css_selector("#line1");
    x = txt.text
    return x

#sending initial message msg to browser_1
msg = "Hello bot" #initialized message
writemsg(browser_1,msg)
print("Initializer message : "+msg)
msg = readmsg(browser_1)
print("Bot 1:"+msg)
count = 0

#making two bots talk to each other with while loop
while(True):
    writemsg(browser_2,msg)
    msg = readmsg(browser_2)
    print("Bot 2:"+msg)
    writemsg(browser_1,msg)
    msg = readmsg(browser_1)
    print("Bot 1:"+msg)
    count = count + 1
    if(count == 50):
        break
