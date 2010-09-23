# Makefile for mcfly

kill:
	-ps aux | egrep delorean | egrep -v egrep | head -1 | awk '{ print $$2 }' | xargs kill -9

run_db:
	@mkdir -p /tmp/mcfly_test_db
	@rm -rf /tmp/mcfly_test_db/*
	@delorean --username test --password test --dir /tmp/mcfly_test_db &

test: kill run_db
	@cd tests && nosetests -s
	@make kill
