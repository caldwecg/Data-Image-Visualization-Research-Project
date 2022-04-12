# Data-Image-Visualization-Research-Project


## Hosting on Heroku

All images are now hosted and displayed at the following web address: 

https://duodenum.herokuapp.com/


Preview: 
![WebPreview](https://github.com/caldwecg/Data-Image-Visualization-Research-Project/blob/main/Screen%20Shot%202022-04-11%20at%209.07.10%20PM.png?raw=true)


---
## Nodemon

Server side handling is done through Node.js to server web pages to the client.

`app.js: `

This is the file used to render each webpage to the client. The HTML pages are now ejs files stored in `/views`. These pages are capable of dynamic rendering of images.

Documentation can be found here: 
 > - https://www.npmjs.com/package/nodemon


---
## Data manipulation

`filescraper.py: `

This is the script used to filter through the 50 pages of generated HTLML code to modify images sources. This has a range of applicability and was used in place of the python file for generating the HTML. 

`.bak` files are generated as backup in case there is a need to access the original HTML code. 

This version now supports full size image rendering when clicked instead of selection:
 
 ![FullSizeImage]( https://github.com/caldwecg/Data-Image-Visualization-Research-Project/blob/main/Screen%20Shot%202022-04-11%20at%208.56.09%20PM.png?raw=true)


---
## Notes on image selector generator script
 `BUG: In htmlGenerator.py`

When run, this script will convet the character ">" into "&gt;" which throws an error when loading it into a browser. 
This character occurs on lines 82 and 85 of htmlGenerator.py and lines 24 and 30 of test.html. 

 test.html: what is generated by htmlGenerator.py, uses three images as examles to show the selection and resulting downloadable csv file. 


