# Literally 1984
## Description
> An artist by the name of ‌ made a cover of a song I liked, but I don't remember the original composer of that song. Could you help me find the original composer?
> 
> Flag Format: csawctf{Firstname_Lastname} (replace all spaces with _ )
> 
> `author: lpv2013`


## Challenge Overview
From the challenge description, probably the only thing that we know is that there is an artist who sings a cover for a song that the author likes. So, maybe the first thing that came out to our mind was to 'dox' the author. But, the author already mentions that there is no need to search for his/her information. Gladly I didn't go to the rabbit hole.

![image](https://github.com/user-attachments/assets/127183b7-64c2-463b-a5cb-ed26543572a3)

![image](https://github.com/user-attachments/assets/39e093a9-9296-4f3e-89d9-a36a41ca6900)

The challenge title is hinting about `1984`, which when we searched about it, we found out that it is a novel by English writer George Orwell. 

![image](https://github.com/user-attachments/assets/15826047-7045-4e8b-b4e1-f7cd678c3734)

Some of the participants may guess that the song was `1984` by `David Bowie`, but I can ensure you that it is not. 

## Solution

Actually, if we look closely, we can see that there is some space in the sentence `the name of ‌ made a` (after `of`). So, I tried to inspect the element and found out that there is `&zwnj;` (Zero width non-joiner). That's why the artist's name didn't print out on screen.

![image](https://github.com/user-attachments/assets/8e6919fa-9245-4de1-a95d-f0c02604fbac)

Now, we can search for the artist's information. There is a <a href = "https://www.reddit.com/r/ask/comments/e08xdh/youtube_recommend_me_a_video_and_i_am_now_confused/
">Reddit post</a> talking about an artist named `&zwnj;`. Jackpot!!

We found his YouTube account and found out that the artist is a Vocaloid singer also known as `x0o0x_`. The artist have Instagram and Twitter/X account but there is nothing interesting other than the artist sang a cover for `bad guy` by `Billie Eilish`. Obviously not related to `1984`.
![image](https://github.com/user-attachments/assets/a2c93bb7-5b38-400f-94e8-5bad0a6f3c70)

The artist posted 23 songs on his YouTube channel but which is the right one? I tried to search "x0o0x_ 1984" and found a YouTube video with a comment that talks about a song covered by `x0o0x_` titled `Big Brother`. So,`Big Brother` is using `1984` novel as reference. 

![image](https://github.com/user-attachments/assets/013d5cc9-9cf3-4b99-b020-0f1d3ee4f992)
https://www.youtube.com/watch?v=8Xg4ODVYOfc

`Big Brother` seems like a Japanese song, since the lyrics are all Japanese. So, I tried to search "Big Brother original song Japanese" and found the original song. 

![image](https://github.com/user-attachments/assets/b0777fdc-1370-4242-8c2e-012464a5ef20)
https://www.youtube.com/watch?v=8Xg4ODVYOfc

The song is from `KAKU P-Model`, an electronic rock band from Japan. We can see the composer's name in the YouTube channel name. He is `Susumu Hirasawa`. And that's our flag.

## Flag
```
csawctf{Susumu_Hirasawa}
```
