# TryHackMe: Defensive Security Intro

## 1. PAGE TOPIC
Understanding Defensive Security (Blue Team) by acting as a SOC Analyst to investigate and stop an active cyberattack.

## 2. KEY CONCEPTS LEARNED
*   **Defensive Security:** The process of protecting systems, networks, and data from cyber threats (opposite of Offensive Security).
*   **SOC (Security Operations Center):** A team of IT professionals who monitor, detect, and respond to security incidents 24/7.
*   **Incident Response:** The process of investigating an alert, identifying the attacker, and mitigating the threat (e.g., blocking the IP).
*   **Roman Urdu Summary:** Defensive security mein hum hacker ko rokne aur system ko mehfooz rakhne ki koshish karte hain. SOC analyst ka kaam alerts ko check karna, attacker ko pehchanna aur uski requests ko block karna hota hai.

## 3. PRACTICAL STEPS & TOOLS
*   **Investigate:** Checked the SOC dashboard to find the attacker's IP address `32.122.195.63` probing admin pages.
*   **Block the Attacker:** Selected the IP on the Security Hub and clicked `Deploy` to block it at the edge firewall.
*   **Slow their Requests:** Clicked `Deploy` on rate-limiting to restrict how fast the attacker could send requests.
*   **Turn on Protection:** Activated the WAF/Protection to filter out probing attempts.

## 4. MY PROGRESS
*   Successfully investigated the security alert.
*   Successfully deployed 3 security measures to stop the attacker.
*   Captured the Flag and completed the Room (32 points earned).
