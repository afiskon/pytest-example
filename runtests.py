#!/usr/bin/env python

import os
import re
import subprocess

html_prefix = "./html/"
idx_html = "<table>\n<tr><td>test</td><td>status</td></tr>\n"

for root, dirs, files in os.walk("tests"):
    for fname in files:
        if re.search("\\.py$", fname) is not None:
            sname = os.path.join(root, fname)
            html = html_prefix + sname + ".html"
            cmd = "PYTHONPATH=. py.test --doctest-modules -v -l " + \
                  sname + " --html=" + html
            code = subprocess.call(cmd, shell = True)
            status = "<p style='color:green;'>Success</p>"
            if code != 0:
                status = "<p style='color:red;'>FAILURE</p>"
            idx_html = idx_html + "<tr><td><a href='" + sname +\
                         ".html'>" + sname + "</a></td><td>" + status +\
                         "</td></tr>\n"

idx_html = idx_html + "</table>\n"

with open(html_prefix + "index.html", "w") as f:
    f.write(idx_html)
