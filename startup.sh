LIVING_PROCESS=`ps ux | grep -c [m]ain.py`

if [ ${LIVING_PROCESS} -eq 0 ];then
  echo 'START EXECUTION'
  cd /home/pi/ususama/
  nohup python main.py > /dev/null  &
fi
