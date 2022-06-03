# coding: utf-8
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkims.v2.region.ims_region import ImsRegion
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkims.v2 import *
from huaweicloudsdkecs.v2 import *
from dotenv import load_dotenv
import os
import pandas as pd
import sys
from time import sleep, perf_counter
from openpyxl import load_workbook

pd.options.mode.chained_assignment = None

#declare clients
def declare_client(resource_region, ak, sk):
    credentials = BasicCredentials(ak, sk) \
    # declare ims client
    imsClient = ImsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(ImsRegion.value_of(resource_region)) \
        .build()

    # declare ecs client
    ecsClient = EcsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EcsRegion.value_of(resource_region)) \
        .build()
    
    return [imsClient, ecsClient]


##### CREATE FULL ECS IMAGE FROM CBR BACKUPS #####
# create image from CBR backups
def create_image(client, img_name, backupID, vaultID):
    print("CBR Backup ID: " + backupID)
    createimg_req = CreateWholeImageRequest()
    createimg_req.body = CreateWholeImageRequestBody(
        name = img_name,
        description = "Creating a full-ECS image from a CBR backup",
        whole_image_type = "CBR",
        vault_id = vaultID,
        backup_id = backupID
    )
    createimg_res = client.create_whole_image(createimg_req).to_dict()
    createimg_job_id = createimg_res['job_id']

    # check the status of image creation
    print("Start to create image ......")
    while True:
        showimgjob_req = ShowJobRequest(job_id = createimg_job_id)
        showimgjob_res = client.show_job(showimgjob_req).to_dict()
        showimgjob_status = showimgjob_res['status']
        print("Image Status -----> " + showimgjob_status)
        sleep(5)
        if showimgjob_status == "SUCCESS":
            break
        if showimgjob_status == "FAIL":
            img_id = None
            return img_id
            
    # obtain the latest image id
    listimgID_req = ListImagesRequest(imagetype="private")
    listimgID_res = client.list_images(listimgID_req).to_dict()
    img_id = listimgID_res['images'][0]['id']
    print("Image is created successfully! IMG's ID is " + img_id + "\n")
    return img_id



##### PROVISION ECS USING CREATED IMAGE #####
# create ecs using created image
def create_ecs(client, smsVERSION, eipID, subnetID, img_id, flavorREF, ecs_name, vpcID, adminPW):
    createecs_req = CreateServersRequest()
    rootVolumePrePaidServerRootVolume = PrePaidServerRootVolume(volumetype="SAS")
    publicipPrePaidServerPublicip = PrePaidServerPublicip(
        id = eipID,
    )
    listPrePaidServerNicNicsServer = [
        PrePaidServerNic(
            subnet_id = subnetID
        )
    ]
    # base64 encoding
    # rem cmd
    # curl.exe -o C:\SMS-Agent-Py3.exe https://sms-agent-bucket-2.obs.my-kualalumpur-1.alphaedge.tmone.com.my/SMS-Agent-Py3.exe
    # rem cmd
    # curl.exe -o C:\SMS-Agent-Py2.exe https://sms-agent-bucket-2.obs.my-kualalumpur-1.alphaedge.tmone.com.my/SMS-Agent-Py2.exe
        
    if smsVERSION == "sms3":
        user_data = "cmVtIGNtZCANCmN1cmwuZXhlIC1vIEM6XFNNUy1BZ2VudC1QeTMuZXhlIGh0dHBzOi8vc21zLWFnZW50LWJ1Y2tldC0yLm9icy5teS1rdWFsYWx1bXB1ci0xLmFscGhhZWRnZS50bW9uZS5jb20ubXkvU01TLUFnZW50LVB5My5leGU="
    else:
        user_data = "cmVtIGNtZA0KY3VybC5leGUgLW8gQzpcU01TLUFnZW50LVB5Mi5leGUgaHR0cHM6Ly9zbXMtYWdlbnQtYnVja2V0LTIub2JzLm15LWt1YWxhbHVtcHVyLTEuYWxwaGFlZGdlLnRtb25lLmNvbS5teS9TTVMtQWdlbnQtUHkyLmV4ZQ=="
    serverPrePaidServer = PrePaidServer(
        image_ref = img_id,
        flavor_ref = flavorREF,
        name = ecs_name,
        vpcid = vpcID,
        nics = listPrePaidServerNicNicsServer,
        publicip = publicipPrePaidServerPublicip,
        root_volume = rootVolumePrePaidServerRootVolume,
        admin_pass = adminPW,
        user_data = user_data
    )
    
    createecs_req.body = CreateServersRequestBody(
        server = serverPrePaidServer
    )
    
    createecs_res = client.create_servers(createecs_req).to_dict()
    str2 = ""
    ecs_id = str2.join(createecs_res['server_ids'])
    createecs_job_id = createecs_res['job_id']
            
    # check the status of ecs creation
    print("Start to create ECS ......")
    while True:
        showecsjob_req = ShowJobRequest(job_id = createecs_job_id)
        showecsjob_res = client.show_job(showecsjob_req).to_dict()
        showecsjob_status = showecsjob_res['status']
        print("ECS Status -----> " + showecsjob_status)
        sleep(10)
        if showecsjob_status == "SUCCESS":
            print("ECS is created successfully! ECS's ID is " + ecs_id + "\n")
            break
        if showecsjob_status == "FAIL":
            ecs_id = None
            break
    return ecs_id

