import rumps

class AwesomeStatusBarApp(rumps.App):

    current_user = None
    isStop = False

    def __init__(self, new_user):
        super(AwesomeStatusBarApp, self).__init__("🍪")
        self.menu = ["Stop", "Settings"]
        self.current_user = new_user

    @rumps.clicked("Stop")
    def onoff(self, sender):
        sender.state = not sender.state
        self.isStop = True

        
    @rumps.clicked("Settings")
    def prefs(self, _):
        self.current_user.setting_window()
        


if __name__ == '__main__':
    AwesomeStatusBarApp().run()
