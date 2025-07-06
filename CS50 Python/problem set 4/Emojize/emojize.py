import emoji

emo = input("emoji:")

new_emo = emoji.emojize(emo, language="alias")

print(new_emo)
