# My dot files managed by [ChezMoi](https://github.com/twpayne/chezmoi)

Built around Bash. Most supervitamined replacements stay optional.

## My friend programs

- fish shell, fisher plugin manager
- bash, [starship](https://starship.rs/) super prompt, [hishtory](https://github.com/ddworken/hishtory), [ls exa](https://github.com/rivy/rust.exa)
- terminal multiplexer: [tmux](https://github.com/tmux/tmux), plugin manager [tpm](https://github.com/tmux-plugins/tpm) and session manager [tmuxp](https://github.com/tmux-python/tmuxp) 
- a swiss-knife to make life easier: [fzf](https://github.com/junegunn/fzf)
- git: configuration and the terminal manager [tig](https://jonas.github.io/tig/) 
- vim: [vundle](https://github.com/VundleVim/Vundle.vim)
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
  # deployment path for "d" command (java deploy)
  deploydir = "~/dist"
  # deployment path to dev env with "deploy_dev" command
  deploydir_dev = "~/dist_dev"
  # deployment path to test env with "deploy_test" command
  deploydir_test = "~/dist_test"
  # Java versions from sdkman
  java6_version = "6.0.119-zulu"
  java7_version = "7.0.342-zulu"
  java8_version = "8.0.302-open"
  java11_version = "11.0.12-open"
  java20_version = "20-open"
  # extra certificate for NodeJs (PEM file) to trust HTTPS proxy
  extra_ca_cert = "~/config/security/ca-node.pem"
  # Java truststore for Maven to trust HTTPS proxy
  java_truststore_file = "~/config/security/extra-truststore.jks"
  java_truststore_password = "secret"
  # docker compose bin
  docker_compose_command = "/usr/bin/docker compose"
  # user path added to path
  extra_user_path = ""
  # tmux favorite shortcuts CTRL-ALT-1, CTRL-ALT-2, CTRL-ALT-3, CTRL-ALT-4
  tmux_favorite1 = "cd my_favorite_path"
  tmux_favorite2 = "sudo su"
  tmux_favorite3 = "myusualsshpassword"
  tmux_favorite4 = "export TERM=xterm"
```

