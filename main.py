from random import randint
from warnings import catch_warnings
from vk_api import bot_longpoll
from messageProc import SpamProc, CommandsProc, sendMsg2id, loadPhoto2Vk    # importing message processing function
from vars import *     # importing variables of bot init
from recipients import recipients
import time
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from str_module import TextException
from dotenv import load_dotenv
import os




def main():

    load_dotenv()
    user_token = os.getenv("USER_TOKEN")
    user_id    = os.getenv("USER_ID")


    def captcha_handler(captcha):
        """ При возникновении капчи вызывается эта функция и ей передается объект
            капчи. Через метод get_url можно получить ссылку на изображение.
            Через метод try_again можно попытаться отправить запрос с кодом капчи
        """

        key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

        sendMsg2id(vkapi, user_id, 'send capcha here', [loadPhoto2Vk(captcha.get_url())])

        while True:
            try:
                event = vklongpoll.check()[0]
            except BaseException:
                continue
            if chatId != event.peer_id:
                continue
            key = event.message
            break

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)


    # log onto db
    recipients.update()



    while True:

        print('auth')

        try:

            vksession = vk_api.VkApi(token=user_token, captcha_handler=captcha_handler)
            vkapi = vksession.get_api()

            vklongpoll = VkLongPoll(vksession)
            # vkUpload = VkUpload(vksession)

        except BaseException:
            print('Auth failed')
            print(TextException())
            return 1

        print('\n\n\nBot has been strted.\n\n')


        try:

            # spaming loop
            while True:

                start_time = time.time()



                SpamProc(vkapi)



                # process commands
                while (time.time() - start_time) < sleep_timeout:

                    try:
                        event = vklongpoll.check()[0]
                    except BaseException:
                        continue

                    if event.type == VkEventType.MESSAGE_NEW and ( event.from_user ):

                        # get id
                        chatId = event.peer_id
                        print(chatId)
                        # read comands only from own dialog
                        if str(chatId) != str(user_id):
                            continue

                        # get message
                        userMsg = event.message
                        print(userMsg)
                        # if not command than skip
                        if not userMsg.startswith('!'):
                            continue
                        userMsg = userMsg[1:]

                        # here we are to process comands send to bot
                        CommandsProc(vkapi, userMsg, chatId)   

                    if (time.time() - start_time) >= sleep_timeout:
                        break

            

        # if vk is gay then restart connection
        except BaseException:   # vashe poxui
            print(TextException())
            print('\n\nBOT HAS BEEN RESTARTED\n\n')



# running script
if __name__ == "__main__":
	main()
