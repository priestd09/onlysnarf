#!/usr/bin/python3

from OnlySnarf.settings import SETTINGS as settings

ONLYFANS_HOME_URL = 'https://onlyfans.com/'
ONLYFANS_SETTINGS_URL = "https://onlyfans.com/my/settings"
ONLYFANS_USERS_ACTIVE_URL = "https://onlyfans.com/my/subscribers/active"
SEND_BUTTON_XPATH = "//button[@type='submit' and @class='g-btn m-rounded']"
SEND_BUTTON_CLASS = "g-btn.m-rounded"
SEND_BUTTON_CLASS2 = "button.g-btn.m-rounded"
LIVE_BUTTON_CLASS = "b-make-post__streaming-link"
TWITTER_LOGIN0 = "//a[@class='g-btn m-rounded m-flex m-lg']"
TWITTER_LOGIN1 = "//a[@class='g-btn m-rounded m-flex m-lg btn-twitter']"
TWITTER_LOGIN2 = "//a[@class='btn btn-default btn-block btn-lg btn-twitter']"
USERNAME_XPATH = "//input[@id='username_or_email']"
PASSWORD_XPATH = "//input[@id='password']"
MESSAGE_INPUT_CLASS = ".form-control.b-chat__message-input"
MESSAGE_CONFIRM = "g-btn.m-rounded.b-chat__btn-submit"
MONTHS_INPUT = "form-control.b-fans__trial__select"
DISCOUNT_INPUT = "form-control.b-fans__trial__select"
DISCOUNT_TEXT = "form-control.b-fans__trial__select"
DISCOUNT_USER_BUTTONS = "g-btn.m-rounded.m-border.m-sm"
DISCOUNT_USER_BUTTONS1 = "g-btn.m-rounded"
DISCOUNT_USERS = "g-btn.m-rounded.m-border.m-sm"
DISCOUNT_USERS_ = "b-users__item.m-fans"
EXPIRATION = "g-btn.m-flat.b-make-post__expire-period-btn"
EXPIRATION2 = "button.g-btn.m-flat.b-make-post__expire-period-btn"
EXPIRATION_PERIODS = "b-make-post__expire__label"
EXPIRATION_PERIODS2 = "button.b-make-post__expire__label"
EXPIRATION_SAVE = "g-btn.m-rounded.js-make-post-poll-duration-save"
EXPIRATION_SAVE2 = "button.g-btn.m-rounded.js-make-post-poll-duration-save"
EXPIRATION_CANCEL = "g-btn.m-rounded.m-border"
EXPIRATION_CANCEL2 = "button.g-btn.m-rounded.m-border"
ONLYFANS_TWEET = "//label[@for='new_post_tweet_send']"
ONLYFANS_UPLOAD_PHOTO = "fileupload_photo"
ONLYFANS_UPLOAD_MESSAGE_PHOTO = "cm_fileupload_photo"
ONLYFANS_USER_COUNT = "l-sidebar__user-data__item__count"
ONLYFANS_USERS_IDS = "a.g-btn.m-rounded.m-border.m-sm"
ONLYFANS_USERS_STARTEDS = "b-fans__item__list__item"
ONLYFANS_USERS = "g-user-name__wrapper"
ONLYFANS_USERSNAMES = "g-user-username"
ONLYFANS_POST_TEXT_ID = "new_post_text_input"
ONLYFANS_PRICE = "b-chat__btn-set-price"
ONLYFANS_PRICE2 = "button.b-chat__btn-set-price"
ONLYFANS_PRICE_INPUT = "form-control.g-input"
ONLYFANS_PRICE_INPUT2 = ".form-control.g-input"
ONLYFANS_PRICE_INPUT3 = "input.form-control.g-input"
ONLYFANS_PRICE_INPUT4 = "input.form-control.g-input"
ONLYFANS_PRICE_CLICK = "g-btn.m-rounded"
ONLYFANS_PRICE_CLICK2 = "button.g-btn.m-rounded"
ONLYFANS_CHAT_URL = "https://onlyfans.com/my/chats/chat"
ONLYFANS_UPLOAD_BUTTON = "g-btn.m-rounded.m-border"
ONLYFANS_MESSAGE_SEND_BUTTON = "g-btn.m-rounded.b-chat__btn-submit"
ONLYFANS_MESSAGES_FROM = "m-from-me"
ONLYFANS_MESSAGES_ALL = "b-chat__message__text"
ONLYFANS_MESSAGES = "b-chat__message__text"
ONLYFANS_MORE = "g-btn.m-flat.b-make-post__more-btn"
ONLYFANS_MORE2 = "button.g-btn.m-flat.b-make-post__more-btn"
# ONLYFANS_MORE = "g-btn.m-flat.b-make-post__more-btn.has-tooltip.v-tooltip-open"
SCHEDULE = "g-btn.m-flat.b-make-post__datepicker-btn"
SCHEDULE2 = "button.g-btn.m-flat.b-make-post__datepicker-btn"
SCHEDULE_EXISTING_DATE = "vdatetime-calendar__current--month"
SCHEDULE_EXISTING_DATE2 = ".vdatetime-calendar__current--month"
SCHEDULE_EXISTING_DATE3 = "div.vdatetime-calendar__current--month"
SCHEDULE_EXISTING_DATE4 = "vdatetime-popup__date"
SCHEDULE_EXISTING_DATE5 = "div.vdatetime-popup__date"
SCHEDULE_NEXT_MONTH = "vdatetime-calendar__navigation--next"
SCHEDULE_NEXT_MONTH2 = "button.vdatetime-calendar__navigation--next"
SCHEDULE_DAYS = "vdatetime-calendar__month__day"
SCHEDULE_DAYS2 = "button.vdatetime-calendar__month__day"
SCHEDULE_SAVE = "g-btn.m-rounded"
SCHEDULE_SAVE2 = "button.g-btn.m-rounded"
SCHEDULE_HOURS = "vdatetime-time-picker__item.vdatetime-time-picker__item"
SCHEDULE_HOURS2 = "button.vdatetime-time-picker__item.vdatetime-time-picker__item"
SCHEDULE_MINUTES = "vdatetime-time-picker__item"
SCHEDULE_MINUTES2 = "button.vdatetime-time-picker__item"
POLL = "g-btn.m-flat.b-make-post__voting-btn"
POLL2 = "g-btn.m-flat.b-make-post__voting-btn.has-tooltip"
POLL3 = "button.g-btn.m-flat.b-make-post__voting-btn"
POLL4 = "button.g-btn.m-flat.b-make-post__voting-btn.has-tooltip"
POLL_DURATION = "g-btn.m-flat.b-make-post__voting__duration"
POLL_DURATION2 = "button.g-btn.m-flat.b-make-post__voting__duration"
POLL_DURATION3 = "g-btn.m-rounded.js-make-post-poll-duration-save"
POLL_DURATION4 = "button.g-btn.m-rounded.js-make-post-poll-duration-save"
POLL_ADD_QUESTION = "g-btn.m-flat.new_vote_add_option"
POLL_ADD_QUESTION2 = "button.g-btn.m-flat.new_vote_add_option"
POLL_SAVE = "g-btn.m-rounded"
POLL_SAVE2 = "button.g-btn.m-rounded"
POLL_CANCEL = "b-dropzone__preview__delete"
POLL_INPUT_XPATH = "//input[@class='form-control']"
REMEMBERME_CHECKBOX_XPATH = "//input[@id='remember']"

ONLYFANS_ELEMENTS = [
    {
        "name": "confirm",
        "className": [MESSAGE_CONFIRM],
        "text": [],
        "id": []
    },
    {
        "name": "loginCheck",
        "className": [LIVE_BUTTON_CLASS],
        "text": [],
        "id": []
    },
    {
        "name": "post",
        "className": [SEND_BUTTON_CLASS, SEND_BUTTON_CLASS2],
        "text": ["Post"],
        "id": []
    },
    {
        "name": "uploadImage",
        "className": "",
        "text": [],
        "id": [ONLYFANS_UPLOAD_PHOTO]
    },
    {
        "name": "uploadImageMessage",
        "className": "",
        "text": [],
        "id": [ONLYFANS_UPLOAD_MESSAGE_PHOTO]
    },
    {
        "name": "errorUpload",
        "className": "g-btn.m-rounded.m-border",
        "text": [],
        "id": []
    },
    {
        "name": "poll",
        "className": [POLL, POLL2, POLL3, POLL4],
        "text": ["<svg class=\"g-icon\" aria-hidden=\"true\"><use xlink:href=\"#icon-more\" href=\"#icon-more\"></use></svg>"],
        "id": []
    },
    {
        "name": "pollCancel",
        "className": [POLL_CANCEL],
        "text": ["Cancel"],
        "id": []
    },
    {
        "name": "pollDuration",
        "className": [POLL_DURATION, POLL_DURATION2, POLL_DURATION3, POLL_DURATION4],
        "text": [],
        "id": []
    },
    {
        "name": "pollDurations",
        "className": [EXPIRATION_PERIODS],
        "text": [],
        "id": []
    },
    {
        "name": "pollSave",
        "className": [POLL_SAVE, POLL_SAVE2],
        "text": ["Save"],
        "id": []
    },
    {
        "name": "pollQuestionAdd",
        "className": [POLL_ADD_QUESTION, POLL_ADD_QUESTION2],
        "text": [],
        "id": []
    },
    {
        "name": "moreOptions",
        "className": [ONLYFANS_MORE, ONLYFANS_MORE2],
        "text": [],
        "id": []
    },
    {
        "name": "expirationAdd",
        "className": [EXPIRATION, EXPIRATION2],
        "text": [],
        "id": []
    },
    {
        "name": "expirationPeriods",
        "className": [EXPIRATION_PERIODS, EXPIRATION_PERIODS2],
        "text": [],
        "id": []
    },
    {
        "name": "expirationSave",
        "className": [EXPIRATION_SAVE, EXPIRATION_SAVE2],
        "text": [],
        "id": []
    },
    {
        "name": "expirationCancel",
        "className": [EXPIRATION_CANCEL, EXPIRATION_CANCEL2],
        "text": [],
        "id": []
    },
    {
        "name": "discountUserButtons",
        "className": [DISCOUNT_USER_BUTTONS1],
        "text": ["Save"],
        "id": []
    },
    {
        "name": "discountUsers",
        "className": [DISCOUNT_USERS_],
        "text": ["Save"],
        "id": []
    },
    {
        "name": "priceClick",
        "className": [ONLYFANS_PRICE_CLICK, ONLYFANS_PRICE_CLICK2],
        "text": [],
        "id": []
    },
    {
        "name": "priceEnter",
        "className": [ONLYFANS_PRICE_INPUT, ONLYFANS_PRICE_INPUT2, ONLYFANS_PRICE_INPUT3, ONLYFANS_PRICE_INPUT4],
        "text": ["Free"],
        "id": []
    },
    {
        "name": "scheduleAdd",
        "className": [SCHEDULE, SCHEDULE2],
        "text": [],
        "id": []
    },
    {
        "name": "scheduleNextMonth",
        "className": [SCHEDULE_NEXT_MONTH, SCHEDULE_NEXT_MONTH2],
        "text": [],
        "id": []
    },
    {
        "name": "scheduleDate",
        "className": [SCHEDULE_EXISTING_DATE, SCHEDULE_EXISTING_DATE2, SCHEDULE_EXISTING_DATE3, SCHEDULE_EXISTING_DATE4, SCHEDULE_EXISTING_DATE5],
        "text": [],
        "id": []
    },
    {
        "name": "scheduleMinutes",
        "className": [SCHEDULE_MINUTES, SCHEDULE_MINUTES2],
        "text": [],
        "id": []
    },
    {
        "name": "scheduleHours",
        "className": [SCHEDULE_HOURS, SCHEDULE_HOURS2],
        "text": [],
        "id": []
    },
    {
        "name": "scheduleDays",
        "className": [SCHEDULE_DAYS, SCHEDULE_DAYS2],
        "text": [],
        "id": []
    },
    {
        "name": "scheduleSave",
        "className": [SCHEDULE_SAVE, SCHEDULE_SAVE2],
        "text": ["Save"],
        "id": []
    },
    {
        "name": "messagesAll",
        "className": [ONLYFANS_MESSAGES_ALL],
        "text": [],
        "id": []
    },
    {
        "name": "messagesFrom",
        "className": [ONLYFANS_MESSAGES_FROM],
        "text": [],
        "id": []
    },
    {
        "name": "usersUsernames",
        "className": [ONLYFANS_USERSNAMES],
        "text": [],
        "id": []
    },
    {
        "name": "usersUsers",
        "className": [ONLYFANS_USERS],
        "text": [],
        "id": []
    },
    {
        "name": "usersStarteds",
        "className": [ONLYFANS_USERS_STARTEDS],
        "text": [],
        "id": []
    },
    {
        "name": "userIds",
        "className": [ONLYFANS_USERS_IDS],
        "text": [],
        "id": []
    },
    {
        "name": "userCount",
        "className": [ONLYFANS_USER_COUNT],
        "text": [],
        "id": []
    },
    {
        "name": "discountUserButtons",
        "className": [DISCOUNT_USER_BUTTONS],
        "text": [],
        "id": []
    },
    {
        "name": "messageInput",
        "className": [MESSAGE_INPUT_CLASS],
        "text": [],
        "id": []
    },
    {
        "name": "messages",
        "className": [ONLYFANS_MESSAGES],
        "text": [],
        "id": []
    }
]

# represents elements the webdriver sortof looks for
class Element:
    def __init__(self, name=None, classes=[], text=[], id=[]):
        self.name = name
        self.classes = classes
        self.text = text
        self.id = id

    def getClass(self):
        if self.classes and len(self.classes) > 0:
            return self.classes[0]
        return ""

    def getClasses(self):
        return self.classes or []

    def getText(self):
        if self.text and len(self.text) > 0:
            return self.text[0]
        return ""

    def getTexts(self):
        return self.text or []

    @staticmethod
    def get_element_by_name(name):
        settings.devPrint("getting element: {}".format(name))
        if name == None:
            settings.maybePrint("Error: Missing Element Name")
            return None
        global ONLYFANS_ELEMENTS
        for element in ONLYFANS_ELEMENTS:
            # element = Element(name=element["name"], classes=element["className"], text=element["text"], id=element["id"])
            if str(element["name"]) == str(name):
                settings.devPrint("prepped ele: {}".format(element["name"]))
                return Element(name=element["name"], classes=element["className"], text=element["text"], id=element["id"])
        settings.devPrint("Warning: Missing Element Fetch - {}".format(name))
        return None