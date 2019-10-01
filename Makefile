ROLE := fzf git hub nvm packages-system tmux vim zsh

.PHONY: roles
roles: $(ROLE)

.PHONY: $(ROLE)
$(ROLE):
	@make ROLE=$@ test

.PHONY: test
test:
	cd ./${ROLE} && molecule test
