# -------------------------------------------------------------
# PYTHON
# -------------------------------------------------------------

[[ -s $HOME/.pythonz/etc/bashrc ]] && source $HOME/.pythonz/etc/bashrc

if [ -f "$HOME/.pythonz/pythons/CPython-3.9.9/bin/python" ]; then
    export PATH="$HOME/.pythonz/pythons/CPython-3.9.9/bin:$PATH"
fi

if [ -f "$HOME/.pythonz/pythons/CPython-3.9.9/bin/pew" ]; then
    source "$(pew shell_config)"
fi

if [ -d "$HOME/.poetry/bin" ]; then
    export PATH="$HOME/.poetry/bin:$PATH"
fi

