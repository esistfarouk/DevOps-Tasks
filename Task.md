🛠 Task 1: Automate a Daily System Backup Script (Using Bash Script)

Objective:
Create a Bash script to perform automated daily system backups. This script should include:
	1.	Backup Logic:
	•	Back up a specified directory (e.g., /var/www, /etc, or configurable via a variable).
	•	Store backups in a compressed format (e.g., .tar.gz) in a backup directory.
	•	Option to retain a configurable number of daily backups (e.g., keep last 7 days).
	2.	Log Rotation:
	•	Implement logging for every backup run.
	•	Rotate logs to avoid unlimited log growth (e.g., keep last 5 logs).
	3.	Alerting on Failures:
	•	If any part of the backup fails (e.g., archiving, moving file, or permission errors), send an email alert using Postfix (do not use external SMTP services).
	•	Subject of the email should clearly state the error.
	4.	Scheduling:
	•	Set up a cron job to run the script daily.

Deliverables:
	•	Upload your code and cron job setup details to a GitHub repository.
	•	Include a README with:
	•	How to run and test the script
	•	How to configure paths and retention
	•	How to test the failure alert


⚙️ Task 2: Automate LAMP Stack Deployment (Using Ansible)

Objective:
Create an Ansible playbook to deploy and configure a LAMP stack (Linux, Apache, MySQL, PHP) on multiple servers.

Requirements:
	1.	Best Practices:
	•	Use roles to structure your playbook cleanly.
	•	Use blocks for logically grouped tasks.
	•	Use includes/imports where necessary to keep the playbooks modular.
	•	Implement error handling with rescue and always blocks.
	•	Add notification tasks using handlers (e.g., restart Apache after config change).
	2.	Functional Requirements:
	•	Install and configure Apache with a sample index.php.
	•	Install and secure MySQL (include root password setup and secure installation).
	•	Install PHP and confirm Apache can process PHP files.
	3.	Extras (Bonus Points):
	•	Add firewall rules (e.g., UFW) to allow web traffic (port 80/443).
	•	Create a separate inventory file and support different environments (e.g., dev, prod).

Deliverables:
	•	Upload your Ansible project to a GitHub repository.
	•	Include a README with:
	•	Setup instructions
	•	Inventory structure explanation
	•	How to run the playbook
	•	Notes on error handling and structure

✅ Submission Guidelines:
	•	Each task will be scored based on correctness, structure, use of best practices, and documentation.
	•	Please upload your completed work to GitHub and share the repository link with us.
	•	Deadline: Saturday, FEB12,2025 11:59PM (all tasks need to be delivered on time or will be considered as zero score)
    •	if you will not submit your tasks in time so please don't attend the sessions live untill you do it.usually i accept the exception if you faced a critical situation but for this task no exceptions for anyone so don't waste your time by make the request.
    •	Make sure Repo is public and share it with me & ENG. Mohamed el mahdy & you will get your score within a week after your submission.

Let us know if you have any questions or blockers. Good luck!