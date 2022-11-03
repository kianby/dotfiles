# dotfiles

My dot files managed by ChezMoi (https://github.com/twpayne/chezmoi)

Friend tools:
- bash
- tmux, tmuxp, tpm
- tig, git
- starship
- vim or neovim, vundle
- python
- perl
- sdkman
- fzf

Configuration file *~/config/chezmoi/chezmoi.toml*

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

