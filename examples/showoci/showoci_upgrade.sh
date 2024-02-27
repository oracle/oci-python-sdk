#!/bin/bash
###################################################
# Upgrade showoci from oci-python-sdk sdk git
###################################################
source ~/.bashrc >/dev/null

export APPDIR=${HOME}/showoci
export LOGDIR=$APPDIR/log
export LOG=$LOGDIR/showoci_upgrade.log
mkdir -p $LOGDIR
export GIT=https://raw.githubusercontent.com/oracle/oci-python-sdk/master/examples/showoci

###########################################
# Download file Proc
###########################################
download_file()
{
    file=$1
    file_download=${file}.download
    echo "   Download $file" | tee -a $LOG
    wget ${GIT}/$file -O ${APPDIR}/$file_download -o $LOGDIR/${file}.download.log| tee -a $LOG
    if cat $LOGDIR/${file}.download.log | grep -q "ERROR" 
    then
        echo "   -------> Error Downloading $file, Abort, log=$LOGDIR/${file}.download.log" | tee -a $LOG
        echo ""
        exit 1
    else
        echo "   -------> $file_download downloaded successfully" | tee -a $LOG
        echo "   -------> rename $file_download to $file" | tee -a $LOG
        mv -f ${APPDIR}/$file_download ${APPDIR}/$file
        if echo $file | grep -q ".sh" 
        then
            chmod +x ${base_dir}/$file_dir
            echo "   -------> change executable permission to $file_dir" | tee -a $LOG
        fi
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
download_file CHANGELOG.rst
download_file README.md

echo "Rename run_daily_report.sh to run_daily_report.sh.bak" | tee -a $LOG
if [ -f "${APPDIR}/run_daily_report.sh" ]; then
	mv ${APPDIR}/run_daily_report.sh ${APPDIR}/run_daily_report.sh.bak
fi
download_file run_daily_report.sh

###########################################
# Upgrading OCI SDK
###########################################

echo "" | tee -a $LOG
echo "Upgrading OCI SDK Drivers - oci oci-cli" | tee -a $LOG
python3 -m pip install --upgrade oci oci-cli pip
