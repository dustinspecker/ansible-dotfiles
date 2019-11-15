ROLE := fzf git hub nvm packages-system tmux vim zsh

.PHONY: roles
roles: $(ROLE)

.PHONY: $(ROLE)
$(ROLE):
	@make ROLE=$@ test

.PHONY: shellcheck
shellcheck:
	docker run -it -v "${PWD}:/mnt" koalaman/shellcheck:v0.7.0 *.sh

.PHONY: test
test:
	cd ./${ROLE} && molecule test --parallel
