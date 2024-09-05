from Crypto.Util.number import inverse, long_to_bytes

def integer_cube_root(x):
    # Calculate the integer cube root using binary search
    low = 0
    high = x
    while low < high:
        mid = (low + high) // 2
        if mid**3 < x:
            low = mid + 1
        else:
            high = mid
    return low
    
def rsa_decrypt_part1(e, p, q, ct):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    pt = pow(ct, d, n)
    return long_to_bytes(pt)

def rsa_decrypt_part2(e, n, ct):
    # Compute the cube root of the ciphertext
    pt = integer_cube_root(ct)
    
    # Convert the plaintext integer to bytes
    pt_bytes = pt.to_bytes((pt.bit_length() + 7) // 8, 'big')
    
    return pt_bytes

def rsa_decrypt_part3(e, n, cts):
    # Brute-force all small primes to factorize n
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    
    plaintexts = []
    for ct in cts:
        pt = pow(ct, d, n)
        plaintexts.append(long_to_bytes(pt))
    
    return plaintexts

# Part 1
e1 = 65537
p1 = 172121215622002644508203276993358123995088782085757739482882130868561091053479845361954477648500306467444095310649666062152461795633586355092471628205784053504285769208858140932871742412415106236207060182025686366755120683231702876886000637023440269979346996667299858349540142506192780307300266522716801390223
q1 = 130816731468212939119782100270213388416157088491734078876899834892546984128747178271802071875570525831215279762596650056473653420132224523166176255360591908137907081989007546554257961009552201736770859607106812841949474759604000798205179029476815156920877444211898563318697660147370572427801035748911078450601
ct1 = 19831000740386021579343879893567984590639990256960576515876871218906299524946125985319048759869677079723967489377749502277453656068109552975641710887271424965339999359159792129684761331839691348093902589652343405342548209021676002235565881880542880299083709820487111455650876104353247947579013876850666889628097459993643573812287776552278234656463987628306116536197797928508516719701982766942415771317850183169279554818881222907876129486516588666870977090607803220366629728886812275291441790794608313601086374498293275407054119091158179064239429669281845025406721687020680447607252491005032428291434574622862844160390
decrypted_part1 = rsa_decrypt_part1(e1, p1, q1, ct1).decode()

# Part 2
e2 = 3
n2 = 26317970847107033275181949572706791265462461071511777596942432442373972180588642134450282931222077868585772908717447830212844291259645259566268869460161652247726106466583703253324783761595600174455911977177689493821600856282918565664195612137036099282918770148238039983456894701323911506923553241313686027455403884225502817219541144346491462318471695475512146892644773728789072084284349439499384935170513240362163417709616081578479886098291325247131953470392980397451212637599423120852323542581306925900852842200324637477339378467371625614172453652924551666844873618497859454382924933130450896810053419260450904219891
ct2 = 763896358903134847173234638278304609195350525197411748875707128359255804058484653010958693691
decrypted_part2 = rsa_decrypt_part2(e2, n2, ct2).decode()

# Part 3
e3 = 65537
n3 = 134427574635227
cts3 = [15757972435608, 19759917321982, 47493873964104, 60903948969815]
plaintexts_part3 = rsa_decrypt_part3(e3, n3, cts3)
decrypted_part3 = ''.join([pt.decode() for pt in plaintexts_part3])
print("Decrypted Part 1:", decrypted_part1)
print("Decrypted Part 2:", decrypted_part2)
print("Decrypted Part 3:", decrypted_part3)
# Combine all decrypted parts
final_message = decrypted_part1 + decrypted_part2 + decrypted_part3
print("Final Combined Message:", final_message)
pr
