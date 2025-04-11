# Daily Backup Script

This Bash script automates daily backups of a specified directory, logs the results, and manages old backups and log rotation.

---


## What the Script Does

1. **Create Directories and Log Files:**
   - Makes sure backup and log folders exist.
   - Touches and gives write permission to log files.

2. **Perform Backup with Logging:**
   - Uses `tar` to compress the target directory.
   - Redirects `stdout` (success) to the `Success` log.
   - Redirects `stderr` (error) to the `Failed` log.

3. **Check for Errors:**
   - If the failed log is not empty, an email is sent with the log attached.

4. **Clean Old Backups:**
   - Deletes backups older than the configured retention period (`mtime +7`).

5. **Log Rotation:**
   - Calls `logrotate` with a custom configuration.

---

## Usage

Make the script executable and run it to run and test it:

```bash
chmod +x daily-backup.sh
./daily-backup.sh
```

## How to configure paths and retention

Open DailyBackup.sh and modify the following variables at the top:


| Variable                | Purpose                                               |
|------------------------|-------------------------------------------------------|
| `Target_path`          | Directory to be backed up                             |
| `Backup_path`          | Where backup archives will be stored                  |
| `Log_path`             | Logs for success/failure of backup                    |
| `Daily_Backups_Retrained` | Number of old backups to retain                    |
| `Recipient_Email`      | Email to notify in case of failure                    |

## How to test the failure alert

You can test failure alert by chaging Target_path to a non existential path and edit Recipient_Email to your email and rerun the bash script.

## Dependencies

### 1. Mailutils

```bash
sudo apt install mailutils
```

### 2. Postfix

#### 1. Install postfix
```bash
sudo apt-get install postfix
```
#### 2. Configure Postfix
```bash
sudo nano /etc/postfix/main.cf
```
Add the following lines to the end of the file
```
relayhost = [smtp.gmail.com]:587
smtp_use_tls = yes
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous
```
#### 3. Create a Gmail App Password

* Log in to your Gmail account.
* Go to your Google Account settings page.
* Click on "Security".
* Under "Signing in to Google", click on "App Passwords".
* Select "Mail" as the app and "Other (Custom Name)" as the device.
* Enter a name for the password and click on "Generate".
* Make a note of the password that is generated.

#### 4. Add Gmail Credentials in Postfix

```bash
sudo nano /etc/postfix/sasl_passwd
```
Add the following line to the file, replacing "your-email@gmail.com" with your Gmail address and "your-password" with the App Password that you generated

 [smtp.gmail.com]:587 your-email@gmail.com:your-password

Save and exit the file.

Now, use following command to hash the sasl_passwd file
   
```bash
sudo postmap /etc/postfix/sasl_passwd
```

#### 5. Restart Postfix
Now restart Postfix service to apply the changes by using following command ?
   
```bash
sudo systemctl restart postfix
```
#### 6. Test the Configuration

To test configuration, send an email using the "mail" commans, and replace "recipient@email.com" with the email address you want to send the email to
```bash
echo "Test email" | mail -s "Test subject" recipient@email.com
```
