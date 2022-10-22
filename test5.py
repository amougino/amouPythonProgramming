import mechanize
twitteruserid = 'https://commentpicker.com/twitter-id.php'
#twitteruserid = 'https://google.com'
br = mechanize.Browser()
br.set_handle_robots(False)
br.open(twitteruserid)
for f in br.():
    print(str(f) + '\n')
    #form = f
#br.select_form(form)
#br.form['q'] = 'InstrumentalsBC'