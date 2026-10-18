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
    One of the most underated class of vulnerabilities that I think are information disclosure. While the impact heavily depends on what kind of information is disclosed, it is generally a nice find if it exposes sensitive information like internal parameters, hidden functionalities, and secrets that a ordinary user doesnot need. It helps attackers map out the attack surface, and chain it further with other vulnerabilities. 

4) Missing rate limiting 
    While missing rate limits is somewhat ignored by most applications, I belive it crucial for everyone who is somewhat involved in web technologies to know about rate limits. Furthermore, It can be a pain in the neck if its missing in authentication endpoints. It directly opens doors to various possibilities like brute-forcing, resource exhaustion, etc. 

## How to find each issue and how does one issue reveal/hint the other
If you wandered around a little bit, you will see a cookie named "lab_id" in cookies (accessible from browser dev tools). Notice that it has an integer value. If you tamper it and refresh, you can view other students records in /student/records endpoint. There you go, IDOR. If you keep tampering to lets say non existent records, it will state record doesnot exist but uid=3 will hint about teacher roles, dashboard and uid belonging to teacher account. There you go, unnecessary information disclosure which hinted that a teacher dashboard exists somewhere even if it is not visible from student dashboard. Now if you tamper the url from /student/profile to /teacher/profile, the web app normally should restrict student accounts but this web app will not (well duh its designed to be vulnerable) and you can access the teacher dashboard which is our third vulnerability.
(Notice how one vulnerability is leading to the other. From idor to information disclosure to improper authorization controls.)
Then comes the fourth, missing rate limits, which seem a little not-so-connected to other vulnerabilities but it surely exists in the login panel. You can use any tool like burp intruder and send ~50-100 requests and observe that rate limit is absent (btw dont hammer the site with excessive requests, keep it ethical. Only do what is necessary to verify, do not overdo it.)

## How to remediate these issues in a real application
Now, learning to remediate is just as important as learning to find bugs. As the saying goes, "To be a good builder, you need to know how to break things". Yea, I made that up. dk how it fits. But anyway, here is how to remediate those issues:

1) Remediate IDOR:
    ``` python
    @views.route("/student/records")
    def records():
    uid = session.get("uid")
    username = session.get("username")
    if not username:
        error = "You are not logged in yet"
        return render_template("base.html" , error=error)
    record = student_records.get(str(uid))
    return render_template("records.html", course=record["course"], gpa=record["gpa"] , feedback=record["feedback"])
    ```

    See what I did right there, instead of taking uid from the tamperable cookie, if we take uid from session (which is signed by flask by default so its not tamperable), we can retrieve correct uid and display the records associated with it. So yeah there is not point in inventing the unsigned tamperable cookie in the firsdt place, I jsut made that up to make it vulnerable.

2) Enforcing proper authorization
    ``` python
    if role != "teacher":
        error = "You are not a teacher bozo"`
        return render_template("base.html", error=error)
    ```

    By simply checking if user role is teacher or not when somebody tries to access the teacher dashboard prevents unauthorized access to the teacher dashboard. Literally.

3) Information disclosure
    Again, there was no need to display unnecessary excessive information like existence of teacher account and the exact uid associated with it to a normal user. Simply "record nto found" like other non existent uids were enough. Only display what is necessary. 

4) Missing rate limits
    Always protect your sensitive enpoints, especially authentication endpoints with proper rate limiting. Ofcourse, if a user chooses a strong password with special characters and all, bruteforcing is quite not the smartest use of time for the attacker but what if your application uses OTP verification? A 4 digit otp only has 10000 total combination and 1 million for 6 digits so yea, it might take a time but definitely crack-able I would say. So its good practice to protect those endpoints. Also there maybe endpoints other than auth like maybe api calling. So yeah keep an eye for such endpoints.

## My motive behind building this
I am a totally normal 18 year old who just happened to be interested in web security(I dont use arch btw) and web development. I love building some web application and occasinally do bug bounties and responsible disclosures. So yea, I wanted to build smth that combines both of these and I happen to think of this mini lab idea. This would also help complete beginners get a grasp of how vulnerabilities occur in real world applications and get hands on experience in that. This is pretty much my reason behind building this web project.

## How I built this
I built this using Flask (python framework) and basic html/css/js. I didnt use a database and instead used a data.py file to store data because most of the data used are static and this lab is intended to be a small shared lab for everyone. I choose this approach because well obviously I dont want a random guy hamerring my site at 2 am and call it "beginner testing". That is the main reason (defintely not because I ran out of free supabase instances.)

## Screenshot
![screenshot1]\(images/ss1.png)
![screenshot2]\(images/ss2.png)


## Conclusion
To sum it up, this is a intentionally vulnerable lab made by Abip Mahat, for beginners to try, learn and get practical experience on web security. If you are a complete beginner trying to enter web security, this is just for you, a learning resource material. If there are any issues with the site, feel free to connect and share.



