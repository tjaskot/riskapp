#!/bin/bash
read -p "Quick export? " qe
if [[ $qe == 'y' ]]; then
	export FLASK_APP='riskapp.py'
	export FLASK_DEBUG=1
	export FLASK_ENV=Development
	flask run
  exit 0
fi
read -p "What is your app name? (Ex: app.py) " appname
echo "Exporting Flask App as ${appname}."
export FLASK_APP=${appname}

read -p "Would you like to enable debugging mode? Please enter either 1 or 0. " bugmode
if [[ ${bugmode} == 1 ]]; then
	echo "I'm ENALBING Debug mode for flask."
	export FLASK_DEBUG=1
else
	echo "I'm leaving debug mode OFF for now."
	export FLASK_DEBUG=0
fi

echo "I'm assuming you would like to use the default port of 5000, yes? "
select defport in "yes" "other"; do
	case ${defport} in
		yes ) echo "I'm using the default port of 5000.";
	                export FLASK_RUN_PORT=5000
			break;;
		other ) echo "I'm using your port value of ${defport}.";
	                export FLASK_RUN_PORT=${defport}
			break;;
	esac
done

echo "What env? "
select devprod in "Dev" "Prod"; do
	case $devprod in
		Dev ) export FLASK_ENV=development; break;;
		Prod ) export FLASK_ENV=production; break;;
	esac
done

while true; do
	read -p "Do you want to start a server (Yy/Nn)? " ff
	case $ff in
		[Yy]* ) #echo "Which one? (Select 1 or 2) "
			#select forf in "foreman" "flask"; do
			#	case $forf in
			#		foreman ) echo "I'm starting a foreman server for you. Please make sure you have the package installed, otherwise this will fail."
			#			foreman start;
			#			break;;
			#		flask ) echo "I have set your env vars, starting flask."
						flask run;
						break;;
			#	esac
			#done;break;;
		[Nn]* ) echo "Okay, please start the server before going to the localhost endpoint in your browser."; break;;
		* ) echo "Please select one of the options."
	esac
done
