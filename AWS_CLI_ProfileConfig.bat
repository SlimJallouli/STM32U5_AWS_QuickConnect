::******************************************************************************
::* @file    awsConfig.bat
::* @author  MCD Application Team
::* @brief   Configures aws cli for prod account
::******************************************************************************
::* @attention
::*
::* <h2><center>&copy; COPYRIGHT 2015 STMicroelectronics</center></h2>
::*
::* Licensed under MCD-ST Liberty SW License Agreement V2, (the "License");
::* You may not use this file except in compliance with the License.
::* You may obtain a copy of the License at:
::*
::*        http://www.st.com/software_license_agreement_liberty_v2
::*
::* Unless required by applicable law or agreed to in writing, software 
::* distributed under the License is distributed on an "AS IS" BASIS, 
::* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
::* See the License for the specific language governing permissions and
::* limitations under the License.
::******************************************************************************

@echo off

::Setting provision profile credentials 
set provision_accessKey=1234567890ABCDEFG
set provision_secretKey=2YDnAuIZflnJt/bun8f2GoNScKQ8ao0YbnqFHUVBKNgEHg2k
set provision_profile=provision

::Setting dashboard profile credentials 
set dashboard_accessKey=1234567890ABCDEFG
set dashboard_secretKey=2YDnAuIZflnJt/bun8f2GoNScKQ8ao0YbnqFHUVBKNgEHg2k
set dashboard_profile=dashboard

set region=us-west-1
set outputForm=json


::Configures aws cli for prod account
(echo %provision_accessKey% && echo %provision_secretKey% && echo %region% && echo %outputForm%) | (aws configure --profile %provision_profile%)

(echo %dashboard_accessKey% && echo %dashboard_secretKey% && echo %region% && echo %outputForm%) | (aws configure --profile %dashboard_profile%)

@echo on
