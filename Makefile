gettext:
	xgettext --language=Python --keyword=_ --output=i18n/pwdmeter.pot `find pwdmeter -name "*.py"` --from-code utf-8

gettext_gen_local:
	(cd i18n && msginit --input=pwdmeter.pot --locale=cn --output-file cn.po)
	(cd i18n && msginit --input=pwdmeter.pot --locale=en --output-file en.po)
	(cd i18n && sed -i 's:charset=ASCII:charset=utf-8:' cn.po)

gettext_compile:
	(cd i18n && msgfmt cn.po --output-file cn/LC_MESSAGES/pwdmeter.mo)
	(cd i18n && msgfmt en.po --output-file en/LC_MESSAGES/pwdmeter.mo)

test:
	python -m unittest discover tests
