# Day 10: Network Security Architecture

## 1. Network Segmentation (سگمنٹیشن)
Apne bade network ko chote hisson (Subnets) mein takseem karna. 
* **Faida:** Agar hacker Guest Wi-Fi hack bhi kar le, toh woh aapke Main Database tak nahi pohanch sakta.

## 2. DMZ (Demilitarized Zone)
Internal Network (mehfooz) aur Internet (non-secure) ke darmiyan ek dayar.
* **Faida:** Web server DMZ mein rakha jata hai. Agar hacker web server hack kar le, toh woh aapke internal customer database tak nahi pohanch sakta.

## 3. Firewalls (فائر وال)
Network traffic ka police officer. Yeh rules ke mutabiq traffic ko block ya allow karta hai.
* **Network Firewall (Layer 3/4):** IP Address aur Ports check karta hai.
* **WAF (Web Application Firewall):** Sirf Web traffic (HTTP/HTTPS) dekhta hai aur SQLi/XSS jese attacks roakta hai.

## Roman Urdu Summary
Network security ka asool hai: "Zero Trust". Apne network ko chote hisson mein baant do (Segmentation), ahem cheezon ko alag rakho (DMZ), aur un hisson ke darmiyan traffic ko control karne ke liye Firewall lagao.

