export EDITOR="nvim"

export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"

export ZDOTDIR="$XDG_CONFIG_HOME/zsh"

export PATH="$PATH:$HOME/.local/bin:$HOME/.cargo/bin"

eval "$(/opt/homebrew/bin/brew shellenv)"
