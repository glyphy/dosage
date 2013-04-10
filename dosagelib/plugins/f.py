# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape, IGNORECASE, MULTILINE

from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import indirectStarter


class FalconTwin(_BasicScraper):
    url = 'http://www.falcontwin.com/'
    stripUrl = url + 'index.html?strip=%s'
    imageSearch = compile(r'"(strips/.+?)"')
    prevSearch = compile(r'"prev"><a href="(index.+?)"')
    help = 'Index format: nnn'


class Fallen(_BasicScraper):
    baseurl = 'http://www.fallencomic.com/'
    url = baseurl + 'fal-page.htm'
    stripUrl = baseurl + 'pages/part%s/%s-p%s.htm'
    imageSearch = compile(r'<IMG SRC="(page/.+?)"', IGNORECASE)
    prevSearch = compile(r'<A HREF="(.+?)"><FONT FACE="Courier">Back', IGNORECASE)
    help = 'Index format: nn-m (comicNumber-partNumber)'
    starter = indirectStarter(url,
        compile(r'\(NEW \d{2}/\d{2}/\d{2}\)\s*\n*\s*<a href="(pages/part\d+/\d+-p\d+\.htm)">\d+</a>', MULTILINE))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        num = pageUrl.split('/')[-1].split('-')[0]
        part = pageUrl.split('-')[-1].split('.')[0]
        return '%s-%s' % (part, num)

    def getIndexStripUrl(self, index):
        index, part = index.split('-')
        return self.stripUrl % (part, index, part)


class FantasyRealms(_BasicScraper):
    url = 'http://www.fantasyrealmsonline.com/'
    stripUrl = url + 'manga/%s.php'
    imageSearch = compile(r'<img src="(\d{1,4}.\w{3,4})" width="540"', IGNORECASE)
    prevSearch = compile(r'<a href="(.+?)"><img src="../images/nav-back.gif"', IGNORECASE)
    help = 'Index format: nnn'
    starter = indirectStarter(url,
        compile(r'<a href="(manga/.+?)"><img src="preview.jpg"', IGNORECASE))


class FauxPas(_BasicScraper):
    url = 'http://www.ozfoxes.net/cgi/pl-fp1.cgi'
    stripUrl = url + '?%s'
    imageSearch = compile(r'<img .*src="(.*fp/fp.*(png|jpg|gif))"')
    prevSearch = compile(r'<a href="(pl-fp1\.cgi\?\d+)">Previous Strip')
    help = 'Index format: nnn'


class FeyWinds(_BasicScraper):
    baseurl = 'http://kitsune.rydia.net/'
    url = baseurl + 'index.html'
    stripUrl = baseurl + 'comic/page.php?id=%s'
    imageSearch = compile(r"(../comic/pages//.+?)'")
    prevSearch = compile(r"(page.php\?id=.+?)'.+?navprevious.png")
    help = 'Index format: n (unpadded)'
    starter = indirectStarter(url, compile(r'(comic/page.php\?id.+?)"'))


class FilibusterCartoons(_BasicScraper):
    url = 'http://www.filibustercartoons.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php/%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class FirstWorldProblems(_BasicScraper):
    url = 'http://bradcolbow.com/archive/C5/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'P10'
    imageSearch = compile(tagre("img", "src", r'(http://(?:fwpcomics\.s3\.amazonaws\.com|s3\.amazonaws\.com/fwpcomics)/s1-[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bradcolbow\.com/archive/C5/[^"]+)', before="prev"))
    multipleImagesPerStrip = True
    help = 'Index format: a letter and a number'


class FlakyPastry(_BasicScraper):
    baseurl = 'http://flakypastry.runningwithpencils.com/'
    url = baseurl + 'index.php'
    stripUrl = baseurl + 'comic.php?strip_id=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back')
    help = 'Index format: nnnn'


class Flemcomics(_BasicScraper):
    url = 'http://www.flemcomics.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
      tagre("img", "src", r'/images/previous_day\.jpg'))
    help = 'Index format: yyyymmdd'


class Flipside(_BasicScraper):
    url = 'http://flipside.keenspot.com/comic.php'
    rurl = escape(url)
    stripUrl = url + '?i=%s'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.flipside\.keenspot\.com/comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%s\?i=\d+)' % rurl, after="prev"))
    help = 'Index format: nnnn'


class FonFlatter(_BasicScraper):
    url = 'http://www.fonflatter.de/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2005/09/20/01-begegnung-mit-batman'
    lang = 'de'
    imageSearch = compile(r'src="(%s\d+/fred_\d+-\d+-\d+[^"]+)' % rurl)
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/number-stripname'

    def shouldSkipUrl(self, url):
        return url in (
            self.stripUrl % "2006/11/30/adventskalender",
            self.stripUrl % "2006/09/21/danke",
            self.stripUrl % "2006/08/23/zgf-zuweilen-gestellte-fragen",
            self.stripUrl % "2005/10/19/naq-never-asked-questions",
       )


class Footloose(_BasicScraper):
    url = 'http://footloosecomic.com/footloose/today.php'
    stripUrl = 'http://footloosecomic.com/footloose/pages.php?page=%s'
    imageSearch = compile(r'<img src="/footloose/(.+?)"')
    prevSearch = compile(r'(?:first.+?[^>]).+?(/footloose/.+?)".+?(?:prev)')
    help = 'Index format: n (unpadded)'


class Freefall(_BasicScraper):
    url = 'http://freefall.purrsia.com/default.htm'
    stripUrl = 'http://freefall.purrsia.com/ff%s/fc%s.htm'
    imageSearch = compile(r'<img src="(/ff\d+/.+?.\w{3,4})"')
    prevSearch = compile(r'<A HREF="(/ff\d+/.+?.htm)">Previous</A>')
    help = 'Index format: nnnn/nnnnn'


class FredoAndPidjin(_BasicScraper):
    url = 'http://www.pidjin.net/'
    stripUrl = None
    help = 'Index format: yyyy/mm/dd/name'
    imageSearch = compile(tagre('img', 'src', '(http://cdn\.pidjin\.net/wp-content/uploads/\d+/\d+/[^"]+\.png)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre('a', 'href', '([^"]+)')+"Prev</a>")
    starter = indirectStarter(url,
       compile(tagre('a', 'href', "("+url+r'\d\d\d\d/\d\d/\d\d/[^"]+/)')))


class FullFrontalNerdity(_BasicScraper):
    url = 'http://ffn.nodwick.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '6'
    imageSearch = compile(tagre("img", "src", r'(%sffnstrips/\d+-\d+-\d+\.[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: number'


class FunInJammies(_BasicScraper):
    url = 'http://www.funinjammies.com/'
    stripUrl = url + 'comic.php?issue=%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'(/comic.php.+?)" id.+?prev')
    help = 'Index format: n (unpadded)'
