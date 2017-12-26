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

## Reference

[LINE Notify API Document](https://notify-bot.line.me/doc)
