# LINE Notify

A Simple Wrapper for LINE Messenger Notify

## Prerequisites

You have to generate access token on below site.

https://notify-bot.line.me

## Installation

```bash
pip install line_notify
```

## Usage

```python
from line_notify import LineNotify

ACCESS_TOKEN = "L52Z9PAH4kZ82JHSkfjTQ234c1cY2iAKdafaWYv77Ad"

notify = LineNotify(ACCESS_TOKEN)

notify.send("Text test")
notify.send("Image test", image_path='./test.jpg')
notify.send("Sticker test", sticker_id=283, package_id=4)
notify.send("Image & Sticker test", image_path='./test.jpg', sticker_id=283, package_id=4)
```

If you set the name, it send a message with the name; `[NAME] blah blah..`

```python
notify = LineNotify(ACCESS_TOKEN, name="CLAIR")

notify.send("Text test") # [CLAIR] Test test
```

If you set LineNotify off, then it won't send a message. (Default is `on`)

```python
notify.off()
notify.send("It won't be sent.")

notify.on()
notify.send("It will be sent.")
```

Also if you set `ACCESS_TOKEN=None`, it won't send a message.

```python
ACCESS_TOKEN = None

notify = LineNotify(ACCESS_TOKEN)

notify.send("It won't be sent.")
```

## Reference

[LINE Notify API Document](https://notify-bot.line.me/doc/)
