## Requirements

This is a brief overview of the requirements that this application needs to fullfil to be useful for the user.

### Time Complexity (5s)

The environemnt in which this application will be used is very fast paced and time sensititive. Therefore, fast results are important. 
My initial expectation is to keep the the time of the data collection part made by the client side running python application under **5 seconds**.
This is basically the time from clicking the 'Get Data' button on the frontend to seeing the actual game data on the same application.

### Accessibility (mobile and web, Windows)

Initially, I anticipated only the need for a desktop application, but after some careful consideration realized that the possibility of a mobile version would also work quite well
for users that only have one screen available (that would be needed for seeing the actual game without having to tab-out).

Additionally, since I am also developing a python script that has to run on the client for data gathering, I would face the problem of different operating systems.
In this case, I can only focus on Windows, since most of the player base is here (especially in the professional scene, where no-one uses neither mac or linux).

Lastly, I considered wether the program should work constantly in the background, providing constant results, or only act on the click of a button.
Currently, I've decided against a constant version, since it would mean hidden costs that could scale over time (mainly api requests)
and could result in lower performance of the player running the companion, which wouldn't be ideal.

### Functionality Requirements

#### Client Side Python Program (Companion)

The program will need two main functionalities that the user has access to:

- Selecting on which side of the screen their team is (changes from match to match)
- Testing wether the program is working properly before joining an actual game

#### Web application

The web application has 3 main functionalities:

- Gathering data with a click on a button and validation the correct input (maybe tweaking further parameters like choosing a map or specific strategies)
- Viewing the ML models results
- An overview of past results for analysis

## Validation

To validate my expectations, I conducted interviews with two amateur/semi-professional CS:GO players.
Before explaining my concept, I asked them multiple question that I thought should be as little biased as possible.
In the middle of the interview, I explained my project and showcased the MVP, including a demo of it actually working to get their input and feedback after.

### Interview 1 - Alex 'Sofado', 22

**Tell me a about your background in gaming and CS:GO**

*I've been gaming since a child, been playing CS:GO for 3 years and on a semi-professional level for 1 year, I also was an In-Game Leader for a while
and know what is important in strategy calling.*

**How important is round data (players alive, grenades left, available weapons, etc.) for the outcome of a CS:GO round?**

*Very important and round deciding. All that information comes together to form the likelyness of round success.
But, there is still a chance for random impacts that are uncontrollable, such as uncommon positioning by enemy players.*

**Which round data would you say is the most important one and which one are you using most to evaluate round success**

*Grenades for sure, I would say they are about 50% percent of success in professional Counter-Strike and make a huge difference.
I am usually looking first for grenades left in the team, then player health and lastly our teams positions on the map to decide on a strategy.*

**Do you think, it would help the IGL to use a support system that uses past pro matches to give a tendency of success for different bombsites?**

*Yes, because IGL's can then focus on other tasks more or have a second opinion. This can also help on days where they lack focus.
Overall he can focus more on playing and actively supporting the team.*

**What data should this system include in its evaluation process?**

*Of course as much as possible*

**How long should this process take? What is the ideal time? What is the upper limit?**

*Roughly 10-15 seconds, at most 20. And an instant result would be best of course.*

**What would you improve in the current MVP?**

*Nothing really, I like that its very simple. Keep that!*

**Do you think this can be used in actual games?**

*Yes! I think this should get more attention, since it works with data that is available anyway and could make games more interesting.*

### Interview 2 - Gleb 'sTyL3Tz', 25

**Tell me a about your background in gaming and CS:GO**

*Gaming since I am 10 or 11. I started with CS 1.6, continued with source and I have been playing CS:GO for over 10k hours.*

**How important is round data (players alive, grenades left, available weapons, etc.) for the outcome of a CS:GO round?**

*Fairly important, but I think there is a lot that can't really be captured by data. For example tendencies of a particular enemy team or even things they did in the current game.*

**Which round data would you say is the most important one and which one are you using most to evaluate round success**

*Grenades*

**Do you think, it would help the IGL to use a support system that uses past pro matches to give a tendency of success for different bombsites?**

*I think this helps less experiences IGLs more and gets less helpful the better the team and the IGL gets.*

**What data should this system include in its evaluation process?**

*Everything*

**How long should this process take? What is the ideal time? What is the upper limit?**

*10-15 seconds, instant would be best. Maybe even live without the need to actively do sth to get results?*

**What would you improve in the current MVP?**

*I think for unexperienced players, it would be cool to have many strategies to pick from and then show what every player has to do. Besides that, it looks good.*

**Do you think this can be used in actual games?**

*I think that this would be illegal currently, but that might change. I can imagine this being uses, yes.*

### Interview Conclusion

I am very happy with how the interviews turned out.
I learned that they both agreed with almost all of the requirements I came up myself and I am certain that my MVP is on a good track to be actually usefull.
Also they both liked the technical solutions I came up with and where able to use them effortlessly.
