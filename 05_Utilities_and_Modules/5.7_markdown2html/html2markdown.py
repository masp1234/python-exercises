from markdownify import markdownify
import requests as req

file = open('markdown.html', 'w').write(markdownify(req.get('https://clbokea.github.io/exam/assignment_2.html').content))
