# exceptions base
from mTwit.Notification_Ui import NotificationWindow as Ew
from mTwit.Notification_Ui import NotificationMode as Mode


class ErrorNotification(Exception):
    """MTwitでのError基底クラス"""

    def __init__(self, reason, *args):
        self.reason = reason
        super().__init__(*args)

    def show(self):  # Delete this
        """Errorの通知を表示する"""
        Ew(time=2000, message=self.reason).show(Mode.ERROR)

    def __str__(self):
        return self.reason

