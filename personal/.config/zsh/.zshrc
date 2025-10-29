############
### p10k ###
############
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

[[ ! -f ~/.config/zsh/p10k.zsh ]] || source ~/.config/zsh/p10k.zsh

#################
### oh-my-zsh ###
#################
export ZSH="$ZDOTDIR/oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=( git zsh-autosuggestions zsh-syntax-highlighting )

source $ZSH/oh-my-zsh.sh

############
### Misc ###
############

# Shell aliases
source $ZDOTDIR/aliases

# iTerm2 shell integration
test -e "${ZDOTDIR}/.iterm2_shell_integration.zsh" && source "${ZDOTDIR}/.iterm2_shell_integration.zsh"

# fnm
eval "$(fnm env --use-on-cd --shell zsh)"

# Yazi change directory on exit
function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

# Vi mode
bindkey -v
KEYTIMEOUT=1 # Makes Esc fast

export PATH="/Users/hotsno/flutter/bin:/opt/homebrew/opt/ruby@3.4/bin:$PATH"
export PATH="$PATH":"$HOME/.pub-cache/bin"

eval "$(rbenv init - zsh)"

export GLM_INCLUDE_DIR="$(brew --prefix glm)/include"
export GLFW_DIR="/Users/hotsno/Developer/csc-471/graphics_lib/glfw-3.4"

# Aliases zoxide to cd (and some other stuff)
eval "$(zoxide init --cmd cd zsh)"

