# EE551-FlaskSite
Stevens Automatic Study Plan Generator Web Interface and Automated Registration

This is a web interface and serverside code for a study plan validator/checker and automated course registration.
The interface was done using Bootstrap 4 and jQuery for the ajax post to the server. 

Below are the Python librariers and this was in Python 2.7:
Included-
	base64
	itertools
	re (regex)
	subprocess
	copy
	uuid
Installed-
	pypdf
	reportlab
	selenium
	tendo
	email
	urllib
	
To run the code, install all of the libraries and run WebApp.py with everything else in the folder.

Contributions:
Me- WebApp.py and conflictCheck.py (scrape classes and check for conflict)

Dan Pinto- PDF email and another attempt at the conflict check
https://github.com/danpinto97/EE551

David Helale- Transcript scraping of terms/grades 
https://github.com/dhelale1/EE-551

Gina Schnecker- Python lists to write to PDF
https://github.com/ginaschnecker/EE551-Project

The application can be seen in action at:https://www.youtube.com/watch?v=1iK7lIMIT_A

The WebApp serves as an integrator for all of the scripts. A user can either visit the study plan page or the registration page.

On the study plan page, they should enter all their desired courses in xXx 123 or XxX-123 format and upload the transcript. Due to the amount of hardcoding if AP classes or semesters off were taken into account (as well as the user input required), it is assumed that they are taking core classes at the standard times, but all the electives are free to be moved around. More majors and situations may eventually be added in the future.

The extra lab and recitation sections are when the course has the convention LA or RA at the end of xxx-123. They will not appear on the study plan since they need to be taken with the regular course but are there for time conflict checking.
The web app will take all the courses that a specified major needs to take, add the desired electives in, take grades from the transcript, and then check future courses for time conflicts based on data taken from the Stevens site for 2018 Fall/Spring terms.

If the study plan had no conflicts or not found future classes, a email will be sent with the PDF files. Otherwise, error messages by term will be sent to the user.

The user may also use the registration automated page to enter call numbers with their Stevens credentials and the server will use selenium to attempt registration. An error message will be returned if something went wrong aside from the course being full or not able to be added.

I wrote the selenium script mostly for fun, but some of the practicality may be an issue due to robots.txt on my.Stevens.edu. I locked it down to only one instance of the script allowed using tendo and delayed some of the commands. The commented out lines will actually make it attempt registration at the top of the hour (or bottom of next hour). It also does not currently access any prohibited URLs.
