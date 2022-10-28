from dataclasses import dataclass


@dataclass
class Config:
    def __init__(self,
                 username, dob,
                 q1, a1,
                 q2, a2,
                 q3, a3,
                 check_interval,
                 tgbot_token, tgbot_chat_id, step_sleep, webdriver_addr):
        """
        Config class
        :param username: email address
        :param dob: date of birth
        :param q1: question 1
        :param a1: answer 1
        :param q2: question 2
        :param a2: answer 2
        :param q3: question 3
        :param a3: answer 3
        :param check_interval:
        :param tgbot_token:
        :param tgbot_chat_id:
        :param step_sleep: selenium step sleep
        :param webdriver_addr:
        """
        self.remote_driver = False
        self.tgbot_enable = False
        self.password_length = 10  # 新密码长度
        self.username = username
        self.dob = dob
        self.answer = {q1: a1, q2: a2, q3: a3}
        self.check_interval = check_interval
        self.webdriver = webdriver_addr
        self.step_sleep = step_sleep
        if tgbot_chat_id != "" and tgbot_token != "":
            self.tgbot_enable = True
            self.tgbot_chat_id = tgbot_chat_id
            self.tgbot_token = tgbot_token
        if webdriver_addr != "local":
            self.remote_driver = True

    def __str__(self) -> str:
        return f"Username: {self.username}\n" \
               f"DOB: {self.dob}\n" \
               f"Answer: {self.answer}\n" \
               f"Check Interval: {self.check_interval}\n" \
               f"Webdriver: {self.webdriver}\n" \
               f"Step Sleep: {self.step_sleep}\n" \
               f"Remote Driver: {self.remote_driver}\n" \
               f"Telegram Bot: {self.tgbot_enable}\n" \
               f"Password Length: {self.password_length}"
