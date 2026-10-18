## Can-You-Find-The-Bugs?
This is a very beginner friendly web app intentionally made vulnerable to certain web vulnerabilities for beginners to try, learn and get hands on experience on real world security bugs.

## TL;DR
This is a short ctf style web application containing web vulnerabilities that beginners will try to find, chain them and uncover all other vulnerabilities to solve the lab. Below, I have covered the vulnerabilities present in the lab, how one issue leads to the other, how to find each of the issue, how to remediate these vulnerabilities in a real application, my motive behind building this and how I built this(tech stack, workflow and design choices).

Note: If you intend to genuinely solve the lab, it is highly recommended to try solving it youself before looking into the details on how to solve it here.

## Vulnerabilities present in the lab
The web app is a normal student portal. It contains exactly 4 vulnerabilities. It is intended to be short quick ctf (capture the flag) type lab but the catch is there is no flag. You have to find web vulnerabilities that actually exist in real world applications. The 4 vulnerabilities present are:

1) Idor (Insecure Direct Object Reference)
    Idor has been at the top of owasp top 10 for years if not decades. It is still at the top of the list as of now and is a very common web vulnerability so I thought it is a must-include.

2) Lack of proper authorization check
    It directly maps to A01: Broken Access control in the owasp top 10 and is insanely common class on web vulnerability. It essentially arises when the application lacks proper authorization check among its users. Basically a game of you-are-authenticated-but-are-you-authorized-to-do-it? It fits nicely with the student portal (student and teacher roles) so I included it too.

3) Information Disclosure
    One of the most underated class of vulnerabilities that I think are information disclosure. While the impact heavily depends on what kind of information is disclosed, it is generally a nice find if it exposes sensitive information like internal parameters, hidden functionalities, and secrets that a ordinary user doesnot need. It helps attackers map out the attack surface, nad chain it further with other vulnerabilities. 

4) Missing rate limiting 
    While missing rate limits is somewhat ignored by most applications, I belive it crucial for everyone who is somewhat involved in web technologies to know about rate limits. Furthermore, It can be a pain in the neck if its missing in authentication endpoints. It directly opens doors to various possibilities like brute-forcing, resource exhaustion, etc. 

## How to find each issue and how does one issue reveal/hint the other


