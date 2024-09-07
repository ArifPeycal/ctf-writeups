# Authentic Chinese Food

## Description
> I visited this gourmet restaurant a while back, but I'm worried about the health and safety rating of it. Could you check it for me? Oh, and before I forget, could you tell me when the BUILDING was built, as well as the name of the LLC that owns the building?
> 
> Flag Format: csawctf{HealthGrade_YearBuilt_LLCName} (Name does not include LLC, replace all spaces with _ )
> 
> Grade is the MOST RECENT grade, and does not have to be a letter or a number.
> 
> author: lpv2013

## Challenge Overview
We were given a picture of a restaurant called 'Panda Express'. 

![panda](https://github.com/user-attachments/assets/a3af2217-a00d-4224-bf5f-e80e61044b6b)

First of all, we need to know the specific location of this branch. By using Google Lense, I found out that the restaurant is located at `Pearl St Fulton Mall td Brooklyn New York`. 

![image](https://github.com/user-attachments/assets/9b55a19c-2b76-433d-a657-75b7e202075f)
https://commons.wikimedia.org/wiki/File:Pearl_St_Fulton_Mall_td_(2018-07-07)_05_-_Panda_Express.jpg

## Solution
Now, we can start searching its health grade, the building build date and the LLC that owns the building. 

### Health Grade
For this part, I just asked ChatGPT and it gives me sugggestion to use `Restaurant Inspection Results` specifically in New York. Upon searching, I found this link official NYC government website to check for restaurant health grade. https://a816-health.nyc.gov/ABCEatsRestaurants/#!/Search
 
![image](https://github.com/user-attachments/assets/161237e4-a710-4a15-8981-1faa875700a0)

- HealthGrade: Pending

## Year Built

At first, I thought the question wants to ask about when the `Panda Express` was built. The official Panda Express page didnt state the first opening date whatsover. Then, I realize that the challenge wants the date when the **BUILDING** was built, not the restaurant. Then, I found this link that can search the building landlord in NYC. https://whoownswhat.justfix.org/en/

![image](https://github.com/user-attachments/assets/256cf083-f309-4ddf-a90f-60cadf8bfa0c)

The website didnt gives specific answer but it gives us other links that we can look into. We can see the property info and the year it was built. https://portal.displacementalert.org/property/3001500011

![image](https://github.com/user-attachments/assets/482d538a-6271-4921-9b1f-e8b51a4d0019)

- YearBuilt: 1920

## LLC Name
Using the same website, it shows the owner of the building which is `BNN FULTON FLUSHING OWNER LLC`. For the flag, we can ommit the LLC.

![image](https://github.com/user-attachments/assets/b73a3759-d483-4ae0-a31e-b722acf8a57b)

- LLCName: BNN FULTON FLUSHING OWNER 


## Flag
```
csawctf{Pending_1920_BNN_FULTON_FLUSHING_OWNER}
```
