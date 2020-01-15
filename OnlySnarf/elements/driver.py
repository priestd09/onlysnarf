# general driver elements

ELEMENTS = [
    ### login
    {
        "name": "login",
        "classes": [],
        "text": [],
        "id": []
    },
    # username
    {
        "name": "loginUsername",
        "classes": [],
        "text": [],
        "id": []
    },
    # password
    {
        "name": "loginPassword",
        "classes": [],
        "text": [],
        "id": []
    },
    {
        "name": "loginCheck",
        "classes": ["b-make-post__streaming-link"],
        "text": [],
        "id": []
    },
    ### upload
    # send
    {
        "name": "new_post",
        "classes": ["g-btn.m-rounded", "button.g-btn.m-rounded"],
        "text": ["Post"],
        "id": []
    },


    # record voice
    {
        "name": "recordVoice",
        "classes": [None],
        "text": [],
        "id": []
    },
    # post price
    {
        "name": "post_price",
        "classes": [None],
        "text": [],
        "id": []
    },
    # post price cancel
    {
        "name": "post_price_cancel",
        "classes": [None],
        "text": [],
        "id": []
    },
    # post price save
    {
        "name": "post_price_save",
        "classes": [None],
        "text": [],
        "id": []
    },
    # go live
    {
        "name": "go_live",
        "classes": [None],
        "text": [],
        "id": []
    },
    # 

    # upload image file
    {
        "name": "image_upload",
        "classes": ["button.g-btn.m-rounded.b-chat__btn-submit", "g-btn.m-rounded.b-chat__btn-submit"],
        "text": [],
        "id": ["fileupload_photo"],
        "tabIndex": 11,
        "from": "new_post"
    },
    # show more options # unnecessary w/ tabbing
    # {
    #     "name": "moreOptions",
    #     "classes": ["g-btn.m-flat.b-make-post__more-btn", "button.g-btn.m-flat.b-make-post__more-btn"],
    #     "text": [],
    #     "id": [],
    #     "tabIndex": None,
    #     "from": "load"
    # },
    # poll
    {
        "name": "poll",
        "classes": ["g-btn.m-flat.b-make-post__voting-btn", "g-btn.m-flat.b-make-post__voting-btn.has-tooltip", "button.g-btn.m-flat.b-make-post__voting-btn", "button.g-btn.m-flat.b-make-post__voting-btn.has-tooltip"],
        "text": ["<svg class=\"g-icon\" aria-hidden=\"true\"><use xlink:href=\"#icon-more\" href=\"#icon-more\"></use></svg>"],
        "id": []
    },
    # poll cancel
    {
        "name": "pollCancel",
        "classes": ["b-dropzone__preview__delete"],
        "text": ["Cancel"],
        "id": []
    },
    # poll duration
    {
        "name": "pollDuration",
        "classes": ["g-btn.m-flat.b-make-post__voting__duration", "button.g-btn.m-flat.b-make-post__voting__duration", "g-btn.m-rounded.js-make-post-poll-duration-save", "button.g-btn.m-rounded.js-make-post-poll-duration-save"],
        "text": [],
        "id": []
    },
    # duration tabs
    {
        "name": "pollDurations",
        "classes": ["b-make-post__expire__label"],
        "text": [],
        "id": []
    },
    # poll save duration
    {
        "name": "pollSave",
        "classes": ["g-btn.m-rounded", "button.g-btn.m-rounded"],
        "text": ["Save"],
        "id": []
    },
    # poll add question
    {
        "name": "pollQuestionAdd",
        "classes": ["g-btn.m-flat.new_vote_add_option", "button.g-btn.m-flat.new_vote_add_option"],
        "text": [],
        "id": []
    },

    # expiration
    {
        "name": "expirationAdd",
        "classes": ["g-btn.m-flat.b-make-post__expire-period-btn", "button.g-btn.m-flat.b-make-post__expire-period-btn"],
        "text": [],
        "id": []
    },
    # expiration periods (same for duration)
    {
        "name": "expirationPeriods",
        "classes": ["b-make-post__expire__label", "button.b-make-post__expire__label"],
        "text": [],
        "id": []
    },
    # expiration save
    {
        "name": "expirationSave",
        "classes": ["g-btn.m-rounded", "button.g-btn.m-rounded", "button.g-btn.m-rounded.js-make-post-poll-duration-save", "g-btn.m-rounded.js-make-post-poll-duration-save"],
        "text": ["Save"],
        "id": []
    },
    # expiration cancel
    {
        "name": "expirationCancel",
        "classes": ["g-btn.m-rounded.m-border", "button.g-btn.m-rounded.m-border"],
        "text": ["Cancel"],
        "id": []
    },
    # discount modal for user
    {
        "name": "discountUserButton",
        "classes": ["g-btn.m-rounded"],
        "text": ["Apply"],
        "id": []
    },
    # discount save for user
    {
        "name": "discountUsers",
        "classes": ["b-users__item.m-fans"],
        "text": ["Save"],
        "id": []
    },

    ## price
    # price add
    {
        "name": "priceClick",
        "classes": ["b-chat__btn-set-price", "button.g-btn.m-rounded"],
        "text": ["Save"],
        "id": []
    },
    # price enter (adds .00)
    {
        "name": "priceEnter",
        "classes": ["form-control.g-input", ".form-control.g-input", "input.form-control.g-input", "input.form-control.g-input"],
        "text": ["Free"],
        "id": []
    },

    # schedule add
    {
        "name": "scheduleAdd",
        "classes": ["g-btn.m-flat.b-make-post__datepicker-btn", "button.g-btn.m-flat.b-make-post__datepicker-btn"],
        "text": [],
        "id": []
    },
    # schedule next month
    {
        "name": "scheduleNextMonth",
        "classes": ["vdatetime-calendar__navigation--next", "button.vdatetime-calendar__navigation--next"],
        "text": [],
        "id": []
    },
    # schedule date
    {
        "name": "scheduleDate",
        "classes": ["vdatetime-calendar__current--month", "div.vdatetime-calendar__navigation > div.vdatetime-calendar__current--month", ".vdatetime-calendar__current--month", "div.vdatetime-calendar__current--month", "vdatetime-popup__date", "div.vdatetime-popup__date"],
        "text": [],
        "id": []
    },
    # schedule minutes
    {
        "name": "scheduleMinutes",
        "classes": ["vdatetime-time-picker__item", "button.vdatetime-time-picker__item"],
        "text": [],
        "id": []
    },
    # schedule hours
    {
        "name": "scheduleHours",
        "classes": ["vdatetime-time-picker__item.vdatetime-time-picker__item", "button.vdatetime-time-picker__item.vdatetime-time-picker__item"],
        "text": [],
        "id": []
    },
    # schedule days
    {
        "name": "scheduleDays",
        "classes": ["vdatetime-calendar__month__day", "button.vdatetime-calendar__month__day"],
        "text": [],
        "id": []
    },
    # schedule save
    {
        "name": "scheduleSave",
        "classes": ["g-btn.m-rounded", "button.g-btn.m-rounded"],
        "text": ["Save"],
        "id": []
    },

    ### message
    # message enter text
    {
        "name": "messageText",
        "classes": [".form-control.b-chat__message-input"],
        "text": [],
        "id": []
    },
    # message upload image
    {
        "name": "uploadImageMessage",
        "classes": ["g-btn.m-rounded.b-chat__btn-submit"],
        "text": [],
        "id": ["cm_fileupload_photo"],
        "tabIndex": None, # can't find
        "from": "load"
    },
    # upload error window close
    # tab probably closes error windows...
    {
        "name": "errorUpload",
        "classes": ["g-btn.m-rounded.m-border", "button.g-btn.m-rounded.m-border"],
        "text": ["Close"],
        "id": []
    },
    # messages all
    {
        "name": "messagesAll",
        "classes": ["b-chat__message__text"],
        "text": [],
        "id": []
    },
    # messages from user
    {
        "name": "messagesFrom",
        "classes": ["m-from-me"],
        "text": [],
        "id": []
    },
    # messages to user
    {
        "name": "usersUsernames",
        "classes": ["g-user-username"],
        "text": [],
        "id": []
    },
    ## Users
    # users
    {
        "name": "usersUsers",
        "classes": ["g-user-name__wrapper"],
        "text": [],
        "id": []
    },
    # users started dates
    {
        "name": "usersStarteds",
        "classes": ["b-fans__item__list__item"],
        "text": [],
        "id": []
    },
    # users ids
    {
        "name": "usersIds",
        "classes": ["a.g-btn.m-rounded.m-border.m-sm"],
        "text": [],
        "id": []
    },
    # users count
    {
        "name": "usersCount",
        "classes": ["l-sidebar__user-data__item__count"],
        "text": [],
        "id": []
    },
    # users discount buttons
    {
        "name": "discountUserButtons",
        "classes": ["g-btn.m-rounded.m-border.m-sm"],
        "text": [],
        "id": []
    }

]