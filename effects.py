from enum import Enum


def split(new_text):
    strings = []

    temp_string = ""
    temp_font = Font.NORMAL

    for char in new_text:
        if char == '*' and temp_font == Font.NORMAL:
            if temp_string != "":
                strings.append({"string": temp_string, "font": temp_font})
            temp_string = ""
            temp_font = Font.BOLD

        elif char == '*' and temp_font == Font.BOLD:
            if temp_string != "":
                strings.append({"string": temp_string, "font": temp_font})
            temp_string = ""
            temp_font = Font.NORMAL

        if char != '*':
            temp_string = temp_string + char

    if temp_string != "":
        strings.append({"string": temp_string, "font": temp_font})

    return strings


class Font(Enum):
    NORMAL = "Helvetica 10"
    BOLD = "Helvetica 10 bold"
    ITALIC = "Helvetica 10"
