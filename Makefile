ROLE := fzf git go hub nvm packages-system tmux vim zsh

.PHONY: roles
roles: $(ROLE)

.PHONY: $(ROLE)
$(ROLE):
	@make ROLE=$@ test

.PHONY: shellcheck
shellcheck:
	docker run --rm -it -v "${PWD}:/mnt" koalaman/shellcheck:v0.7.0 *.sh

.PHONY: test
test:
	if ! ./check-role-changed.sh ; then \
		exit 0; \
	fi

	cd ./${ROLE} && molecule test --parallel
