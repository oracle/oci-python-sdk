#!/bin/bash
###################################################
# Upgrade showoci from adizohar git
###################################################
source ~/.bashrc >/dev/null

export APPDIR=${HOME}/showoci
export LOGDIR=$APPDIR/log
export LOG=$LOGDIR/showoci_upgrade.log
mkdir -p $LOGDIR
export GIT=https://raw.githubusercontent.com/adizohar/showoci/master

###########################################
# Download file Proc
###########################################
download_file()
{
    file=$1
    echo "   Download $file" | tee -a $LOG
    wget ${GIT}/$file -O ${APPDIR}/$file -o $LOGDIR/${file}.download.log| tee -a $LOG
    if cat $LOGDIR/${file}.download.log | grep -q "ERROR" 
    then
        echo "   -------> Error Downloading $file, Abort, log=$LOGDIR/${file}.download.log" | tee -a $LOG
        echo ""
        exit 1
    else
        echo "   -------> $file downloaded successfully" | tee -a $LOG
    fi
}

echo "##################################################" | tee -a $LOG
echo "# Upgrade showoci" | tee -a $LOG
echo "##################################################" | tee -a $LOG
cd $HOME
echo "Checking file showoci.py location before upgrade"
if [ -f "${APPDIR}/showoci.py" ]; then
   echo "   File showoci.py exist in app - ${APPDIR}/showoci.py " 
elif [ -f "${HOME}/oci-python-sdk/examples/showoci/showoci.py" ]; then
   echo "   File showoci.py exist in oci-python-sdk location, ${HOME}/oci-python-sdk/examples/showoci/showoci.py"
   echo "   Creating Symbolic Link: ln -s ${HOME}/oci-python-sdk/examples/showoci ."
   ln -s ${HOME}/oci-python-sdk/examples/showoci .
else
   echo "   File showoci.py could not find, creating showoci folder"
   mkdir -p ${HOME}/showoci
fi

###########################################
# Download files from github
###########################################
echo "" | tee -a $LOG
echo "Download showoci Files from github - $GIT " | tee -a $LOG
download_file showoci.py
download_file showoci_data.py
download_file showoci_service.py
download_file showoci_output.py
download_file showoci_csv2adw.py
download_file CHANGELOG.rst
download_file README.md

###########################################
# Upgrading OCI SDK
###########################################

echo "" | tee -a $LOG
echo "Upgrading OCI SDK Drivers - oci oci-cli oracledb" | tee -a $LOG
python3 -m pip install --upgrade oci oci-cli oracledb pip
