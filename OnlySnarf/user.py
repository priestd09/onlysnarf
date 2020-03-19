#!/usr/bin/python3
# 3/25/2019: Skeetzo
# User Class

import json
import time
import os
import threading
from datetime import datetime
from re import sub
from decimal import Decimal
##
from OnlySnarf.settings import SETTINGS as settings

class User:

    def __init__(self, data):
        data = json.loads(json.dumps(data))
        # print(data)
        self.name = data.get('name') or ""
        self.username = data.get('username') or ""
        self.id = data.get('id') or ""
        self.messages_from = data.get('messages_from') or []
        self.messages_to = data.get('messages_to') or []
        self.messages = data.get('messages') or []
        self.preferences = data.get('preferences') or []
        self.last_messaged_on = data.get('last_messaged_on')
        self.sent_images = data.get('sent_images') or []
        self.subscribed_on = data.get('subscribed_on')
        self.isFavorite = data.get('isFavorite') or False
        self.statement_history = data.get('statement_history') or []
        self.started = data.get('started')
        ###### fucking json #####
        self.messages_from = ",".join(self.messages_from).split(",")
        self.messages_to = ",".join(self.messages_from).split(",")
        self.messages = ",".join(self.messages_from).split(",")
        self.preferences = ",".join(self.messages_from).split(",")
        self.sent_images = ",".join(self.messages_from).split(",")
        self.statement_history = ",".join(self.messages_from).split(",")
        #########################
        try:
            settings.devPrint("User: {} - {} - {}".format(self.name, self.username, self.id))
        except Exception as e:
            print(e)
            settings.devPrint(e)
            settings.devPrint("User: {}".format(self.id))

    def discount(self, Driver=None, discount={}):
        amount = getattr(discount, "amount")
        months = getattr(discount, "months")
        if not amount: amount = input("Discount: ")
        if not months: months = input("Months: ")
        discount = {"amount":amount,"months":months}
        successful = Driver.discount_user(self.username, discount)
        return successful

    def message(self, Driver=None, message=None):
        if not Driver: Driver = Driver.get()
        if str(self.username) == "": return print("User Error: Missing Message Username")
        print("Messaging: {}".format(self.username))
        successful = Driver.message(self.username, message)
        if not successful: return False
        successful = User.enter_message(Driver, message)
        if not successful: return False
        print("Messaged: {}".format(self.username))

    @staticmethod
    def message(Driver=None, username="", message=None):
        user = User()
        setattr(user, "username", username)
        user.message(Driver=Driver, message=message)

    @staticmethod
    def enter_message(Driver, message=None):
        try:
            print("Entering Message: {} - ${}".format(message, price))
            def enter_text(text):
                success = Driver.message_text(text)
                if not success: return False
                return True
            def enter_price(price):
                if path == "": return False
                if path != None and Decimal(sub(r'[^\d.]', '', price)) < settings.PRICE_MINIMUM:
                    print("Warning: Price Too Low, Free Image")
                    print("Price Minimum: ${}".format(settings.PRICE_MINIMUM))
                else:
                    success = Driver.message_price(price)
                    if not success: return False
                settings.debug_delay_check()
                return True
            def enter_file(path):
                if path == "": return False
                image_name = os.path.basename(path)
                if str(image_name) in self.sent_images:
                    print("Error: Image Already Sent: {} -> {}".format(image_name, self.username))
                    return False
                success = Driver.message_files(path)
                if not success: return False
                if str(settings.DEBUG) != "True":
                    self.sent_images.append(str(image_name))
                settings.debug_delay_check()
                return True
            def confirm():
                success = Driver.message_confirm()
                if not success: return False
                return True
            if not enter_text(message.text): return False # not allowed to fail
            enter_price(message.price) # allowed to fail
            for file in message.files:
                enter_file(file.get_path()) # allowed to fail
            if not confirm(): return False # not allowed to fail
            print("Message Entered")
            return True
        except Exception as e:
            settings.maybePrint(e)
            return False

    def equals(self, user):
        # print(str(user.username)+" == "+str(self.username))
        if user.username == self.username:
            return True
        return False

    def toJSON(self):
        return json.dumps({
            "name":str(self.name),
            "username":str(self.username),
            "id":str(self.id),
            "messages_from":str(self.messages_from),
            "messages_to":str(self.messages_to),
            "messages":str(self.messages),
            "preferences":str(self.preferences),
            "last_messaged_on":str(self.last_messaged_on),
            "sent_images":str(self.sent_images),
            "subscribed_on":str(self.subscribed_on),
            "isFavorite":str(self.isFavorite)
        })

    # greet user if new
    def greet(self):
        if self.last_messaged_on == None:
            return print("Error: User Not New")
        print("Sending User Greeting: {}".format(self.username))
        # self.send_message(message=settings.DEFAULT_GREETING)
        User.enter_message(Driver=None, message=settings.DEFAULT_GREETING)

    # send refresher message to user
    def refresh(self):
        if self.last_messaged_on == None:
            print("Warning: Never Greeted, Greeting Instead")
            return self.greet()
        elif (timedelta(self.last_messaged_on)-timedelta(datetime())).days < 30:
            return print("Error: Refresher Date Too Early - {}".format((timedelta(self.last_messaged_on)-timedelta(datetime())).days))
        print("Sending User Refresher: {}".format(self.username))
        # self.send_message(message=settings.user_DEFAULT_REFRESHER)
        User.enter_message(Driver=None, message=settings.user_DEFAULT_REFRESHER)

    # saves chat log to user
    def readChat(self, Driver):
        print("Reading Chat: {} - {}".format(self.username, self.id))
        messages = Driver.read_user_messages(self.id)
        self.messages = messages[0]
        # self.messages_and_timestamps = messages[1]
        self.messages_to = messages[2]
        self.messages_from = messages[3]
        settings.maybePrint("Chat Read: {} - {}".format(self.username, self.id))

    # saves statement / payment history
    def statementHistory(self, Driver, history):
        print("Reading Statement History: {} - {}".format(self.username, self.id))
        Driver.read_statements(user=self.id)

    # sets as favorite
    def favor(self):
        print("Favoring: {}".format(self.username))
        self.isFavorite = True

    # unsets as favorite
    def unfavor(self):
        print("Unfavoring: {}".format(self.username))
        self.isFavorite = False

    @staticmethod
    def get_all_users(Driver):
        return User.get_active_users(Driver)

    # gets users from local or refreshes from onlyfans.com
    @staticmethod
    def get_active_users(Driver):
        if str(settings.PREFER_LOCAL) == "True": return read_users_local()
        active_users = []
        users = Driver.users_get()
        for user in users:
            try:
                user = User(user)
                user = skipUserCheck(user)
                if user is None: continue
                active_users.append(user)
            except Exception as e:
                settings.maybePrint(e)
        settings.maybePrint("pruning memberlist")
        settings.maybePrint("users: {}".format(len(active_users)))
        write_users_local(users=active_users)
        settings.PREFER_LOCAL = True
        return active_users

    @staticmethod
    def get_user_by_username(Driver, username):
        if not username or username == None:
            print("Error: Missing Username")
            return None
        users = read_users_local()
        for user in users:
            if str(user.username) == "@u"+str(username) or str(user.username) == "@"+str(username) or str(user.username) == str(username):
                settings.maybePrint("Found User: Local")
                return user
        users = User.get_all_users(Driver)
        for user in users:
            if str(user.username) == "@u"+str(username) or str(user.username) == "@"+str(username) or str(user.username) == str(username):
                settings.maybePrint("Found User: Members")
                return user
        print("Error: Missing User by Username - {}".format(username))
        return None

    @staticmethod
    def get_favorite_users(Driver):
        settings.maybePrint("Getting Fav Users")
        users = User.get_all_users(Driver)
        favUsers = []
        favorites = ",".join(str(settings.USERS_FAVORITE))
        for user in users:
            if user in favorites:
                settings.maybePrint("Fav User: {}".format(user.username))
                user = skipUserCheck(user)
                if user is None: continue
                favUsers.append(user)
        return favUsers

    # returns users that have no messages sent to them
    @staticmethod
    def get_new_users(Driver):
        settings.maybePrint("Getting New Users")
        users = User.get_all_users(Driver)
        newUsers = []
        date_ = datetime.today() - timedelta(days=10)
        for user in users:
            started = datetime.strptime(user.started,"%b %d, %Y")
            # settings.maybePrint("date: "+str(date_)+" - "+str(started))
            if started < date_: continue
            settings.maybePrint("New User: {}".format(user.username))
            user = skipUserCheck(user)
            if user is None: continue
            newUsers.append(user)
        return newUsers

    @staticmethod
    def get_never_messaged_users(Driver):
        settings.maybePrint("Getting New Users")
        update_chat_logs(Driver)
        users = User.get_all_users(Driver)
        newUsers = []
        for user in users:
            if len(user.messages_to) == 0:
                settings.maybePrint("Never Messaged User: {}".format(user.username))
                user = skipUserCheck(user)
                if user is None: continue
                newUsers.append(user)
        return newUsers

    @staticmethod
    def get_recent_users(Driver):
        settings.maybePrint("Getting Recent Users")
        users = User.get_all_users(Driver)
        i = 0
        users_ = []
        for user in users:
            settings.maybePrint("Recent User: {}".format(user.username))
            user = skipUserCheck(user)
            if user is None: continue
            users_.append(user)
            i += 1
            if i == settings.RECENT_USER_COUNT:
                return users_
        return users_

#######################################################################################

def delayForThirty():
    settings.maybePrint("30...")
    time.sleep(10)
    settings.maybePrint("20...")
    time.sleep(10)
    settings.maybePrint("10...")
    time.sleep(7)
    settings.maybePrint("3...")
    time.sleep(1)
    settings.maybePrint("2...")
    time.sleep(1)
    settings.maybePrint("1...")
    time.sleep(1)

# gets a list of all subscribed user_ids from local txt
def read_users_local():
    settings.maybePrint("Getting Local Users")
    users = []
    users_ = []
    try:
        with open(settings.USERS_PATH) as json_file:  
            users = json.load(json_file)['users']
        settings.maybePrint("Loaded:")
        for user in users:
            try:
                users_.append(User(json.loads(user)))
            except Exception as e:
                settings.maybePrint(e)
        return users_
    except Exception as e:
        settings.maybePrint(e)
    return users_

def skipUserCheck(user):
    if str(settings.SKIP_USERS) == "None":
        settings.SKIP_USERS = []
    if str(user.id).lower() in settings.SKIP_USERS or str(user.username).lower() in settings.SKIP_USERS:
        settings.maybePrint("skipping: {}".format(user.username))
        return None
    return user

# writes user list to local txt
def write_users_local(users=None):
    if users is None:
        users = User.get_all_users()
    if len(users) == 0:
        settings.maybePrint("Skipping: Local Users Save - No Users")
        return
    print("Saving Users Locally")
    settings.maybePrint("local users path: "+str(settings.USERS_PATH))
    data = {}
    data['users'] = []
    for user in users:
        if str(settings.DEBUG) == "True":
            settings.maybePrint("Saving: "+str(user.username))
        data['users'].append(user.toJSON())
    try:
        with open(settings.USERS_PATH, 'w') as outfile:  
            json.dump(data, outfile, indent=4, sort_keys=True)
    except FileNotFoundError:
        print("Error: Missing Local Users")
    except OSError:
        print("Error: Missing Local Path")