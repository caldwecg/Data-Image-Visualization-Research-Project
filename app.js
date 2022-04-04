const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const fs = require("fs");
const data = require("./data.json")

app.set('view engine', 'ejs');
app.use(express.static("public"))
app.use(bodyParser.urlencoded({extended: true}));






app.get("/home", function(req, res) {

  fs.readdir('./public/thumbnail/A1BG', (error, files) => {
    var imgFiles = [];
    files.forEach(file => {
            var imgpath ='/thumbnail/A1BG/' + file;
            imgFiles.push(imgpath);
    })
  
    res.render("home", {imgFiles: data})
  })
});

app.get("/", function(req, res) {
  res.render("index1")
});

app.get("/index1", function(req, res) {
  res.render("index1")
  });
app.get("/index2", function(req, res) {
  res.render("index2")
});
app.get("/index3", function(req, res) {
  res.render("index3")
});
app.get("/index4", function(req, res) {
  res.render("index4")
});
  app.get("/index5", function(req, res) {
  res.render("index5")
  });
  app.get("/index6", function(req, res) {
  res.render("index6")
  });
  app.get("/index7", function(req, res) {
  res.render("index7")
  });
  app.get("/index8", function(req, res) {
  res.render("index8")
  });
  app.get("/index9", function(req, res) {
  res.render("index9")
  });
  app.get("/index10", function(req, res) {
  res.render("index10")
  });
  app.get("/index11", function(req, res) {
  res.render("index11")
  });
  app.get("/index12", function(req, res) {
  res.render("index12")
  });
  app.get("/index13", function(req, res) {
  res.render("index13")
  });
  app.get("/index14", function(req, res) {
  res.render("index14")
  });
  app.get("/index15", function(req, res) {
  res.render("index15")
  });
  app.get("/index16", function(req, res) {
  res.render("index16")
  });
  app.get("/index17", function(req, res) {
  res.render("index17")
  });
  app.get("/index18", function(req, res) {
  res.render("index18")
  });
  app.get("/index19", function(req, res) {
  res.render("index19")
  });
  app.get("/index20", function(req, res) {
  res.render("index20")
  });
  app.get("/index21", function(req, res) {
  res.render("index21")
  });
  app.get("/index22", function(req, res) {
  res.render("index22")
  });
  app.get("/index23", function(req, res) {
  res.render("index23")
  });
  app.get("/index24", function(req, res) {
  res.render("index24")
  });
  app.get("/index25", function(req, res) {
  res.render("index25")
  });
  app.get("/index26", function(req, res) {
  res.render("index26")
  });
  app.get("/index27", function(req, res) {
  res.render("index27")
  });
  app.get("/index28", function(req, res) {
  res.render("index28")
  });
  app.get("/index29", function(req, res) {
  res.render("index29")
  });
  app.get("/index30", function(req, res) {
  res.render("index30")
  });
  app.get("/index31", function(req, res) {
  res.render("index31")
  });
  app.get("/index32", function(req, res) {
  res.render("index32")
  });
  app.get("/index33", function(req, res) {
  res.render("index33")
  });
  app.get("/index34", function(req, res) {
  res.render("index34")
  });
  app.get("/index35", function(req, res) {
  res.render("index35")
  });
  app.get("/index36", function(req, res) {
  res.render("index36")
  });
  app.get("/index37", function(req, res) {
  res.render("index37")
  });
  app.get("/index38", function(req, res) {
  res.render("index38")
  });
  app.get("/index39", function(req, res) {
  res.render("index39")
  });
  app.get("/index40", function(req, res) {
  res.render("index40")
  });
  app.get("/index41", function(req, res) {
  res.render("index41")
  });
  app.get("/index42", function(req, res) {
  res.render("index42")
  });
  app.get("/index43", function(req, res) {
  res.render("index43")
  });
  app.get("/index44", function(req, res) {
  res.render("index44")
  });
  app.get("/index45", function(req, res) {
  res.render("index45")
  });
  app.get("/index46", function(req, res) {
  res.render("index46")
  });
  app.get("/index47", function(req, res) {
  res.render("index47")
  });
  app.get("/index48", function(req, res) {
  res.render("index48")
  });
  app.get("/index49", function(req, res) {
  res.render("index49")
  });
  app.get("/index50", function(req, res) {
  res.render("index50")
  });
  



//Local Port for development
const PORT = process.env.PORT || 3000;


//Local Port for development
app.listen(PORT, function () {
    console.log('App is listening on port ${PORT}');
})
