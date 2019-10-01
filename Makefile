.PHONY: test
test:
	cd ./${ROLE} && molecule test
