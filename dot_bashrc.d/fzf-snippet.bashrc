# edit single line snippet
cfg-snippetrc() { $EDITOR ~/.snippetrc ;}

fzf-snippet() { 
	selected="$(cat ~/.snippetrc | sed '/^$/d' | sort -n | fzf -e -i )"
	# remove tags, leading and trailing spaces, also no newline
	echo "$selected" | sed -e s/\;\;\.\*\$// | sed 's/^[ \t]*//;s/[ \t]*$//' | tr -d '\n' | xclip -selection clipboard
}
