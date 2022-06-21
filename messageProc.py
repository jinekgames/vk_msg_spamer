from recipients import recipients
from str_module import TextException, contain5, end5, i5, choo5e, endswith_list, _contain5, _end5, replace_layout, startswith_list, dicklist_search

import time
import requests
import datetime
import calendar
import smtplib

import random
random.seed(version=2)

import vk_api
from vk_api.utils import get_random_id


requestSession = requests.Session()





# some static variables
class SomeVars:
    timers = {}
    timeoutSec = 30
    chats = {}



def sendMsg2id(vkapi, id, msg, attachments=[]):
    cur_time = time.time()
    if (not id in SomeVars.timers) or (cur_time - SomeVars.timers[id] > SomeVars.timeoutSec):
        SomeVars.timers[id] = cur_time
        rtrn_msg = ''
        try:
            vkapi.messages.send(peer_id=int(id), message=msg, random_id=get_random_id(), attachment=attachments)
            rtrn_msg = 'готово, с вас three hundred bucks'
        except vk_api.exceptions.ApiError:
            print("ERROR SENDING MSG TO " + str(id))
            TextException()
        return rtrn_msg

def loadPhoto2Vk(url, upload):
    image = requestSession.get(url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    return 'photo{}_{}'.format(photo['owner_id'], photo['id'])



# send msgs to users from db
def SpamProc(vkapi):

    recips = recipients.get()
    cur_time = time.time()

    for id in recips:

        if ((not id in SomeVars.timers) or (cur_time - SomeVars.timers[id] > int(recips[id]['timer']) * 60)) and int(recips[id]['on']):
            sendMsg2id(vkapi, id, choo5e(recips[id]['msgs']))
            print("sent msg to", id, "\n")



def CommandsProc(vkapi, msg: str, chatId: int):

    if msg.startswith('setupspam'):

        msg = msg.split('\n')
        cmds = msg[0].split(' ')
        recip  = cmds[1]
        status = int(cmds[2])

        if not status:
            try:
                old_set = recipients.getSetting(recip)
                old_set['on'] = 0
                recipients.setSetting(recip, old_set)
            except BaseException:
                print(TextException())

        else:
            timer = int(cmds[3])

            old_set = recipients.getSetting(recip)
            if not old_set:
                old_set = {
                    "on": 0,
                    'timer': 15,
                    'msgs': ['але']
                }

            old_set['on']    = status
            old_set['timer'] = timer
            if len(msg) > 1:
                old_set['msgs'] = msg[1:]
            recipients.setSetting(recip, old_set)

        recipients.forceUpdate()
        