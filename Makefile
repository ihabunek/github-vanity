default : clean dist

dist :
	python -m build

clean :
	rm -rf build dist *.egg-info MANIFEST htmlcov deb_dist github-vanity*.tar.gz

publish :
	twine upload dist/*
