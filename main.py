import rumps
import time
from datetime import datetime, timedelta
import _thread

rumps.debug_mode(True)  # turn on command line logging information for development - default is off

class StrainElf:
    def __init__(self):
        self.app = rumps.App("Strainy the Elf", icon='normal_eye.ico')
        self.interval_minutes = 20
        self.last_break = datetime.strftime(datetime.now(), '%d %B %Y %I:%M%p')
        self.next_break = datetime.strftime(datetime.now()  + timedelta(minutes=self.interval_minutes), '%d %B %Y %I:%M%p')
        self.menu = self.app.menu = [
            rumps.MenuItem('Back from break'),
            rumps.MenuItem(f"Next break @ {self.next_break.split()[-1]}"),
        ]


    def set_next_break(self):
        self.next_break = datetime.strftime(datetime.now()  + timedelta(minutes=self.interval_minutes), '%d %B %Y %I:%M%p')


    def reset_timer(self):
        self.last_break = datetime.strftime(datetime.now(), '%d %B %Y %I:%M%p')
        self.next_break = None


    def alert_take_break(self):
        message = f"Time to relax the eyes."
        self.app.icon = 'redeye.ico'
        rumps.notification(title='Break Time',subtitle='Time to take a break', message=message)
        self.reset_timer()
    

    def check_time(self):
        while True:
            if datetime.strftime(datetime.now(), '%d %B %Y %I:%M%p') == self.next_break:
                self.alert_take_break()
            else:
                time.sleep(60)


    def run(self):
        _thread.start_new_thread(self.check_time)
        self.app.run()


@rumps.clicked("Back from break")
def break_taken(sender):
    elf.app.icon = 'normal_eye.ico'
    elf.set_next_break()


if __name__ == "__main__":

    elf = StrainElf()

    elf.run()