#!/bin/bash

Target_path=home/farouk/Desktop
Backup_path=/var/backups/my-daily-backups
Log_path=/var/log/daily-backup_logs
Daily_Backups_Retrained=7
Recipient_Email=ahmedmohamedfarouk20@gmail.com

sudo mkdir -p $Backup_path
sudo mkdir -p $Log_path/Success
sudo mkdir -p $Log_path/Failed

sudo touch $Log_path/Success/daily_backup.log
sudo touch $Log_path/Failed/daily_backup.log

sudo chmod o+w $Log_path/Success/daily_backup.log
sudo chmod o+w $Log_path/Failed/daily_backup.log    


sudo tar -czf  $Backup_path/"$(date +%d-%m-%Y)"-backup.tar.gz -C / $Target_path 1> $Log_path/Success/daily_backup.log 2> $Log_path/Failed/daily_backup.log



if [ -s $Log_path/Failed/daily_backup.log ]; then

    # The file is not empty. That means there's an error occured
    echo "Error Occured. Email Sent"
    sudo echo "please check the attached file" | mail -s 'Daily Update Failure' -A $Log_path/Failed/daily_backup.log $Recipient_Email
else

    echo "No errors occured"
fi

sudo find $Backup_path -mtime +$Daily_Backups_Retrained -name '*.tar.gz' -exec rm {} \;

sudo logrotate -f /home/farouk/Desktop/devops/Scored\ Tasks/Daily\ Backup\ &\ Lamp\ Stack\ Deployment/logrotate.d/daily-backup
