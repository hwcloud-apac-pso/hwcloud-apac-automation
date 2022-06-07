Automation on Elastic Cloud Server Provisioning using a created image from Cloud Backup and Recovery

**1. Introduction**

This Program will use Huawei Cloud Python SDK to automate the process of creating images from Cloud Backup and Recovery (CBR) and use the created image to provision Elastic Cloud Server (ECS) in Huawei Cloud.
 
We are going to achieve the below objectives:

1. Automate the process of creating a Full-ECS image from Cloud Backup and Recovery (CBR) using Huawei SDK.
2. Automate the process of creating an Elastic Cloud Server (ECS) from the created image using Huawei SDK.
3. Automate the process of resource cleaning using Huawei SDK.

Solution Overview


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/solution_overview.png?raw=true)


**2. Prerequisites**

Before getting started, complete the following prerequisites:

1. To use *Huawei Cloud Python SDK*, you must have a Huawei Cloud account as well as the Access Key and Secret Key of the Huawei Cloud account. You can create an Access Key in the Huawei Cloud console. You can obtain the AK/SK pair for your account at *My credentials > Access keys > Create Access key.*** ** **

![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/create_credentials.png?raw=true)Figure 3.0: Example of how to create Access Key

1. To use *Huawei Cloud Python SDK* to access the APIs of a specific service, please make sure you have activated the service in the Huawei Cloud console (https://console.huaweicloud.com/?locale=en-us) if needed.
2. Huawei Cloud Python SDK requires *Python 3.3* *or later*, run the command *python --version* to check the version of Python. *If Python 3.3* or later is installed. skip step *4**.*
3. Install Python 3 and add Python to *PATH.* Open your browser and navigate to the Downloads for Windows section (https://www.python.org/downloads/windows/) of the official Python website (https://www.python.org/).

 

**3. Folder Content**

**3.1 Batch File**


**Batch File**	
**Function**

config.bat	To input configuration parameter and save to *Code > config.env* file.

create_image_and_ecs.bat	
Execute *main.py* python file to create Image from CBR backup and then use  the created image to provision ECS.

delete_servers.bat	
Execute *deleteServer.py* to delete all Servers from *resource_list.xlsx.*

delete_images.bat	
Execute *deleteImage.py* to delete all Images from *resource_list.xlsx.*

install.bat	
Install all the Python  Package defined in *requirement.txt.*

Table 3.0 :  Batch File (.bat)

**3.2 Python File**


**Python File**	
**Function**

main.py	
Create Image from CBR backup  and use the created image to provision ECS. ECS and Image ID are saved to *resource_list.xlsx*.

deleteServer.py	
Delete all servers in *resource_list.xlsx.*

deleteImage.py	
Delete all images in *resource_list.xlsx.*

utils.py	
Functions

Table 3.1 :  Python File (.py)

**3.3 Microsoft Excel File**


**Microsoft Excel**	
**Function**

ids_list.xlsx	
Save details required to  create Images and ECS in Huawei Cloud.

resource_list.xlsx	
Save Image ID and ECS ID  that successfully created. Failed Task will also be recorded in “Failed”  sheet.

Table 3.2 :  Microsoft Excel File (.xlsx)

**3.4 Text File**


**Text File**	
**Function**

num.txt	
Save the counter to  determine which sheets will be used to create image.

Table 3.3 :  Text File (.txt)


**4. Getting Start**

**4.1 Install Python 3**

1. Open your web browser and navigate to the Downloads for Windows section (https://www.python.org/downloads/windows/) of the official Python website (https://www.python.org/).
2. Search for your desired version of Python. At the time of publishing this article, the latest Python 3 release is version 3.10.4, while the latest Python 2 release is version 2.7.18.


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/python_latest_version.png?raw=true)Figure 4.0: Python's latest release for Windows


1. Run the *Python Installer* once downloaded. (In this example, we have downloaded Python 3.7.3.)
2. Make sure you select the *Install launcher for all users* and *Add Python 3.7 to PATH* checkboxes. The latter places the interpreter in the execution path. For older versions of Python that do not support the *Add Python to Path* checkbox. See Figure 4.1.
3. Select *Install Now* – the recommended installation options.


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/python_path_config.png?raw=true)Figure 4.1:  Install launcher for all users and add Python to PATH



1. The next dialog will prompt you to select whether to *Disable the path length limit*. Choosing this option will allow Python to bypass the 260-character MAX_PATH limit. Effectively, it will enable Python to use long path names.


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/python_max_length_config.png?raw=true)
Figure 4.2: Disable path length limit


1. The *Disable path length* *limit* option will not affect any other system settings. Turning it on will resolve potential name-length issues that may arise with Python projects developed in Linux.



**4.2 Install Python Packages**

1. Run *install.bat.* This batch file will install all the Python Packages defined in *requirement.txt.*


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/install_bat.png?raw=true)
Figure 4.3: install.bat & requirement.txt


**4.3 Write Configuration File**

1. Run *config.bat*. This batch file will start Command Prompt and ask the user to input configuration as prompted.


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd_config.png?raw=true)Figure 4.4 : Command Prompt to input configuration parameters.


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_vpc_id.png?raw=true)Figure 4.5 : Example to obtain VPC ID

![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_subnet_id.png?raw=true)
Figure 4.6 : Example to obtain subnet ID


1. The configuration parameter will pass to environment variable file in *Code > config.env*


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/config_env.png?raw=true)
Figure 4.7 : config.env file stores environment variables.


**4.4 Create Images and ECS**

1. Run *create_images_and_ecs.bat.* This batch file will execute *main.py* to create images and ECS.
2. Input number of sheets to determine which sheet in *ids_list.xlsx* to be used in creating images and servers. The *previous running* sheet number will also be shown in figure below. *Note: None in figure below indicate that the program never run before.


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd.png?raw=true)
Figure 4.8 : Command Prompt shows Previous running: None


**4.5 Delete Images**

1. Run *delete_images.bat*. This batch file will execute *deleteImage.py* to delete all created Images in Huawei Cloud.


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/delete_image_bat.png?raw=true)

Figure 4.9 : delete_images.bat


**4.6 Delete ECS**

1.  Run *delete_servers.bat.* This batch file will execute deleteServer.py to delete all created Servers in Huawei Cloud. 


![alt text](https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/delete_server_bat?raw=true)Figure 4.10 :  delete_servers.bat


 

5. Appendix 

codeExcel.zip (https://apac-professional-services.quip.com/-/blob/ZeBAAAOBvv1/keRXxZ-xzYkYmFXuPjRaGA?name=codeExcel.zip) 
