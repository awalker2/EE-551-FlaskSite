# EE551-FlaskSite
Stevens Automatic Study Plan Generator Web Interface

This is a web interface and part of the serverside code for a flask site to automatically generate a study plan given parameters.

The interface was done using Bootstrap 4 and jQuery for the ajax post to the server. The post should contain all desired classes as well as a .txt file that contains the transcript.

Currently, the UI works and the server is able to print out the sent data.

The course scrape file is there as progress towards checking if two classes have a time conflict. The script currently can go through the web page of times for offered courses and obtain a data structure as follows [course name, [sec1 times], [sec2 times], ...]. The below revisions are needed for this:

-correct the AM/PM to 24 hour conversion
-make script a function
-make it so the script can tell if the section is a lab or not (check for xxx-123[L][A-Z] instead of just xxx-123)

With a group of three others, we will also be working on scraping data from a transcript, processing the courses taken and desired to check for potential time conflicts using previous offered times, and writting the courses to the end goal of the generated pdf study plan file.
