import emoji

class Emoji:

    __sml = (':beaming_face_with_smiling_eyes:',':face_with_tears_of_joy:',':grinning_face:',':grinning_face_with_big_eyes:',':grinning_face_with_smiling_eyes:',':grinning_face_with_sweat:',':grinning_squinting_face:',':rolling_on_the_floor_laughing:',':slightly_smiling_face:',':smiling_face:',':smiling_face_with_halo:',':smiling_face_with_smiling_eyes:',':upside-down_face:',':winking_face:')
    __neg = (':angry_face:',':angry_face_with_horns:',':face_with_steam_from_nose:',':face_with_symbols_on_mouth:',':pouting_face:',':skull:',':skull_and_crossbones:',':smiling_face_with_horns:')

    def __init__(self):
        self.__sml_emo = list(map(emoji.emojize, self.__sml))
        self.__neg_emo = list(map(emoji.emojize, self.__neg))

    def get_smiling_emoji_count(self, text):
        count = 0
        for e in self.__sml_emo:
            count += text.count(e)
        return count

    def get_negative_emoji_count(self, text):
        count = 0
        for e in self.__neg_emo:
            count += text.count(e)
        return count

    def remove_emoji(self, text):
        return emoji.get_emoji_regexp().sub(u' ', text)
