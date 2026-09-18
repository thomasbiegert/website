"""Content for thomasbiegert.github.io. Edit this file, then run build.py."""

SITE = {
    "base_url": "https://thomasbiegert.github.io",
    "description": "Thomas Biegert — Associate Professor in International Social and "
                    "Public Policy, LSE Department of Social Policy.",
    "year": "2026",
}

NAV = [
    ("Home", "{{ROOT}}"),
    ("Publications", "{{ROOT}}publications/"),
    ("CV", "{{ROOT}}cv/"),
    ("Contact", "{{ROOT}}contact/"),
]

ICON_EMAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="M3 6l9 7 9-7"/></svg>'
ICON_GITHUB = '<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.57.1.78-.25.78-.55 0-.27-.01-1.16-.02-2.1-3.2.7-3.88-1.36-3.88-1.36-.52-1.33-1.28-1.68-1.28-1.68-1.04-.71.08-.7.08-.7 1.15.08 1.75 1.18 1.75 1.18 1.03 1.75 2.7 1.25 3.36.96.1-.75.4-1.25.72-1.54-2.55-.29-5.23-1.28-5.23-5.68 0-1.26.45-2.29 1.18-3.1-.12-.29-.51-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11 11 0 0 1 5.79 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.24 2.76.12 3.05.74.81 1.18 1.84 1.18 3.1 0 4.41-2.69 5.38-5.25 5.67.41.36.78 1.06.78 2.14 0 1.55-.01 2.8-.01 3.18 0 .3.2.66.79.55A10.52 10.52 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z"/></svg>'
ICON_BLUESKY = '<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M12 8.5C10.6 5.8 7.2 3.6 4.2 3.4c-1 0-1.6.6-1.2 1.6.4 1 1.1 3.6 1.6 4.9.7 1.8 2.5 2.9 4.4 3.1-2 .3-3.9 1.4-4.9 3-.5.8.1 1.6 1 1.4 2.6-.6 5.5-2.3 6.9-4.6 1.4 2.3 4.3 4 6.9 4.6.9.2 1.5-.6 1-1.4-1-1.6-2.9-2.7-4.9-3 1.9-.2 3.7-1.3 4.4-3.1.5-1.3 1.2-3.9 1.6-4.9.4-1-.2-1.6-1.2-1.6-3 .2-6.4 2.4-7.8 5.1z"/></svg>'
ICON_SCHOLAR = '<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M12 3 1 9l11 6 9-4.9V17h2V9L12 3Zm0 8.9L4.6 8 12 4.1 19.4 8 12 11.9ZM5 13.2V17c0 1.9 3.1 3.5 7 3.5s7-1.6 7-3.5v-3.8l-7 3.8-7-3.8Z"/></svg>'
ICON_ORCID = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="11" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="7.6" cy="7.4" r="1.1" fill="currentColor"/><rect x="6.8" y="10" width="1.6" height="7.2" fill="currentColor"/><path d="M10.4 10h3.1c2.6 0 4.1 1.6 4.1 3.7 0 2.2-1.6 3.5-4.1 3.5h-3.1V10Zm1.6 1.4v4.4h1.4c1.7 0 2.5-.9 2.5-2.2 0-1.3-.8-2.2-2.5-2.2h-1.4Z" fill="currentColor"/></svg>'

SOCIAL_LINKS = [
    ("Email", "mailto:t.biegert@lse.ac.uk", ICON_EMAIL),
    ("GitHub", "https://github.com/thomasbiegert/", ICON_GITHUB),
    ("Bluesky", "https://bsky.app/profile/tbiegert.bsky.social", ICON_BLUESKY),
    ("Google Scholar", "https://scholar.google.com/citations?user=mJxa04MAAAAJ&hl=en", ICON_SCHOLAR),
    ("ORCID", "https://orcid.org/0000-0001-5437-2561", ICON_ORCID),
]

HOME_CONTENT = """
<div class="intro">
    <div class="intro-text">
        <h1 class="sr-only">Thomas Biegert</h1>
        <p class="intro-tagline">Sociologist. Interested in Social Policy, Labor Markets,
        Cumulative Inequality, and Research Methods. LSE Department of Social Policy.</p>
    </div>
    <img class="intro-photo" src="{{ROOT}}img/thomas-gears.jpg" alt="Thomas Biegert">
</div>

<div class="text-block">
<p>I&rsquo;m an Associate Professor in International Social and Public Policy in the
Department of Social Policy at the <strong>London School of Economics (LSE)</strong>.
I am on sabbatical for the entirety of the 2026/27 academic year, based at the
<strong>European University Institute (EUI)</strong> until mid-December 2026. I obtained my
Ph.D. in Sociology from the Graduate School for Economic and Social Sciences at the
<strong>University of Mannheim</strong> in 2014. Before coming to LSE in 2017 I held a
position as post-doctoral researcher at the <strong>WZB Berlin Social Science Center</strong>.
I am also a visiting research fellow at <strong>Tallinn University</strong>.</p>

<p>My main research interests are in the fields of comparative social policy and social
inequality, combined with a strong interest in research methods and research design.
Specifically, I look at <strong>social protection</strong> and
<strong>labour market policies</strong>, the <strong>conditionality of policy impact</strong>,
and how they shape <strong>social inequalities</strong> and
<strong>cumulative (dis-)advantages</strong> in employment and related social outcomes.
I am also more and more interested in doing basic research on the <strong>mechanisms</strong>
underlying the generation of social inequalities. PDFs and replication materials for several of my studies can be accessed from the
<a href="{{ROOT}}publications/"><strong>publications</strong></a> page. In case such
materials are still missing for a study you are interested in, please get in touch and
I will be happy to provide you with what I can.</p>

<p>I am not teaching this year while on sabbatical. In a typical year I convene and teach
<strong>SP401 Understanding Policy Research</strong> and
<strong>SP442 The Future of Work and Social Policy</strong> at LSE. You can find a full
list of the courses I have taught over the years in my <a href="{{ROOT}}cv/"><strong>CV</strong></a>.</p>

<p>Please don&rsquo;t hesitate to <a href="{{ROOT}}contact/"><strong>get in touch</strong></a>
if you want to talk about any of your or my research or teaching.</p>
</div>
"""

CV_CONTENT = """
<h2 class="page-title">Curriculum Vitae</h2>
<p>You can find a PDF version of my CV <a href="{{ROOT}}files/cv_tbiegert.pdf">here</a>.</p>
"""

CONTACT_CONTENT = """
<h2 class="page-title">Contact</h2>
<div class="contact-block">
<address>
Thomas Biegert<br>
London School of Economics and Political Science<br>
Department of Social Policy<br>
Houghton Street OLD 2.13<br>
London WC2A 2AE<br>
<a href="mailto:t.biegert@lse.ac.uk">t.biegert@lse.ac.uk</a>
</address>
</div>
"""

# Publications content: being revised incrementally by request.
PUBLICATIONS_CONTENT = """
<h2 class="page-title">Publications</h2>

<div class="pub-section">
<h4>Articles in Peer-Reviewed Journals</h4>
<p><strong>Biegert, Thomas</strong>, Kühhirt, Michael &amp; Van Lancker, Wim (2026): There Is Cumulative Status Bias and Status Entrenchment in NBA Awards: Comment on McMahan and Shor (2024). <em>Sociological Science</em> 13: 287-302. <a href="https://sociologicalscience.com/download/volume-13/march/SocSci_v13_287to302.pdf">[Open access link]</a> <a href="https://osf.io/t4n75/">[Replication files]</a></p>
<p>Breznau, Nate, &hellip; <strong>Biegert, Thomas</strong> &hellip; Marahrens, H. (2025): The Reliability of Replications: A Study in Computational Reproductions. <em>Royal Society Open Science</em> 12(3): 241038. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11922520/">[Open access link]</a></p>
<p><strong>Biegert, Thomas</strong>, Kühhirt, Michael &amp; Van Lancker, Wim (2023): They Can&rsquo;t All Be Stars: The Matthew Effect, Cumulative Status Bias, and Status Persistence in NBA All-Star Elections. <em>American Sociological Review</em> 88(2): 189-219. <a href="https://doi.org/10.1177/00031224231159139">[Open access link]</a> <a href="https://osf.io/ft8nc/">[Replication files]</a></p>
<p><strong>Biegert, Thomas</strong>, Özcan, Berkay &amp; Rossetti-Youlton, Magdalena (2023): Household Joblessness in US Metropolitan Areas during the COVID19 Pandemic: Polarization and the Role of Educational Profiles. <em>Socius</em> 9: 23780231231158087. <a href="https://doi.org/10.1177/23780231231158087">[Open access link]</a> <a href="https://osf.io/ab3w5/">[Replication files]</a></p>
<p><strong>Biegert, Thomas</strong>, Brady, David &amp; Hipp, Lena (2022): Cross-National Variation in the Relationship between Welfare Generosity and Single Mother Employment. <em>The ANNALS of the American Academy of Political and Social Science</em> 702(1): 37-54. <a href="https://journals-sagepub-com.gate3.library.lse.ac.uk/doi/full/10.1177/00027162221120760">[Open access link]</a></p>
<p>Breznau, Nate, &hellip; <strong>Biegert, Thomas</strong> &hellip; (total of 166 authors) (2022): Observing Many Researchers Using the Same Data and Hypothesis Reveals a Hidden Universe of Uncertainty. <em>Proceedings of the National Academy of Sciences</em> 119(44): e2203150119. <a href="https://doi.org/10.1073/pnas.2203150119">[Open access link]</a></p>
<p><strong>Biegert, Thomas</strong> &amp; Ebbinghaus, Bernhard (2022): Accumulation or absorption? Changing disparities of household non-employment in Europe during the Great Recession. <em>Socio-Economic Review</em> 20(1): 141-168. <a href="https://doi.org/10.1093/ser/mwaa003">[Link]</a> <a href="https://osf.io/preprints/socarxiv/pr57z/">[Replication files &amp; ungated pre-review version]</a></p>
<p><strong>Biegert, Thomas</strong> (2019): Labor Market Institutions, the Insider/Outsider Divide and Social Inequalities in Employment in Affluent Countries. <em>Socio-Economic Review</em> 17(2): 255-281. <a href="https://academic.oup.com/ser/article-abstract/doi/10.1093/ser/mwx025/4084295/Labor-market-institutions-the-insider-outsider?redirectedFrom=fulltext">[Link]</a></p>
<p>Meyer, Brett &amp; <strong>Biegert, Thomas</strong> (2019): The Conditional Effect of Technological Change on Collective Bargaining Coverage. <em>Research &amp; Politics</em>. <a href="https://journals.sagepub.com/doi/full/10.1177/2053168018823957">[Open access link]</a> <a href="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FJ9UZU">[Replication files]</a></p>
<p><strong>Biegert, Thomas</strong> &amp; Kühhirt, Michael (2018): Taking Lemons for a Trial Run: Does Type of Job Exit Affect the Risk of Entering Fixed-term Employment in Germany? <em>European Sociological Review</em> 34(2): 184-197. <a href="https://academic.oup.com/esr/article-abstract/34/2/184/4909813">[Link]</a> <a href="https://osf.io/nh5u4/">[Replication files &amp; ungated pre-review version]</a></p>
<p>Brady, David &amp; <strong>Biegert, Thomas</strong> (2017): The Rise of Precarious Employment in Germany. <em>Research in Sociology of Work</em> 31: 245-271. <a href="https://www.emeraldinsight.com/doi/full/10.1108/S0277-283320170000031008">[Link]</a> <a href="http://www.lisdatacenter.org/wps/liswps/708.pdf">[Ungated version]</a></p>
<p><strong>Biegert, Thomas</strong> (2017): Welfare Benefits and Unemployment in Affluent Democracies: The Moderating Role of the Institutional Insider/Outsider Divide. <em>American Sociological Review</em> 82(5): 1037-1064. <a href="http://journals.sagepub.com/doi/full/10.1177/0003122417727095">[Link]</a></p>
<p><strong>Biegert, Thomas</strong> (2014): On the Outside Looking in? Transitions Out of Non-employment in the United Kingdom and Germany. <em>Journal of European Social Policy</em> 24(1): 3-18 (JESP/ESPAnet Doctoral Researcher Prize Paper). <a href="http://journals.sagepub.com/doi/full/10.1177/0958928713511283">[Link]</a></p>
</div>

<div class="pub-section">
<h4>Monographs, Chapters, Working Papers</h4>
<p>König, Christian, <strong>Biegert, Thomas</strong>, Heisig, Jan Paul &amp; Solga, Heike (2025): <em>Cross-National Analysis of the Short- and Longer-Term Effects of Conditions at Labor Market Entry.</em> Mapineq Deliverable No. D4.2. <a href="https://www.econstor.eu/handle/10419/320735">[Link]</a></p>
<p><strong>Biegert, Thomas</strong> (2023): Labour Market Policies and Social Inequality in Labour Market Outcomes, in: Clegg, Daniel &amp; Durazzi, Niccolo (eds.): <em>Handbook of Labour Market Policy in Advanced Democracies</em>. Cheltenham: Edward Elgar Publishing: 479-494.</p>
<p>Täht, Kadri, Unt, Marge &amp; <strong>Biegert, Thomas</strong> (2023): Does a Higher Minimum Salary Protect Youth from In-work Poverty? Cross-national Evidence from the EU, in: Karner, Christian &amp; Hofäcker, Dirk (eds.): <em>Research Handbook on the Sociology of Globalization</em>. Cheltenham: Edward Elgar: 275-287.</p>
<p>Unt, Marge, Täht, Kadri &amp; <strong>Biegert, Thomas</strong> (2022): <em>Cross-national Differences in In-work Poverty among Young Adults in EU.</em> EUROSHIP Working Paper No. 18. <a href="https://euroship-research-eu.azurewebsites.net/wp-content/uploads/2022/11/EUROSHIP-Working-paper-No.-18-Cross-national-differences-in-in-work-poverty-among-young-adults-in-EU.pdf">[Link]</a></p>
<p>Unt, Marge, Täht, Kadri &amp; <strong>Biegert, Thomas</strong> (2022): <em>An Assessment of In-work Poverty among Female and Male Youth in Europe.</em> EUROSHIP Working Paper No. 16. <a href="https://euroship-research.eu/wp-content/uploads/2022/05/EUROSHP-Working-Paper-No-16.pdf">[Link]</a></p>
<p>Brady, David, <strong>Biegert, Thomas</strong> &amp; Vitols, Sigurt (2015): Continuity and Change in the German Labour Market, in: Dolphin, Tony (ed.): <em>Technology, Globalisation, and the Future of Work in Europe. Essays on Employment in a Digitised Economy</em>. London: Institute for Public Policy Research: 69-73.</p>
<p><strong>Biegert, Thomas</strong> (2014): <em>Patterns of Non-employment: How Labor Market Institutions Shape Social Inequality in Employment Performance in Europe</em>. Mannheim: University of Mannheim (Dissertation, received the Lorenz von Stein Prize for the best dissertation in Social Sciences at the University of Mannheim in 2014). <a href="https://ub-madoc.bib.uni-mannheim.de/37391/">[Link]</a></p>
<p><strong>Biegert, Thomas</strong> (2011): <em>Patterns of Non-employment: Labor Market Institutions and the Employment Performance of Social Groups</em>. MZES Working Paper 145. <a href="http://www.mzes.uni-mannheim.de/publications/wp/wp-145.pdf">[Link]</a></p>
</div>

<div class="pub-section">
<h4>Work Under Review and in Progress</h4>
<p>Economic Impact on Labor Market Outcomes of Older Workers in the EU <em>(with Marge Unt &amp; Kadri Täht, under review)</em></p>
<p>Why Comparative Social Policy Research Needs Better Theory and Measurement <em>(with Wim Van Lancker, under review)</em></p>
<p>Theoretical and Methodological Challenges for Researching Institutional Interplay <em>(in progress)</em></p>
<p>The Impact of Labor Market Conditions at Entry in the EU <em>(with Christian König, Heike Solga &amp; Jan-Paul Heisig, in progress)</em></p>
<p>Household Joblessness in US Local Labor Markets, 1970-2021 <em>(with Berkay Özcan, in progress)</em></p>
<p>Methods for Researching the Impact of Social Policies on Socio-Economic Outcomes <em>(in progress)</em></p>
<p>Group Differences in Cumulative Status Bias in Basketball Awards <em>(in preparation)</em></p>
</div>

<div class="pub-section">
<h4>Blog Posts, Media Coverage, etc.</h4>
<p><em>&ldquo;Was macht den Star zum Star?&rdquo;</em>, Süddeutsche Zeitung, April 19, 2023. <a href="https://www.sueddeutsche.de/wissen/star-soziologie-nba-kobe-bryant-sport-1.5808890">[Link]</a></p>
<p><em>&ldquo;Households failed to absorb massive job loss during economic crisis&rdquo;</em>, Social Europe, 02/2020. <a href="https://socialeurope.eu/households-failed-to-absorb-massive-job-loss-during-economic-crisis">[Link]</a></p>
<p><em>&ldquo;Nutzlose Befristungen&rdquo;</em>, Böckler Impuls, 09/2018. <a href="https://www.boeckler.de/114066_114078.htm">[Link]</a></p>
<p><em>&ldquo;The Worker Retraining Challenge&rdquo;</em>, U.S. News &amp; World Report, February 6, 2018. <a href="https://www.usnews.com/news/best-countries/articles/2018-02-06/what-sweden-can-teach-the-world-about-worker-retraining">[Link]</a></p>
<p><em>&ldquo;Good Job&rdquo;</em>, LSE News, December 15, 2017. <a href="http://www.lse.ac.uk/News/Research-Highlights/Economy/Good-job">[Link]</a></p>
<p><em>&ldquo;A generous welfare state can help reduce unemployment &ndash; if there are good job opportunities for the jobless.&rdquo;</em>, LSE United States Politics and Policy Blog, October 3, 2017. <a href="http://bit.ly/2fIUQqo">[Link]</a></p>
</div>
"""

NOT_FOUND_CONTENT = """
<h2 class="page-title">Page not found</h2>
<p>Sorry, that page doesn&rsquo;t exist. Head back to the <a href="{{ROOT}}">homepage</a>.</p>
"""

PAGES = {
    "": {
        "title": "Thomas Biegert",
        "nav_href": "{{ROOT}}",
        "content": HOME_CONTENT,
    },
    "publications": {
        "title": "Publications",
        "nav_href": "{{ROOT}}publications/",
        "content": PUBLICATIONS_CONTENT,
    },
    "cv": {
        "title": "Curriculum Vitae",
        "nav_href": "{{ROOT}}cv/",
        "content": CV_CONTENT,
    },
    "contact": {
        "title": "Contact",
        "nav_href": "{{ROOT}}contact/",
        "content": CONTACT_CONTENT,
    },
}

NOT_FOUND_PAGE = {
    "title": "Page not found",
    "nav_href": "",
    "content": NOT_FOUND_CONTENT,
}
