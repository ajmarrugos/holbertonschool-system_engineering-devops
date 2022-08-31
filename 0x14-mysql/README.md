## MySQL: 

#### Step 1: Add MySQL APT repository in Ubuntu
- Ubuntu already comes with the default MySQL package repositories. In order to add or install the latest repositories, we are going to install package repositories. Download the repository using the below command:

sudo apt update
sudo apt install wget -y
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb

- Once downloaded, install the repository by running the command below:
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

#### Step 2: Update MySQL Repository on Ubuntu
- Run the below command to update your system packages

sudo apt-get update

- Now search for MySQL 5,7 using apt-cache as shown below:

$ sudo apt-cache policy mysql-server