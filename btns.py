from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton(text="Filter Image🖼"),
        KeyboardButton(text="Connect to admin👨‍💻"),
    )

    return btn


async def filters_btn(filters: list):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    # print(*[KeyboardButton(text=item) for item in filters])
    # print([KeyboardButton(text=item) for item in filters])
    btn.add(
        KeyboardButton(text="⬅️")
    )
    btn.add(
        *[KeyboardButton(text=item) for item in filters],
    )

    return btn


async def cancel_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)

    btn.add(
        KeyboardButton(text="CANCEL❌"),
    )

    return btn



