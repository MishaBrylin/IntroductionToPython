# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

text = 'абв фыв фыавапв абыфаывпа фыв фыа пващр ыщващыв ывщуцщм бывщалщвы щлывщ мащч ы вщалщыв ывмалщвыалп абвдрщшрщш'
text = text.split()


for i in text:
    if 'а' in i:
        if 'б' in i:
            if 'в' in i:
                text.remove(i)

print(text)
