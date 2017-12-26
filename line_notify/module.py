"""
A Simple Wrapper for LINE Messenger Notify
"""
import os.path
import requests

API_URI = "https://notify-api.line.me/api/notify"


class LineNotify:
    def __init__(self, access_token):
        """Example:

            notify = LineNotify(ACCESS_TOKEN)

        :param access_token:
        """
        self.accessToken = access_token
        self.headers = {"Authorization": "Bearer " + access_token}

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
        files = {}
        params = {"message": message}

        if image_path and os.path.isfile(image_path):
            files = {"imageFile": open(image_path, "rb")}

        if sticker_id and package_id:
            params = {**params, "stickerId": sticker_id, "stickerPackageId": package_id}

        requests.post(API_URI, headers=self.headers, params=params, files=files)
