# Notes
> I wrote the flag in the notepad and accidentally closed it. Will I lose the flag?
> Author: Identities

## Solution
Another AD1 file. Similar to Autosave for Words, we also have Autosave for Notepad. https://answers.microsoft.com/en-us/windows/forum/all/where-is-microsoft-notepads-autosave-files-located/b2d44571-0c80-4e44-a16d-0569032ecd9b 

We need to go to this path.
```
%localappdata%\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState

```

There will be a `.bin` file, extract and read the flag at the bottom of the file.
```
 1 .   * * G i v e n * * :   A   m e m o r y   d u m p   o f   a   c o m p r o m i s e d   s y s t e m .     
 2 .   * * T a s k s : * *     
   -   A n a l y z e   m e m o r y   d u m p   u s i n g   V o l a t i l i t y .     
   -   I d e n t i f y   s u s p i c i o u s   p r o c e s s e s   a n d   c o n n e c t i o n s .     
   -   D e c r y p t   d a t a   t o   r e v e a l   h i d d e n   i n f o .     
   -   L o c a t e   t h e   h i d d e n   f l a g .     
 3 .   * * E x a m p l e   F l a g   F o u n d : * *     
 b b c t f { Y 3 S _ l a _ i _ F o u n d _ m Y _ n o t 3 S }
```

# Flag
```
bbctf{Y3S_la_i_Found_mY_not3S}
```
