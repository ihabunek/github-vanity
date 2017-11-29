default : clean dist

dist :
	@echo "\nMaking source"
	@echo "-------------"
	@python setup.py bdist

	@echo "\nMaking wheel"
	@echo "-------------"
	@python setup.py bdist_wheel --universal

	@echo "\nDone."

clean :
	rm -rf build dist *.egg-info MANIFEST htmlcov deb_dist github-vanity*.tar.gz

publish :
	twine upload dist/*

deb:
	@python setup.py --command-packages=stdeb.command bdist_deb
