# Makefile for mcfly

test:
	@mkdir -p /tmp/mcfly_test_db
	@rm -rf /tmp/mcfly_test_db/*
	@delorean --username test --password test --dir /tmp/mcfly_test_db &
	@cd tests && nosetests -s
