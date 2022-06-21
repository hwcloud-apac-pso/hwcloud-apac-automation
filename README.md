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
### **Objective #1: Automate image creation from CBR and ECS provisioning**
<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/solution_overview1.png" alt="Solution Overview"/>
</p>
<p align="center"><i>Figure 2.0: image creation from CBR and ECS provisioning</i></p>
</br>

### **Objective #2: Automate image and ECS cleaning**
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
<p align="center"><i>Figure 3.1: Command Prompt check Python version</i></p>
<br/>

4. Install Python 3 and add Python to **PATH.** Open your browser and navigate to the [Downloads for Windows section](https://www.python.org/downloads/windows/) of the [official Python website](https://www.python.org/). Navigate to the Using [Python on Windows section](https://docs.python.org/3/using/windows.html) for steps to install Python in the Windows environment.
5. Please note that this program is only applicable for Windows environments only for now.
 

## **4. Getting Started**

Before starting to automate the process of creating images and Elastic Cloud Server (ECS) in Huawei Cloud, some steps need to be done:

1. Download Source File
2. Install Python Packages
3. Configure Environment Variable

### **Download Source Code**

1. Click [hwc_automation.zip](https://codeload.github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/zip/refs/heads/main)  to download the Source Code Zip archive file. Extract the Zip archive file after the download is complete.
2. Check [File Content.docx](https://raw.githubusercontent.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/main/Reference/File%20Content.docx) for the file content.


### **Install Python Packages**
1. Open the **hwc_automation** folder you have downloaded and extracted it in the previous step.
2. Inside the folder, find **install.bat** and double-click to run it. 
3. This batch file will install all the Python Packages defined in **requirement.txt.**
4. Python packages in **requirement.txt**
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
      1. On the console homepage, hover over the username in the upper right corner and choose <b>My Credentials</b> from the drop-down list. </br>
      2. Choose <b>Access Key</b> from the navigation tab at the left and click <b>Create Access Key.</b></br> 
      3. Click Download. </br>
      4. Open the <b>credentials.csv</b> you have downloaded to obtain <b>AK/SK pair.</b>
    </td>
  </tr>
  <tr>
    <td>Admin Pass</td>
    <td>
       1. On the console homepage, under <b>Management & Governance</b>, click <b>Identity and Access Management</b>. </br>
       2. In the navigation pane on the left, choose <b>Account Security</b>. </br>
       3. On the <b>Account Security</b> Settings page, select <b>Password Policy</b> in the navigation pane. </br>
       4. Follow the <b>Password Policy</b> to set Admin Pass. Admin Pass is required to create ECS and login into the ECS.
   </td>
  </tr>
 <tr>
    <td>VPC ID</td>
    <td>
       1. On the console homepage, under <b>Network</b>, click <b>Virtual Private Cloud.</b> </br>
       2. The VPC ID will appear once the cursor hovers over the VPC name.  </br>
       3. After that, click the copy to clipboard icon beside the VPC ID to copy it.
    </td>
  </tr>
 <tr>
    <td>Subnet ID</td>
    <td>
       1. On the console homepage, under <b>Network</b>, click <b>Virtual Private Cloud</b>.</br>
       2. On the navigation pane at the left, click Subnets.</br>
       3. On the displayed Subnets page, locate your mouse cursor on the Subnets name.</br>
       4. The subnet ID will appear once the cursor hovers over the subnet name. After that, click the copy to clipboard icon beside the subnet ID to copy it.
   </td>
  </tr>
</table>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd_config.png" alt="Command Prompt"/>
</p>
<p align="center"><i>Figure 4.0: Command Prompt to input configuration parameters.</i></p>
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_vpc_id.png" alt="Obtain VPC ID"/>
</p>
<p align="center"><i>Figure 4.1: Example to obtain VPC ID</i></p>
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/get_subnet_id.png" alt="Obtain Subnet ID"/>
</p>
<p align="center"><i>Figure 4.2: Example to obtain subnet ID</i></p>
</br>

5.	Parameter input by the user will save in the **config.env** environment variable file. You may open the **hwc_automation > Code > config.env** file to verify that the parameters are correctly declared.

## **5. Demonstration of Automation**

### **Create Images and ECS**
In this demo, we are going to automate the process of creating a Full-ECS image from Cloud Backup and Recovery (CBR) backup and creating an Elastic Cloud Server (ECS) from the created images. Step by step is as below:
1.	Inside the **hwc_automation** folder, find **create_image_and_ecs.bat** and double click to run it.
2.	This batch file will start a command prompt to show the **number of sheets of the previous running** and ask the user to **input the number of sheets that need to be used in the current running** as shown in Figure 5.0. 

> Note: None in the figure below indicate that the program never run before.

3.	The input is used to determine which sheet in **ids_list.xlsx** is to be used in creating images and servers. For example, if we input **1, sheet1** in **ids_list.xlsx** will be used while if we input **2, sheet2** will be used accordingly. 

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/cmd.png" alt="Command Prompt"/>
</p>
<p align="center"><i>Figure 5.0: Command Prompt shows Previous running: None</i></p>
</br>

4. In this demo, we will use **sheet1** to create images and servers, so we input **1**.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/CBR_backup_details.png" alt="CBR backup details"/>
</p>
<p align="center"><i>Figure 5.1: CBR backup details in Sheet1</i></p>
</br>

5.	After inputting the number of sheets, the batch file will continue with executing the **main.py** Python file to create Images and ECSs.
6.	This Python file will retrieve the backup ID from **sheet1**, and use the backup ID to create an image and ECS.
7.	Figure 5.2 below showed that the images and ECS are successfully created using **row 3 (6d8055a8-4375-46e4-a7e3-e57ba865f122)** and **row 4 (444fca5a-8a91-4398-b6fb-df9ba305e3ca)** backup ID.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/success.png" alt="Image and ECS successfully created"/>
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/success1.png" alt="Image and ECS successfully created"/>
</p>
<p align="center"><i>Figure 5.2: Image and ECS successfully created</i></p>
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/img_hwc.png" alt="IMG in HWC"/>
</p>
<p align="center"><i>Figure 5.3: Image successfully created in Huawei Cloud console</i></p>
</br>

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/ecs_hwc.png" alt="ECS in HWC"/>
</p>
<p align="center"><i>Figure 5.4: ECS successfully created in Huawei Cloud console</i></p>
</br>

8.	If the image and ECS are successfully created, the Image ID and ECS ID will be saved in **resource_list.xlsx**. 

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/img_id_excel.png" alt="ECS in HWC"/>
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/ecs_id_excel.png" alt="Image and Server sheets in resource_list.xlsx"/>
</p>
<p align="center"><i>Figure 5.5: Image and Server sheets in resource_list.xlsx</i></p>
</br>

9.	Figure 5.6 below showed that the image was failed to create using **row 2 (00f0ff7a-b5b2-41fb-90d1-d2d348923c60)** backup ID.
10.	The image creation might fail if:
  - The backup ID is already registered as an image.
  - The backup ID provided in Excel is invalid.

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/failed.png" alt="image creation failed"/>
</p>
<p align="center"><i>Figure 5.6: Image creation failed due to the backup ID already used to create an image.</i></p>
</br>

11.	If the image creation fails, the **vault ID** and **backup ID** will be saved in the **“Failed”** sheet in **resource_list.xlsx**. 
12.	If the image is successfully created but ECS creation failed, the **vault ID, backup ID**, and image ID will be saved in the **“Failed”** sheet in **resource_list.xlsx**. 

<p align="center">
   <img src="https://github.com/terraform-hwcloud-apac-pso-modules/hwcloud-apac-automation/blob/main/Image/failed_list_excel.png" alt="Failed sheets"/>
</p>
<p align="center"><i>Figure 5.7: Failed sheets in resource_list.xlsx.</i></p>
</br>


## 6. Resource Cleaning

Once the resources are no longer used, It’s a good idea to remove all the resources you created so Huawei Cloud doesn’t charge you for them. 

### Delete Images
1.	Inside the hwc_automation folder, find delete_images.bat and double click to run it.
2.	This batch file will execute the deleteImage.py Python File.
3.	deleteImage.py will read the images’ ID from the resourse_list.xlsx Excel file and use the ID to delete Images in Huawei Cloud.

### Delete Server (ECS)
1.	 Run delete_servers.bat. This batch file will execute the deleteServer.py Python file.
2.	deleteServer.py will read the servers’ ID from the resourse_list.xlsx Excel file and use the ID to delete servers in Huawei Cloud.


