"use strict";

    var all_images = ["0", "1", "2"];

    function setCSV(newValues, init){
       let rows = [
           ["Images", "Selected"],
       ];

       window.all_images.forEach(image=>{
            rows.push([image,newValues.includes(image)]);

       })

       let csvContent = "data:text/csv;charset=utf-8,"
            + rows.map(e => e.join(",")).join("\n");


      var encodedUri = encodeURI(csvContent);
      var link;
      if(init===true){
          link = document.createElement("a");
          link.id = "linkID"
      }
      else{
          link = document.getElementById("linkID")
      }
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "my_data.csv");
      if(init===true){
          link.innerText = "download";
          document.body.appendChild(link);
      }
    }
    setCSV([], true);
    $('select').imagepicker({
      hide_select : true,
      show_label  : true,
      changed     : function(select, newValues, oldValues, event){
         window.setCSV(newValues, false);
      }
    })