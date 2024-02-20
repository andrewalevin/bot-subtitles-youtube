from string import Template

DEMO_1_REQUEST = 'https://www.youtube.com/watch?v=Ao-746CujAE'

DEMO_2_REQUEST = 'https://www.youtube.com/watch?v=Ao-746CujAE бегемот'


START_TEXT = f'''
👋 Hello!
This Bot lets you to get subtitles of Youtube single movie and find single word.

🚩Supported language: RU only 
(other will be available later)

🔮 Usage:

<b> - Download all sutitles in .txt file </b>
Enter URL only
<pre>
{DEMO_2_REQUEST}
</pre>


<b> - Find keyword in subtitles text. </b>
Enter URL and keyword separated by a space.
<pre>
{DEMO_2_REQUEST}
</pre>

* If the size of the output text exceeds the maximum size of the telegram text, 
the answer will be sent as a .txt file.

'''

IS_TEXT_FORMATTED = True

FORMAT_TEMPLATE = Template('<b><s>$text</s></b>')

ADDITION_ROWS_NUMBER = 1


MAX_TELEGRAM_BOT_TEXT_SIZE = 4095


DESCRIPTION_TEXT = '''

Commands: 
 - \help
 - \start
 - \demo1
 - \demo2

'''
