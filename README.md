# css2xpath #

Convert CSS selectors to XPath

css2xpath is a handy tool for converting CSS selectors to XPath
queries.  It's simple to use as both a shell command or a Python
module.

## Examples ##

##### Pass a single CSS selector as command argument #####
```css
$ css2xpath.py '#4web .home > h1'
//*[@id='4web']//*[contains(@class, 'home')]/h1

$ css2xpath.py '#4web .home' '#4web .work'
//*[@id='4web']//*[contains(@class, 'home')]
//*[@id='4web']//*[contains(@class, 'work')]
```

##### Use interactively #####
```css
$ css2xpath.py
div#4web > div.home
//div[@id='4web']/div[contains(@class, 'home')]

div#4web > div.work
//div[@id='4web']/div[contains(@class, 'work')]
```

##### Convert a file with CSS selectors on each line #####
```css
$ cat input
#4web  div.home > h1
#4web  div.work > p.lead
#4web .copyleft > p.notice
$ css2xpath.py < input > output
$ cat output
//*[@id='4web']//div[contains(@class, 'home')]/h1
//*[@id='4web']//div[contains(@class, 'work')]/p[contains(@class, 'lead')]
//*[@id='4web']//*[contains(@class, 'copyleft')]/p[contains(@class, 'notice')]
```

### More ###
Please see the source code for more details, it's very simple and
compact.

### Warning! ###
Currently the script doesn't handle some complex selectors.  While
most of these are completely unnecessary (like for adjacent sibling),
I believe there are still some we might want it to work with.  If you
stumble upon such a case, please report it to me or, even better, send
a push request.

### Bugs, feature requests, etc. ###
yordan [at] 4web [dot] bg
