# Rickshaw
## Description
> I saw this cool vehicle while travelling around India. Unfortunately, I lost most of the image. This is all I have! Can you find the phone number of whoever manages this vehicle so I can contact them? DO NOT MAKE ANY CALLS Flag Format: csawctf{PhoneNumber} Replace spaces with dashes. Include the + and country code.

## Challenge Overview

We were given an image of a pink-coloured vehicle with a blue registration plate. The plate number is incomplete and starts with `77 CD`.

There is a hint in the description that says that the vehicle is probably a rickshaw in India. 

![image](https://github.com/user-attachments/assets/7bce343b-4b44-4b41-b0ef-4341609fdedc)

## Solution

By giving this information to ChatGPT, we get this information: 
- The "CD" stands for `Corps Diplomatique`
- In India, the number "77" featuring blue-coloured plates is assigned to the `USA` in the diplomatic license plate numbering system.

So, now we know that this pink rickshaw belongs to US Embassy in India. There is also a video on Youtube that features this rickshaw. 

![image](https://github.com/user-attachments/assets/89cf8264-11a8-467d-bb40-9e8f8dff2da6)

Search US Embassy in India contact number. 

![image](https://github.com/user-attachments/assets/4fee4902-6cba-4639-9514-456a6dca2ff1)

## Flag
```
csawctf{+91-11-2419-8000}
```
