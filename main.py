import user
import bar
import time


new_user = user.User()

new_bar = bar.AwesomeStatusBarApp(new_user)
new_bar.run()
while new_bar.isStop == False:

    new_user.create_window_task()
    time.sleep(new_user.delay)

