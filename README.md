# **Automation on Elastic Cloud Server Provisioning using a created image from Cloud Backup and Recovery**

## **1. Introduction**

This Program will use Huawei Cloud Python SDK to automate the process of creating images from Cloud Backup and Recovery (CBR) and use the created image to provision Elastic Cloud Server (ECS) in Huawei Cloud.
 
We are going to achieve the below objectives:

1. Automate the process of creating a Full-ECS image from Cloud Backup and Recovery (CBR) using Huawei SDK.
2. Automate the process of creating an Elastic Cloud Server (ECS) from the created image using Huawei SDK.
3. Automate the process of resource cleaning using Huawei SDK. </br>

## **2. Solution Overview**
<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/solution_overview.png" alt="Solution Overview"/>
</p>
<p align="center"><i>Figure 2.0: Solution Overview</i></p>
</br>

## **3. Prerequisites**

Before getting started, complete the following prerequisites:

1. To use **Huawei Cloud Python SDK**, you must have a Huawei Cloud account as well as the Access Key and Secret Key of the Huawei Cloud account. You can create an Access Key in the Huawei Cloud console. You can obtain the :key: AK/SK pair for your account at **My credentials > Access keys > Create Access key.**

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/create_credentials.png" alt="Create Credentials"/>
</p>
<p align="center"><i>Figure 3.0: Example of how to create Access Key</i></p>
<br/>

2. To use **Huawei Cloud Python SDK** to access the APIs of a specific service, please make sure you have activated the service in the [Huawei Cloud console](https://console.huaweicloud.com/?locale=en-us) if needed.
3. Huawei Cloud Python SDK requires **Python 3.3 or later**, run the command **python --version** to check the version of Python. If **Python 3.3 or later** is installed. skip **step 4**.
4. Install Python 3 and add Python to **PATH.** Open your browser and navigate to the [Downloads for Windows section](https://www.python.org/downloads/windows/) of the [official Python website](https://www.python.org/).

 

## **4. Folder Content**

### **4.1 Batch File**

<table>
  <tr>
    <th><b>Batch File</b></th>
    <th><b>Function</b></th>
  </tr>
  <tr>
    <td>config.bat</td>
   <td>To input configuration parameter and save to <b>Code > config.env</b> file.</td>
  </tr>
  <tr>
    <td>create_image_and_ecs.bat</td>
    <td>Execute *main.py* python file to create Image from CBR backup and then use  the created image to provision ECS.</td>
  </tr>
 <tr>
    <td>delete_servers.bat</td>
    <td>Execute *deleteImage.py* to delete all Images from <b>resource_list.xlsx.</b></td>
  </tr>
 <tr>
    <td>delete_images.bat</td>
    <td>Execute *deleteImage.py* to delete all Images from <b>resource_list.xlsx.</b></td>
  </tr>
 <tr>
    <td>install.bat</td>
    <td>Install all the Python  Package defined in <b>requirement.txt.</b></td>
  </tr>
</table>

<p align="center"><i>Table 4.0 :  Batch File (.bat)</i></p>
<br/>


### **4.2 Python File**

<table>
  <tr>
    <th><b>Python File</b></th>
    <th><b>Function</b></th>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Create Image from CBR backup  and use the created image to provision ECS. ECS and Image ID are saved to <b>resource_list.xlsx</b>.</td>
  </tr>
  <tr>
    <td>deleteServer.py</td>
    <td>Delete all servers in <b>resource_list.xlsx.</b></td>
  </tr>
 <tr>
    <td>deleteImage.py</td>
    <td>Delete all images in <b>resource_list.xlsx.</b></td>
  </tr>
 <tr>
    <td>utils.py	</td>
    <td>Python File to store all functions defined.</b></td>
  </tr>
</table>

<p align="center"><i>Table 4.1 :  Python File (.py)</i></p>
<br/>

### **4.3 Microsoft Excel File**

<table>
  <tr>
    <th><b>Microsoft Excel File</b></th>
    <th><b>Function</b></th>
  </tr>
  <tr>
    <td>ids_list.xlsx</td>
    <td>Save details required to  create Images and ECS in Huawei Cloud.</b></td>
  </tr>
  <tr>
    <td>resource_list.xlsx</td>
    <td>Save Image ID and ECS ID  that successfully created. Failed Task will also be recorded in “Failed”  sheet.</b></td>
  </tr>
</table>

<p align="center"><i>Table 4.2 :  Microsoft Excel File (.xlsx)</i></p>
<br/>

### **4.4 Text File**

<table>
  <tr>
    <th><b>TextFile</b></th>
    <th><b>Function</b></th>
  </tr>
  <tr>
    <td>num.txt</td>
    <td>Save the counter to  determine which sheets will be used to create image.</b>.</td>
  </tr>
  <tr>
    <td>requirement.txt</td>
    <td>Save all the required python packages</b></td>
  </tr>
</table>

<p align="center"><i>Table 4.3 :  Text File (.txt)</i></p>
<br/>


## **5. Getting Start**

### **5.1 Install Python 3**

1. Open your web browser and navigate to the Downloads for [Windows section](https://www.python.org/downloads/windows/) of the [official Python website](https://www.python.org/).
2. Search for your desired version of Python. At the time of publishing this article, the latest Python 3 release is version 3.10.4, while the latest Python 2 release is version 2.7.18.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/python_latest-version.png" alt="Python Latest Release"/>
</p>
<p align="center"><i>Figure 5.0:  Python's latest release for Windows</i></p>
</br>

3. Run the **Python Installer** once downloaded. (In this example, we have downloaded Python 3.7.3.)
4. Make sure you select the **Install launcher for all users** and **Add Python 3.7** to PATH checkboxes. See **Figure 5.1**.
5. Select **Install Now** – the recommended installation options.


<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/python_path_config.png" alt="Add Python to PATH"/>
</p>
<p align="center"><i>Figure 5.1:  Install launcher for all users and add Python to PATH</i></p>
</br>

6. The next dialog will prompt you to select whether to **Disable the path length limit**. Choosing this option will allow Python to bypass the 260-character MAX_PATH limit. Effectively, it will enable Python to use long path names.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/python_max_length_config.png" alt="Disable path length limit"/>
</p>
<p align="center"><i>Figure 5.2:  Disable path length limit</i></p>
</br>

7. The *Disable path length* *limit* option will not affect any other system settings. Turning it on will resolve potential name-length issues that may arise with Python projects developed in Linux.



### **5.2 Install Python Packages**

1. Run **install.bat.** This batch file will install all the Python Packages defined in **requirement.txt.**

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/install_bat.png" alt="Batch file to install python packages"/>
</p>
<p align="center"><i>Figure 5.3: install.bat & requirement.txt</i></p>
</br>


### **5.3 Write Configuration File**

1. Run **config.bat**. This batch file will start Command Prompt and ask the user to input configuration as prompted.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd_config.png" alt="Command Prompt"/>
</p>
<p align="center"><i>Figure 5.4: Command Prompt to input configuration parameters.</i></p>
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_vpc_id.png.png" alt="Obtain VPC ID"/>
</p>
<p align="center"><i>Figure 5.5: Example to obtain VPC ID</i></p>
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_subnet_id.png" alt="Obtain Subnet ID"/>
</p>
<p align="center"><i>Figure 5.6: Example to obtain subnet ID</i></p>
</br>


2. The configuration parameter will pass to environment variable file in **Code > config.env**.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/config_env.png" alt="config.env"/>
</p>
<p align="center"><i>Figure 5.7: config.env file stores environment variables</i></p>
</br>


### **5.4 Create Images and ECS**

1. Run **create_images_and_ecs.bat.** This batch file will execute **main.py** to create images and ECS.
2. Input number of sheets to determine which sheet in **ids_list.xlsx** to be used in creating images and servers. The **previous running** sheet number will also be shown in figure below. 
 
:warning: *Note: None in figure below indicate that the program never run before.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd.png" alt="Command Prompt"/>
</p>
<p align="center"><i>Figure 5.8: Command Prompt shows Previous running: None</i></p>
</br>


### **5.5 Delete Images**

1. Run *delete_images.bat*. This batch file will execute *deleteImage.py* to delete all created Images in Huawei Cloud.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/delete_image_bat.png" alt="Batch file to delete images"/>
</p>
<p align="center"><i>Figure 5.9: delete_images.bat</i></p>
</br>


### **5.6 Delete ECS**

1.  Run *delete_servers.bat.* This batch file will execute deleteServer.py to delete all created Servers in Huawei Cloud. 

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/delete_server_bat.png" alt="Batch file to delete server"/>
</p>
<p align="center"><i>Figure 5.10: delete_servers.bat</i></p>
</br>
