ROLE := fzf git go hub nvm packages_system tmux vim zsh

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
	cd ./roles/dustinspecker.${ROLE} && molecule test
