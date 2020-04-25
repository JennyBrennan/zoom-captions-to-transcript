# Zoom captions to transcript converter

Formats downloaded Zoom captions as a transcript and saves them in a new file.

If you download a set of captions from a Zoom call you get a text file where each line is a line of caption as it appeared on the screen, either starting with the speaker's name or the timestamp. It looks like this:

```
SPEAKER: Says some words
12:03:08  and some more words
12:03:11  and additional words,
12:03:14  followed by more lovely words!
NEWSPEAKER: Says different words - 
12:03:34  maybe better words, maybe worse.
```

But for use as a transcript, you'd probably prefer it looked something like this:

```
SPEAKER: Says some words and some more words and additional words, followed by more lovely words!

NEWSPEAKER: Says different words - maybe better words, maybe worse.
```

This tiny Python script does that with the command:

```python3 caption-convert.py your-captions.txt```

(Remember to replace ```your-captions.txt``` with the file name of your downloaded captions!)