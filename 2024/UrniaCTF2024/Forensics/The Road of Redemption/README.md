# The Road of Redemption
> The key to redemption lies in the hands of those who know the deep secrets of the church. Do you have the courage to uncover them and find your way to the light?
>
> Hint:
> 
> Are you familiar with the Blowfish protocol? Analyze the DNS packets directed towards uctf.ir. Pay attention to the return paths.
>
> Make sure to pay attention to the different modes of encryption in Blowfish.
>
> tshark -r The-Road-of-Redemption.pcap -Y "dns.qry.name contains uctf.ir" -T fields -e dns.qry.name | uniq | sed 's/.uctf.ir//g' | tr -d '\n'




