# **Automation on Elastic Cloud Server Provisioning using a created image from Cloud Backup and Recovery**

## **1.0 Problem Statement**

Currently, the process of creating a Full-ECS image from Cloud Backup and Recovery (CBR) backup and creating Elastic Cloud Server (ECS) from the created images is done manually by the user using the Huawei Cloud console. 

Users have to repeat the step from creating an image from CBR backup to creating ECS with the image created many times because there is a very huge number of backups that need to be restored. This is very time-consuming and might have human errors.

## **1.1 Objective**

In this artifact, we are going to achieve the below objectives:

1. To automate the process of creating a Full-ECS image from Cloud Backup and Recovery (CBR) and creating an Elastic Cloud Server (ECS) from the created image using Huawei Python SDK.
2. To automate the process of resource cleaning using Huawei Python SDK.
3. To develop an automated program to reduce time consumption. 


## **2. Solution Overview**
### **2.1 Objective #1: Automate image creation from CBR and ECS provisioning**
<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/solution_overview1.png" alt="Solution Overview"/>
</p>
<p align="center"><i>Figure 2.0: image creation from CBR and ECS provisioning</i></p>
</br>

### **2.1 Objective #1: Automate image and ECS cleaning**
<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/solution_overview2.png" alt="Solution Overview"/>
</p>
<p align="center"><i>Figure 2.1: image and ECS cleaning</i></p>
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

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/check_python_version.png" alt="Create Credentials"/>
</p>
<p align="center"><i>Figure 3.0: Command Prompt check Python version</i></p>
<br/>

4. Install Python 3 and add Python to **PATH.** Open your browser and navigate to the [Downloads for Windows section](https://www.python.org/downloads/windows/) of the [official Python website](https://www.python.org/).Navigate to the Using [Python on Windows section](https://docs.python.org/3/using/windows.html) for steps to install Python in the Windows environment.
5. Please note that this program is only applicable for Windows environments only for now.
 

## **4. Getting Started**

Before starting to automate the process of creating images and Elastic Cloud Server (ECS) in Huawei Cloud, some steps need to be done:

1. Download Source File
2. Install Python Packages
3. Configure Environment Variable

### **Download Source Code**

1. Click [hwc_automation.zip](https://codeload.github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/zip/refs/heads/main)  to download the Source Code Zip archive file. Extract the Zip archive file after the download is complete.
2. Check [File Content.docx](https://www.google.com) for the file content.


### **Install Python Packages
1. Open the *hwc_automation* folder you have downloaded and extracted it in the previous step.
2. Inside the folder, find *install.bat* and double-click to run it. **
3. This batch file will install all the Python Packages defined in *requirement.txt.*
4. Python packages in *requirement.txt*
  - huaweicloudsdkecs
  - huaweicloudsdkims
  - huaweicloudsdksmn
  - huaweicloudsdksms
  - requests
  - python-dotenv
  - openpyxl 
  - pandas

### **Configure Environment Variables**

1. Environment variables need to be declared first before proceeding to create Image, create ECS, delete Image, and Delete ECS.
2. Inside the **hwc_automation** folder, find **config.bat** and double-click to run it.
3. This batch file will start Command Prompt and ask the user to input parameters as prompted.
4. The parameters required and steps to obtain as shown below:

<table>
  <tr>
    <th><b>Parameter</b></th>
    <th><b>Steps</b></th>
  </tr>
  <tr>
    <td>Access Key & Secret Key (AK/SK pair)</td>
    <td>
      1. On the console homepage, hover over the username in the upper right corner and choose My Credentials from the drop-down list. </br>
      2. Choose Access Key from the navigation tab at the left and click Create Access Key.</br> 
      3. Click Download. 
      4. Open the credentials.csv you have downloaded to obtain AK/SK pair.
    </td>
  </tr>
  <tr>
    <td>Admin Pass</td>
    <td>
       1. On the console homepage, under Management & Governance, click Identity and Access Management. </br>
       2. In the navigation pane on the left, choose Account Security. </br>
       3. On the Account Security Settings page, select Password Policy in the navigation pane. </br>
       4. Follow the Password Policy to set Admin Pass. Admin Pass is required to create ECS and login into the ECS.
   </td>
  </tr>
 <tr>
    <td>VPC ID</td>
    <td>
       1. On the console homepage, under Network, click Virtual Private Cloud.
       2. 
       3. 
    </td>
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


### **5.3 Configure Environment Variables**

#### **5.3.1 Run config.bat batch file**

1. Run *config.bat*. This batch file will start Command Prompt and ask the user to input parameters as prompted.
2. Parameter input by the user will save in *the config.env* environment variable file. 
3. Environment variables need to be declared first before proceeding to create Image, create ECS, delete Image, and Delete ECS.
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd_config.png" alt="Command Prompt"/>
</p>
<p align="center"><i>Figure 5.4: Command Prompt to input configuration parameters.</i></p>
</br>

#### **5.3.2 Obtain VPC ID**

1. On the console homepage, under **Network**, click **Virtual Private Cloud**.
2. On the **Virtual Private Cloud** page, locate your mouse cursor on the VPC name
3. The VPC ID will appear once the cursor hovers over the VPC name. After that, click the copy to clipboard icon beside the VPC ID to copy it.
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_vpc_id.png" alt="Obtain VPC ID"/>
</p>
<p align="center"><i>Figure 5.5: Example to obtain VPC ID</i></p>
</br>

#### **5.3.3 Obtain Subnet ID**

1. On the console homepage, under **Network**, click **Virtual Private Cloud**.
2. On the navigation pane at the left, click **Subnets**.
3. On the displayed Subnets page, locate your mouse cursor on the Subnets name.
4. The subnet ID will appear once the cursor hovers over the subnet name. After that, click the copy to clipboard icon beside the subnet ID to copy it.
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_subnet_id.png" alt="Obtain Subnet ID"/>
</p>
<p align="center"><i>Figure 5.6: Example to obtain subnet ID</i></p>
</br>

#### **5.3.4 View Environment Variable file**

1. The configuration parameter is saved in the environment variable file in *Code > config.env.*
</br>
<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/config_env.png" alt="config.env"/>
</p>
<p align="center"><i>Figure 5.7: config.env file stores environment variables</i></p>
</br>


### **5.4 Create Images and ECS**

1. Run **create_images_and_ecs.bat.** This batch file will execute **main.py** to create images and ECS.
2. Input sheet number to determine which sheet in **ids_list.xlsx** to be used in creating images and servers. 
3. The **previous running** sheet number will also be shown in the command prompt to let the user know which number of the sheet is previously used to create images and server.
 
:warning: *Note: None in the figure below indicate that the program never run before.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd.png" alt="Command Prompt"/>
</p>
<p align="center"><i>Figure 5.8: Command Prompt shows Previous running: None</i></p>
</br>


### **5.5 Delete Images**
:recycle: Once the resources are no longer used, It’s a good idea to remove all the resources you created so Huawei Cloud doesn’t charge you for them. 

#### **5.5.1 Delete Images**
1. Run **delete_images.bat**. This batch file will execute **deleteImage.py** Python file.
2.  **deleteImage.py** will read Image ID from **resourse_list.xlsx** Excel file and use the ID to delete Image in Huawei Cloud.
</br>
<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/delete_image_bat.png" alt="Batch file to delete images"/>
</p>
<p align="center"><i>Figure 5.9: delete_images.bat</i></p>
</br>

#### **5.5.2 Delete Server (ECS)**

1.  Run **delete_servers.bat.** This batch file will execute **deleteServer.py** Python file. 
2.  **deleteServer.py** will read server ID from **resourse_list.xlsx** Excel file use the ID to delete server in Huawei Cloud.
</br>
<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/delete_server_bat.png" alt="Batch file to delete server"/>
</p>
<p align="center"><i>Figure 5.10: delete_servers.bat</i></p>
