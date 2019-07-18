# exceptions base
from mTwit.ui import NotificationWindow
from mTwit.notifications import NotificationKind, notify
from debtcollector import removals


class ErrorNotification(Exception):
    """MTwitでのError基底クラス"""

    def __init__(self, reason, *args):
        self.reason = reason
        super().__init__(*args)

    @removals.remove
    def show(self):  # Delete this
        self.notify()

    def notify(self):
        notify(NotificationKind.ERROR, self.reason)

    def __str__(self):
        return self.reason
