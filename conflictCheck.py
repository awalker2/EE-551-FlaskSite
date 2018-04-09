import courseScrape as scrape

def setupLoop(*args):
    for arg in args:
        setupLoop(arg)
    else:
        
    


fallSite = "http://personal.stevens.edu/~gliberat/registrar/17f/17f_u.html"
springSite = "http://personal.stevens.edu/~gliberat/registrar/17s/17s_u.html"

scrape.courseScrape("BME 505", False, fallSite)


