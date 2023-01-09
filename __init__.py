from mycroft import MycroftSkill, intent_file_handler


class IssIntroduction(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('introduction.iss.intent')
    def handle_introduction_iss(self, message):
        self.speak_dialog('introduction.iss')


def create_skill():
    return IssIntroduction()

