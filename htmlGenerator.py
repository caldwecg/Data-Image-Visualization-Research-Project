import dominate
from dominate.tags import meta, h3, table, tr, td, p, a, img, br, link, script, select, option
import os
import html as html1



class HTML:
    """This HTML class allows us to save images and write texts into a single HTML file.
     It consists of functions such as <add_header> (add a text header to the HTML file),
     <add_images> (add a row of images to the HTML file), and <save> (save the HTML to the disk).
     It is based on Python library 'dominate', a Python library for creating and manipulating HTML documents using a DOM API.
    """

    def __init__(self, web_dir, title, refresh=0):
        """Initialize the HTML classes
        Parameters:
            web_dir (str) -- a directory that stores the webpage. HTML file will be created at <web_dir>/index.html; images will be saved at <web_dir/images/
            title (str)   -- the webpage name
            refresh (int) -- how often the website refresh itself; if 0; no refreshing
        """
        self.title = title
        self.web_dir = web_dir
        self.img_dir = os.path.join(self.web_dir, 'images')
        if not os.path.exists(self.web_dir):
            os.makedirs(self.web_dir)
        if not os.path.exists(self.img_dir):
            os.makedirs(self.img_dir)

        self.doc = dominate.document(title=title)
        with self.doc.head:
            script(src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js')
            script(src='image-picker-master/image-picker/image-picker.min.js')
            link(rel='stylesheet', type="text/css", href='image-picker-master/image-picker/image-picker.css')

        if refresh > 0:
            with self.doc.head:
                meta(http_equiv="refresh", content=str(refresh))

    def get_image_dir(self):
        """Return the directory that stores images"""
        return self.img_dir

    def add_header(self, text):
        """Insert a header to the HTML file
        Parameters:
            text (str) -- the header text
        """
        with self.doc:
            h3(text)

    def add_images(self, ims, txts, links, width=400):
        #self.t = table(border=1, style="table-layout: fixed;")  # Insert a table
        self.s = select(cls="image-picker show-html", multiple="multiple")

        self.doc.add(self.s)
        with self.s:
            x = 0;

            for im, txt, link in zip(ims, txts, links):

                option1 = option(str(links[x]), value=x)
                option1['data-img-src'] = os.path.join(im)
                option1['data-img-alt'] = "Page " + str(x)

                x = x + 1



    def save(self):
        """save the current content to the HMTL file"""
        html_file = '%s/test.html' % self.web_dir
        f = open(html_file, 'wt')
        f.write(self.doc.render())
        f.close()

    def add_select_image(self):
        with self.doc:
            script(html1.unescape("\n       var all_images = ['0', '1', '2'];\r\n\r\n       "
                                  "function setCSV(newValues, init){\r\n           "
                                  "let rows = [\r\n               ['Images', 'Selected'],\r\n           ];"
                                  "\r\n\r\n           window.all_images.forEach(image=>{\r\n                "
                                  "rows.push([image,newValues.includes(image)]);\r\n\r\n           })"
                                  "\r\n\r\n           let csvContent = 'data:text/csv;charset=utf-8,'"
                                  "\r\n                + rows.map(e => e.join(',')).join('\\n');"
                                  "\r\n\r\n\r\n          var encodedUri = encodeURI(csvContent);"
                                  "\r\n          var link;\r\n          if(init===true){\r\n              "
                                  "link = document.createElement('a');\r\n              link.id = 'linkID'"
                                  "\r\n          }\r\n          else{\r\n              "
                                  "link = document.getElementById('linkID')\r\n          }"
                                  "\r\n          link.setAttribute('href', encodedUri);\r\n          "
                                  "link.setAttribute('download', 'my_data.csv');\r\n          "
                                  "if(init===true){\r\n              link.innerText = 'download';"
                                  "\r\n              document.body.appendChild(link);\r\n          }"
                                  "\r\n       }\r\n       setCSV([], true);\r\n       "
                                  "$(\'select\').imagepicker({\r\n          hide_select : true,"
                                  "\r\n          show_label  : true,\r\n          changed     : "
                                  "function(select, newValues, oldValues, event){\r\n             "
                                  "window.setCSV(newValues, false);\r\n          }\r\n       })\n"))

if __name__ == '__main__':  # we show an example usage here.
    html = HTML('web/', 'test_html')
    html.add_header('**PROTEIN NAME**')

    ims, txts, links = [], [], []
    ims.append('ABCA3_7884_23302_A_7_2.jpg')
    txts.append('text_%d' % 0)
    links.append('ABCA3_7884_23302_A_7_2.jpg')

    ims.append('ABCA3_7884_23302_A_8_2.jpg')
    txts.append('text_%d' % 1)
    links.append('ABCA3_7884_23302_A_8_2.jpg')

    ims.append('ABCA3_7884_23302_A_9_2.jpg')
    txts.append('text_%d' % 2)
    links.append('ABCA3_7884_23302_A_9_2.jpg')

    html.add_images(ims, txts, links)
    html.add_select_image()
    html.save()