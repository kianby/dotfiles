# My dot files managed by [ChezMoi](https://github.com/twpayne/chezmoi)

## My friend programs

- shell interpreter : bash and the prompt manager [starship](https://starship.rs/)
- terminal multiplexer: [tmux](https://github.com/tmux/tmux), plugin manager [tpm](https://github.com/tmux-plugins/tpm) and session manager [tmuxp](https://github.com/tmux-python/tmuxp) 
- a swiss-knife to make life easier: [fzf](https://github.com/junegunn/fzf)
- git: configuration and the terminal manager [tig](https://jonas.github.io/tig/) 
- vim: vim or neovim, [vundle](https://github.com/VundleVim/Vundle.vim)
- languages: python, perl, java with [sdkman](https://sdkman.io/) 


## Configuration file

a sample file (located in *~/config/chezmoi/chezmoi.toml*)

```toml
[data]
  # git configuration
  git_email = ""
  git_alias = ""
  # fzf search path for "p" command
  projectdir = "~/work"
  # deployment java path for "d" command
  deploydir = "~/dist"
  # Java versions from sdkman
  java6_version = "6.0.119-zulu"
  java7_version = "7.0.342-zulu"
  java8_version = "8.0.302-open"
  java11_version = "11.0.12-open"
  # extra certificate for NodeJs (PEM file) to trust HTTPS proxy
  extra_ca_cert = "/home/yannic/config/security/ca-node.pem"
  # Java truststore for Maven to trust HTTPS proxy
  java_truststore_file = "/home/yannic/config/security/snef-security.jks"
  java_truststore_password = "secret"
  # docker compose bin
  docker_compose_command = "/usr/bin/docker compose"
```

