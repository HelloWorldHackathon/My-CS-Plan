# My-CS-Plan
A web application that allows Purdue CS students to optimize the classes they take to complete multiple CS concentrations

## Inspiration
The CS track system is VERY complicated. It can be frustrating trying to figure out what classes you need to take to finish two tracks. Some tracks have overlapping requirements, but most of the time, it is a list on the web that is tough to navigate. The two resources you can use are myPurduePlan which is notoriously outdated and slow, or an incredibly complicated spreadsheet posted by the CS Department 
## What it does
We have made a website that allows the user to select two of the CS tracks, and it will output a table with the minimum number of classes you need to take to fulfill to complete the two tracks. 
## How we built it
We used a next.js frontend that takes input from the checkboxes which then sends a get request to the python backend. The python backend then processes the classes selected and returns a minimum list of classes required for the student to complete the two tracks. 

That list of classes and their codes, names, and credit hours are formatted into a .json file which is then posted to the front-end.  The front-end formats the classes and their information into an HTML table string for a display.

## Challenges we ran into
- The track requirement list varies among different sources. 
- There were plenty of edge cases due to overlapping requirements. 
- We had issues posting from the backend. (HTTP requests with CORS are hard! Thank you Alwin!)
- Turning the JSON into an HTML table string

## Accomplishments that we're proud of
- Making it past the challenges listed above
- Creating a fully functional tool in less than 24 hours! 
- Making a full-on website accessible to anyone 

## What we learned
- How to make a full-on website (with frontend and backend connected) 
- How to make backend with python (flask) 
- How to connect the frontend to the backend 
- How hackathons work! 

## What's next for My CS plan
- Allowing more than 2 tracks to be selected 
- Ensuring data sources are accurate to be used by our algorithm 
