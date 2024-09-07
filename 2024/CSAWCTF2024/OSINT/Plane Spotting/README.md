# Plane Spotting

## Description
> My friend swears he saw a Russian plane in the US this June, but I don't believe him. He also says he saw it was parked next to a plane owned by an infamous former president!
> 
> Can you find the registration number of this Russian plane, the FAA airport code of where the plane was spotted parked next to the other, as well as the registration number of the plane owned by that president?
> 
> My friend also tells me that a few days earlier, ANOTHER Russian plane flew to the US. Find the city that Russian plane was closest to at 21:07:40 Z during its flight to the US!
> 
> Flag format: csawctf{RegistrationNumberRUS_AirportCode_RegistrationNumberUS_CityName}
> 
> Do not include any special characters (dashes, etc)

## Solution
There are 4 pieces of information that we need to search for the flag. 

### Registration Number for Russian plane
The description mentions that the Russian plane is parked beside an infamous former president. The hint heavily suggests that the former president is `Donald Trump`. 

Donald Trump's plane is indeed parked next to a Russian plane back in June 2024 according to <a href ="https://x.com/PenguinSix/status/1806740535685664847/photo/1">this tweet</a>.

![image](https://github.com/user-attachments/assets/28bd1ea5-b1b9-4e70-8551-c76a08538074)

If we zoom into the image, we can see the registration number of the plane.

- RegistrationNumberRUS: RA96018

### Airport Code
Both of the planes were parked at Washington Dulles International Airport (IAD).

![image](https://github.com/user-attachments/assets/16c135e4-9aa6-4626-bf3c-6cec7bc5c4de)

- AirportCode: IAD

### Registration Number for US plane
Next, we need to find the registration number for Trump's plane. According to <a href="https://www.autoevolution.com/news/trump-force-one-spotted-next-to-russian-jet-at-dulles-airport-embassy-or-something-else-236217.html#agal_0">this article</a>, Trump's plane is called Trump Force One. 

![image](https://github.com/user-attachments/assets/b90488ed-6028-4b26-8dff-52fa7f2e7a8d)

And the registration number is `N757AF`.

- RegistrationNumberUS: N757AF

### CityName

For me, this part is quite hard to find. We need to find another Russian plane that is bound for the US (few days) before the plane that is parked beside Trump's plane. So, the registration number should not be `RA96018`. 

Upon searching for "Russian plane to US in June", I found <a href="https://onemileatatime.com/news/russian-government-jet-new-york-washington/">this article </a> about a Russian plane (Ilyushin Il-96-300) flies from Moscow to New York and Washington.


![image](https://github.com/user-attachments/assets/4a0a32ca-e4bb-4c26-9488-2aba78221e25)

We also get its registration and flight number, which means that we can track its flight route using FlightAware. I used FlightAware because it allows us to track flight routes up to 3 months before the current date. 

According to FlightAware, `RA96019` flew to the US on `26 June 2024` from `02:06 EDT to 14:07 EDT`.

![image](https://github.com/user-attachments/assets/14d9afe1-f526-4f05-ac72-c59c4ce3a59d)

The challenge description mentions that the plane is still flying at `21:07:40 Z/UTC` (`17:07:40 EDT`). We can see that the flight from Moscow (`VKO`) to New York (`JFK`) is wrong due to the flight time being out of range. 

The next option is the flight from New York (`JFK`) to Washington (`IAD`). The plane flew from `16:55 EDT` and arrived at `IAD` at `17:46 EDT`. Seems like a valid answer. 

![image](https://github.com/user-attachments/assets/c4962395-73e6-4680-b6c9-8225e2d22e1b)

FlightAware allows us to see the plane's location at a specific time. At approximate `17:07:40 EDT`, the plane was about to fly across a river. I used Google Maps to find this exact location.

![image](https://github.com/user-attachments/assets/5b22f05e-60b9-4c33-aeef-7162a3d75643)

The plane was flying above `Trenton` city and about to fly across the Delaware River. 

- CityName: Trenton

## Flag
```
csawctf{RA96018_IAD_N757AF_Trenton}
```
