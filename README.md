Sav.com Software Engineering Application Challenge
===

This is Hernan Razo's solution to the challenge listed on the job opening for software engineer at Sav.com. This python script uses `python 3.8.5` and no prebuilt APIs, packages, SDKs or examples on Stack Overflow.  

Explanation
---

The `get_domain_info()` function takes a domain name as input. It uses the Python Standard Library package `socket` to establish a connection with the InterNIC. From that connection, the function will retrieve a plethora of information regarding the domain. This information includes the Domain Name, Registry Domain ID, Registrar, WHOIS Server, etc.. This also includes the needed information for this challenge, the Registry Expiry Date. All this information is returned as a binary object.  

The `main()` function begins by asking the user to type in a domain name to search up. The program then dissects the input to only include the domain and the extension. After that, the previously stated `get_domain_info()` is called with the domain name passed as an argument. Retrieved data is then decoded to a string to make parsing easier. Since the challenge is only asking for the Registry Expiry Date, a regular expression is used to filter that part out. The `.search()` function from the `re` Python Standard library package is used to extract the date value between the object's name and the EOL character. Lastly, the `main()` function prints out the resulting date in a clean, easy-to-read manner onto the terminal.  
