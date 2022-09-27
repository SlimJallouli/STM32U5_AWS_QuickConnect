::******************************************************************************
::* @file    awsConfig.bat
::* @author  MCD Application Team
::* @brief   Configures aws cli for prod account
::******************************************************************************
:: * Copyright (c) 2022 STMicroelectronics.
::
:: * All rights reserved.
::
:: * This software component is licensed by ST under BSD 3-Clause license,
:: * the "License"; You may not use this file except in compliance with the
:: * License. You may obtain a copy of the License at:
:: *                        opensource.org/licenses/BSD-3-Clause
:: *
:: ******************************************************************************

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
