def load_telegram_addess_token():
    with open('telegram_token') as f:
        return f.read().strip()

def set_web_hook():
    result = "https://api.telegram.org/bot{}/setWebhook?url=".format(
            load_telegram_addess_token())
    print(result)

def construct_link(action):
    result = "https://api.telegram.org/bot{}/{}".format(
            load_telegram_addess_token(), action)
    print(result)


if __name__ == '__main__':
    set_web_hook()
