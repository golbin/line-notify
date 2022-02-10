"""
A Simple Wrapper for LINE Messenger Notify
"""
import os.path
import requests

API_URI = "https://notify-api.line.me/api/notify"


class LineNotify:
    def __init__(self, access_token, name=None):
        """Example:

            notify = LineNotify(ACCESS_TOKEN)
            notify = LineNotify(ACCESS_TOKEN, name="CLAIR")

        :param access_token:
        :param name: If name is set, send a message with the name; [NAME] blah blah..
        """
        self.name = name
        self.accessToken = access_token

        if access_token:
            self.enable = True
            self.headers = {"Authorization": "Bearer " + access_token}
        else:
            self.enable = False
            self.headers = {}

    def on(self):
        """Enable notify"""
        self.enable = True

    def off(self):
        """Disable notify"""
        self.enable = False

    def format(self, message):
        if self.name:
            message = '[{0}] {1}'.format(self.name, message)

        return message

    def send(self, message, image_path=None, sticker_id=None, package_id=None):
        """Examples:

            notify.send("text test")
            notify.send("image test", image_path='./test.jpg')
            notify.send("sticker test", sticker_id=283, package_id=4)
            notify.send("image & sticker test", image_path='./test.jpg', sticker_id=283, package_id=4)

        :param message: string
        :param image_path: string
        :param sticker_id: integer
        :param package_id: integer
        :return:
        """
        if not self.enable:
            return

        files = {}
        params = {"message": self.format(message)}

        if image_path and os.path.isfile(image_path):
            files = {"imageFile": open(image_path, "rb")}

        if sticker_id and package_id:
            params = {**params, "stickerId": sticker_id, "stickerPackageId": package_id}

        return requests.post(API_URI, headers=self.headers, params=params, files=files)

